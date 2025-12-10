# -*- coding: utf-8 -*-
{
    'name': "partner_chinese_stats",

    'summary': "Modulo que permite ver el signo del horoscopo chino",

    'description': """
Este modulo extiende de res partner añadiendo los siguientes 3 datos a contactos:
-Fecha de nacimiendo
-Edad
-Signo del horoscopo chino
    """,

    'author': "Daniel Castelao",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

