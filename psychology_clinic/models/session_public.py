# psychology_clinic/models/session_public.py

from odoo import models, fields, api, _
from datetime import timedelta
from odoo.exceptions import ValidationError


class PsychologySession(models.Model):
    _name = 'psychology.session'
    _description = 'Sesión de Terapia (versión pública)'
    _order = 'session_date desc'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    # ---------------------------------------------------------
    # CAMPOS PRINCIPALES
    # ---------------------------------------------------------
    patient_id = fields.Many2one(
        'psychology.patient',
        string='Paciente',
        required=True,
        ondelete='cascade'
    )

    psychologist_id = fields.Many2one(
        'res.partner',
        string='Psicólogo',
        domain=[('is_psychologist', '=', True)],
        required=True,
        ondelete='restrict'
    )

    name = fields.Char(
        string='Descripción',
        compute='_compute_name',
        store=True,
        readonly=True
    )

    session_date = fields.Datetime(
        string='Fecha y Hora',
        required=True,
        default=fields.Datetime.now
    )

    duration = fields.Integer(
        string='Duración (min)',
        default=45,
        required=True
    )

    session_end = fields.Datetime(
        string='Fin de sesión',
        compute='_compute_session_end',
        store=True
    )

    session_type = fields.Selection([
        ('individual', 'Individual'),
        ('couple', 'Pareja'),
        ('family', 'Familiar'),
        ('evaluation', 'Evaluación'),
        ('initial', 'Primera consulta'),
        ('other', 'Otro')
    ], default='individual')

    diagnosis = fields.Char(string='Diagnóstico')
    session_notes = fields.Html(string='Notas')

    calendar_event_id = fields.Many2one(
        'calendar.event',
        string='Evento de Calendario',
        ondelete='cascade'
    )

    # ---------------------------------------------------------
    # COMPUTES
    # ---------------------------------------------------------
    @api.depends('session_date', 'duration')
    def _compute_session_end(self):
        for rec in self:
            if rec.session_date and rec.duration:
                rec.session_end = rec.session_date + timedelta(minutes=rec.duration)
            else:
                rec.session_end = False

    @api.depends('patient_id')
    def _compute_name(self):
        for rec in self:
            rec.name = _("Sesión con %s") % rec.patient_id.name if rec.patient_id else _("Nueva sesión")

    # ---------------------------------------------------------
    # VALIDACIONES
    # ---------------------------------------------------------
    @api.constrains('duration')
    def _check_duration(self):
        for rec in self:
            if rec.duration < 30:
                raise ValidationError("La duración mínima de una sesión es de 30 minutos.")

    @api.constrains('session_date', 'session_end', 'psychologist_id')
    def _check_overlap(self):
        for rec in self:
            if not rec.session_date or not rec.session_end:
                continue

            overlap = self.search([
                ('id', '!=', rec.id),
                ('psychologist_id', '=', rec.psychologist_id.id),
                ('session_date', '<=', rec.session_end),
                ('session_end', '>=', rec.session_date),
            ], limit=1)

            if overlap:
                raise ValidationError(
                    _("Ya existe una sesión para este profesional en el horario seleccionado.")
                )

    # ---------------------------------------------------------
    # CREATE (simplificado)
    # ---------------------------------------------------------
    @api.model
    def create(self, vals):
        session = super().create(vals)
        session._create_calendar_event()
        return session

    # ---------------------------------------------------------
    # CALENDAR (versión básica)
    # ---------------------------------------------------------
    def _create_calendar_event(self):
        for rec in self:
            if not rec.session_date or not rec.duration:
                continue

            end = rec.session_date + timedelta(minutes=rec.duration)

            partners = []
            if rec.patient_id.partner_id:
                partners.append(rec.patient_id.partner_id.id)
            if rec.psychologist_id:
                partners.append(rec.psychologist_id.id)

            event = self.env['calendar.event'].create({
                'name': rec.name,
                'start': rec.session_date,
                'stop': end,
                'partner_ids': [(6, 0, partners)],
            })

            rec.calendar_event_id = event.id
