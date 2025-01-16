from odoo import models, fields 

class RefundButton(models.Model):
    _inherit = 'pos.config'

    disable_refund_button = fields.Boolean('Disable Refund Button')

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_res_config_settings(self):
        result = super()._loader_params_res_config_settings()
        result['search_params']['fields'].append('disable_refund_button')  
        return result