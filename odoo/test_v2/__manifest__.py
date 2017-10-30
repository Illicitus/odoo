# -*- coding: utf-8 -*-
{
    'name': "Test task",

    'summary': """
        Just test task""",

    'description': """
        - add tests
        - add test sessions
        - add form view res.partners
        - add active field is_tested
        - add filter to res.partners view 
    """,

    'author': "Honchar Vitalii",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test task',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}