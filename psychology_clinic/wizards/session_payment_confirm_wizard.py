# psychology_clinic/wizards/session_payment_confirm_wizard.py

from odoo import models, fields, api
from odoo.exceptions import UserError


class SessionPaymentConfirmWizard(models.TransientModel):
    _name = 'session.payment.confirm.wizard'
    _description = 'Confirmación de actualización de pago'

    session_id = fields.Many2one('psychology.session', string="Sesión", required=True)
    new_amount = fields.Float(string="Nuevo monto") 
    new_method = fields.Selection(selection=[ 
        ('efectivo', 'Efectivo'), 
        ('transferencia', 'Transferencia'), 
        ('mercadopago', 'MercadoPago'), 
        ('other', 'Otro'), 
        ], string="Nuevo método de pago")


    @api.model 
    def default_get(self, fields_list): 
        """Inicializa los campos con los valores actuales de la sesión""" 
        defaults = super().default_get(fields_list) 
        session_id = self._context.get('active_id') 
        if session_id: 
            session = self.env['psychology.session'].browse(session_id) 
            defaults['session_id'] = session.id 
            defaults['new_amount'] = session.amount_charged 
            defaults['new_method'] = session.payment_method 
        return defaults


    def action_confirm(self):
        session = self.session_id
        payment = session.payment_id

        # Actualizar la sesión con los nuevos valores 
        session.with_context(from_wizard=True).write({ 
            'amount_charged': self.new_amount, 
            'payment_method': self.new_method,
            })

        if not payment: 
            journal = self._get_journal_from_session(self.new_method) 
            if not journal: 
                raise UserError("No se encontró un diario para el método de pago seleccionado.") 
            payment = self.env['account.payment'].create({ 
                'amount': self.new_amount, 
                'payment_type': 'inbound', 
                'partner_id': session.patient_id.id, 
                'payment_method_id': self.env.ref('account.account_payment_method_manual_in').id, 
                'journal_id': journal.id, 
                }) 
            session.payment_id = payment 
        else: 
            if payment.state == 'posted': 
                raise UserError("El pago ya está confirmado. Debe restablecerlo a borrador para modificarlo.") 
            journal = self._get_journal_from_session(self.new_method) 
            if not journal: 
                raise UserError("No se encontró un diario para el método de pago seleccionado.") 
            payment.amount = self.new_amount 
            payment.journal_id = journal.id


    def _get_journal_from_session(self, method):
        mapping = {
            'efectivo': self.env['account.journal'].search([('code','=','EFEC')], limit=1),
            'transferencia': self.env['account.journal'].search([('code','=','BCO')], limit=1),
            'mercadopago': self.env['account.journal'].search([('code','=','MP')], limit=1),
            'other': self.env['account.journal'].search([('code','=','EFEC')], limit=1),
        }
        return mapping.get(method)


    def action_cancel(self):
        return {'type': 'ir.actions.act_window_close'}

