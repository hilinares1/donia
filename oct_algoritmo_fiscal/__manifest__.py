# -*- coding: utf-8 -*-

{
    'name': "oct_algoritmo_fiscal",

    'summary': """
        Module for generate Trimestral account for POS
        """,

    'description': """
        Module for generate Trimestral account for POS
    """,

    'author': "Octupus Technologies SL",
    'website': "https://www.octupus.es",

    'category': 'productivity',
    'version': '0.1',

    'depends': ['base', 'point_of_sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'wizard/wizard_view_form.xml',
        #'data/sequence.xml',
    ],
    'installable': True,
    'application': False,
}
