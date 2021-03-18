# -*- coding: utf-8 -*-
{
    'name': "oct_clean_excel",

    'summary': """
        Module to clean data""",

    'description': """
        Module that allows you to clean the data from the product variants before being imported into ODOO
    """,

    'author': "Marcos M. Martinez",
    'website': "https://octupus.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

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
