import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

class AwesomeDashboard extends Component {
    static template = "pos_customer_restrict.AwesomeDashboard";
}

registry.category("actions").add("pos_customer_restrict.dashboard", AwesomeDashboard)