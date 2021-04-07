# -*- coding: utf-8 -*-
{
    'name': "oct_clean_html",

    'summary': """ 
        Module to clean HTML""",

    'description': """
        Module that allows you to clean the HTML code only to leave the text, eliminate labels and their values in dirty data
    """,

    'author': "Marcos M. Martinez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing 
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': "1.0",

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/wz_load_excel.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}