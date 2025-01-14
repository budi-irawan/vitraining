odoo.define('point_of_sale.CustomAction', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');

    /**
     * @props partner
     * @emits click-partner
     * @emits click-pay
     */
    class CustomAction extends PosComponent {
        get isLongName() {
            return this.props.partner && this.props.partner.name.length > 10;
        }
    }
    CustomAction.template = 'CustomAction';
    CustomAction.defaultProps = {
        isActionButtonHighlighted: false,
    }

    Registries.Component.add(CustomAction);

    return CustomAction;
});
