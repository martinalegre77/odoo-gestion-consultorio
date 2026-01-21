# psychology_clinic/models/patient_public.py

from odoo import models, fields, api
from odoo.tools.translate import _
from odoo.exceptions import UserError



class PsychologyPatient(models.Model):
    _name = 'psychology.patient'
    _description = 'Paciente de Consultorio de Psicología'

    # ---------------------------------------------------------
    # CAMPOS PRINCIPALES
    # ---------------------------------------------------------
    partner_id = fields.Many2one('res.partner', string='Contacto Relacionado', required=True, ondelete='restrict')
    name = fields.Char(related='partner_id.name', string='Nombre del Paciente', store=True, readonly=True)
    dni = fields.Char(string='DNI', size=10, help="Documento Nacional de Identidad del paciente.")
    
    patient_code = fields.Char(string='Código de Paciente', required=True, copy=False, readonly=True,
                                default=lambda self: self.env['ir.sequence'].next_by_code('psychology.patient.code') or _('New'))
    phone = fields.Char(string='Teléfono', related='partner_id.phone', store=True, readonly=False)
    email = fields.Char(string='Correo Electrónico', related='partner_id.email', store=True, readonly=False, help="Importante para el envío de notificaciones")
    birth_date = fields.Date(string='Fecha de Nacimiento')
    age = fields.Integer(string='Edad', compute='_compute_age', store=True)
    gender = fields.Selection([
        ('male', 'Masculino'),
        ('female', 'Femenino'),
        ('other', 'Otro'),
        ('prefer_not_say', 'Prefiero no decir')
    ], string='Género')
    occupation = fields.Char(string='Ocupación')
    marital_status = fields.Selection([
        ('single', 'Soltero/a'),
        ('married', 'Casado/a'),
        ('divorced', 'Divorciado/a'),
        ('widowed', 'Viudo/a'),
        ('union_libre', 'Unión Libre')
    ], string='Estado Civil')

    has_social_security = fields.Boolean(string='Tiene Obra Social', default=False)
    social_security_name = fields.Char(string='Nombre Obra Social')
    social_security_number = fields.Char(string='Número de Afiliado')

    emergency_contact_name = fields.Char(string='Contacto de Emergencia')
    emergency_contact_phone = fields.Char(string='Teléfono de Emergencia')

    referral_source = fields.Char(string='Fuente de Referencia', help="Por que medio se enteró del consultorio?")
    is_active = fields.Boolean(string='Paciente Activo', default=True, help="Paciente que está actualmente recibiendo tratamiento terapéutico.")

    # Informacion clinica
    reason_for_consultation = fields.Text(string='Motivo de Consulta', help="Para dejar registro del motivo que lo llevó a requerir una consulta al Psicólogo.")
    medical_history = fields.Text(string='Antecedentes Médicos', help="Registro de patologías o enfermedades que el profesional considere necesario.")
    family_history = fields.Text(string='Antecedentes Familiares', help="Registro de patologías o enfermedades de familiares que el profesional considere necesario.")
    current_medication = fields.Text(string='Toma Medicación', help="Registro de medicación que el paciente tome o haya tomado y que el profesional considere relevante.")
    diagnosis = fields.Char(string='Diagnóstico Principal', help="Diagnóstico del profesional")
    diagnosis_color = fields.Char(compute='_compute_diagnosis_color', store=False)

    # Campo relacional para las sesiones del paciente
    session_ids = fields.One2many('psychology.session', 
                                    'patient_id', 
                                    string='Sesiones'
                                    )

    # Psicologo terapeuta
    psychologist_user_id = fields.Many2one('res.users',
                                            string='Psicólogo Responsable',
                                            domain=lambda self: self._get_psychologist_domain(),
                                            )

    # Eventos para historias clinicas
    clinical_event_ids = fields.One2many('psychology.clinical.history.event', 
                                        'patient_id', 
                                        string="Eventos Clínicos"
                                        )


    # ---------------------------------------------------------
    # CAMPOS CALCULADOS
    # ---------------------------------------------------------
    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                today = fields.Date.today()
                rec.age = today.year - rec.birth_date.year - \
                    ((today.month, today.day) < (rec.birth_date.month, rec.birth_date.day))
            else:
                rec.age = 0

    @api.depends('diagnosis')
    def _compute_diagnosis_color(self):
        for rec in self:
            rec.diagnosis_color = 'text-secondary'    


    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------
    @api.model
    def create(self, vals):
        if not vals.get('psychologist_user_id') and self.env.user.has_group('psychology_clinic.group_psychologist'):
            vals['psychologist_user_id'] = self.env.uid
        return super().create(vals)


    # ---------------------------------------------------------
    # WRITE
    # ---------------------------------------------------------
    def write(self, vals):

        # Si el usuario no es psicólogo no se modifica el diagnóstico
        if 'diagnosis' in vals and not self._is_user_psychologist():
            raise UserError("Solo los psicólogos pueden modificar el diagnóstico.")

        # Si el usuario no es manager no se modifica el psicólogo
        if 'psychologist_user_id' in vals and not self._is_user_manager():
            raise UserError("Solo los usuarios con rol de Manager pueden modificar el psicólogo asignado.")


        # Capturar psicólogos anteriores por paciente antes del write
        old_partners_by_patient = {
            patient.id: patient.psychologist_user_id.partner_id if patient.psychologist_user_id else False
            for patient in self
        }

        res = super().write(vals)

        for patient in self:
            # Sincronizar diagnóstico en sesiones
            if 'diagnosis' in vals:
                # Sincronización de información clínica con sesiones relacionadas
                # (Implementación completa omitida en versión pública)

            # Actualizar psicólogo en sesiones futuras si se modificó
            if 'psychologist_user_id' in vals:
                # (Implementación completa omitida en versión pública)

                if not new_partner:
                    raise ValidationError("El nuevo psicólogo no tiene un contacto asociado.")

                # Guarda cambio en la História Clínica
                if old_partner != new_partner:
                    self.env['psychology.clinical.history.event'].create({
                                                                        'patient_id': patient.id,
                                                                        'event_type': 'psychologist_change',
                                                                        'description': f"Psicólogo asignado: {patient.psychologist_user_id.name}",
                                                                        'changed_by': self.env.user.id,
                                                                    })

               # (Implementación completa omitida en versión pública)
        
        return res


    # ---------------------------------------------------------
    # FUNCIONES
    # ---------------------------------------------------------
    @api.model
    def _get_psychologist_domain(self):
        group = self.env.ref('psychology_clinic.group_psychologist')
        return [('id', 'in', group.users.ids)]

    
    @api.model
    def _is_user_psychologist(self):
        return self.env.user.has_group('psychology_clinic.group_psychologist')


    @api.model
    def _is_user_manager(self):
        return self.env.user.has_group('psychology_clinic.group_manager')
