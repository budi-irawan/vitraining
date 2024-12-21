from odoo import api, fields, models, _  

class Attendee(models.Model): 
    _name = "academic.attendee"

    name = fields.Char(string='Name',)
    session_id = fields.Many2one(
        comodel_name='academic.session',
        string='Session',
    )
    
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner',
    )

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        self.name = self.partner_id.id

    _sql_constraints = [
        ('partner_session_unique', 'UNIQUE(session_id,partner_id)', 'Multiple attendee detected')
    ]