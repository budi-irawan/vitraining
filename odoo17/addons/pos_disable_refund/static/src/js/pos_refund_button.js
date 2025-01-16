/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import { PosStore } from '@point_of_sale/app/store/pos_store';

console.log("patch ");

patch(PosStore.prototype, {
    async _processData(loadedData) {
        await super._processData(...arguments)

        if (!this.env) {
            console.error("env not found");
            return;
        }

        this.env.disable_refund_button = loadedData['pos.config'].disable_refund_button;
        console.log("DisableRefundButton saved to env : ", this.env.disable_refund_button);

    }
})

