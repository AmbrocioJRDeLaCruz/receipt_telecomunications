# -*- coding: utf-8 -*-
{
    'name': "Recivo Informatica & telecomunicaciones",

    'summary': """
        Recivo Informatica & telecomunicaciones
        """,

    'description': """
        Recivo Informatica & telecomunicaciones
    """,

    'author': "Ambrocio De La Cruz",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale'],

    # always loaded
    'data': [
        'report/paperformat.xml',
        'report/receipt_account_move.xml',
        'report/receipt_sale_order.xml',
        'views/account_move.xml',
        'views/sale_order.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
