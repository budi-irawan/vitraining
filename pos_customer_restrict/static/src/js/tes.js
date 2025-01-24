/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PosStore } from '@point_of_sale/app/store/pos_store';

console.log("pos store prototype : ", PosStore.prototype);

patch(PosStore.prototype, {
    async selectPartner() {
        await super.selectPartner()
        // FIXME, find order to refund when we are in the ticketscreen.
        const currentOrder = this.get_order();
        if (!currentOrder) {
            return;
        }
        const currentPartner = currentOrder.get_partner();
        if (currentPartner && currentOrder.getHasRefundLines()) {
            this.popup.add(ErrorPopup, {
                title: _t("Can't change customer"),
                body: _t(
                    "This order already has refund lines for %s. We can't change the customer associated to it. Create a new order for the new customer.",
                    currentPartner.name
                ),
            });
            return;
        }
        console.log("current partner : ", currentPartner);
        
        const { confirmed, payload: newPartner } = await this.showTempScreen("PartnerListScreen", {
            partner: currentPartner,
        });
        if (confirmed) {
            currentOrder.set_partner(newPartner);
        }
    }
})