# -*- coding: utf-8 -*-
{
    'name': "oct_extend_tarifas",

    'summary': """ 
        Module to extend the rates""",

    'description': """
        Module to add functionalities that allow you to extend the ways to calculate prices 
    """,

    'author': "Marcos M. Martinez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing 
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': "1.0",

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

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