/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PosStore } from '@point_of_sale/app/store/pos_store';

console.log("patch partner");

patch(PosStore.prototype, {
    async _processData(loadedData) {
        await super._processData(...arguments)

        if (!this.env) {
            console.error("env not found");
            return;
        }
        
        let dataPartner = loadedData['res.partner']

        this.env.availablePartnersInPos = [];
        for (let i = 0; i < dataPartner.length; i++) {
            if (dataPartner[i].is_available_in_pos) {
                this.env.availablePartnersInPos.push(dataPartner[i]);
            }
        }
        console.log("Partners available in POS:", this.env.availablePartnersInPos);
    }
})

