/** @odoo-module **/

import { PosGlobalState } from 'point_of_sale.models';
import Registries from 'point_of_sale.Registries';

const PosButtonRestrict = (PosGlobalState) => 
    class PosButtonRestrict extends PosGlobalState {
        async _processData(loadedData) {
            console.log("INISIALISASI MODUL : ", loadedData);
            
            await super._processData(...arguments);
            this.disable_refund_button = loadedData['disable_refund_button']
        }
    }

Registries.Model.extend(PosGlobalState, PosButtonRestrict);