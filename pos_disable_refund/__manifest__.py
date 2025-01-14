{
    'name': 'Disable Refund Button in POS',
    'version': '1.0',
    'summary': 'Disable refund button in POS based on a configuration',
    'author': 'Your Name',
    'depends': ['base','web','point_of_sale'],
    'data': [
        # 'views/assets.xml',
        'views/disable_refund.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_disable_refund/static/src/js/pos_refund_button.js',
            'pos_disable_refund/static/src/xml/pos_refund_button.xml',
            'pos_disable_refund/static/src/xml/pos_refund_button2.xml',
        ],
    },
    'installable': True,
    'application': False,
}
