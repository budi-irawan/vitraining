{
    'name': 'Disable Refund Button in POS',
    'version': '1.0',
    'summary': 'Disable refund button in POS based on a configuration',
    'author': 'Your Name',
    'depends': ['base','point_of_sale'],
    'data': [
        'views/disable_refund.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_disable_refund/static/src/js/pos_refund_button.js',
            'pos_disable_refund/static/src/xml/refund_button.xml',
            'pos_disable_refund/static/src/xml/inherit_ticket_screen.xml',
        ],
    },
    'installable': True,
    'application': False,
}
