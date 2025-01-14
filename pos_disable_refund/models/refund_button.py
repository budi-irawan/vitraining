from odoo import models, fields
import logging
_logger = logging.getLogger(__name__)

class RefundButton(models.Model):
    _inherit = 'pos.config'

    disable_refund_button = fields.Boolean('Disable Refund Button')

    # def _get_pos_ui_config(self):
    #     res = super(RefundButton, self)._get_pos_ui_config()
    #     res['disable_refund_button'] = self.disable_refund_button
    #     _logger.info("DATA DARI DB :", res)
    #     return res


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _pos_data_process(self, loaded_data):
        super()._pos_data_process(loaded_data)
        loaded_data['disable_refund_button'] = self.config_id.disable_refund_button