# -*- coding: utf-8 -*-
{
    'name': "documentarywatchodoo",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Delphine Lemire",
    'website': "https://www.delphinelemire.fr",
    'license': "AGPL-3", 
    'installable': True,
    'application': True,
    
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Social Network',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 
                'mail',
                'crm',
               ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/themes.xml',
        'views/contributions.xml',
        'views/res_partner_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
}
