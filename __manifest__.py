# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.





{
    'name': "Practical",
    'version': '16.0.1.0.0',
    'summary': 'Practical Software',
    'author': 'Ramiz Belim',
    'description': """Practical""",
    'depends': ['sale_management', 'crm', 'purchase'],
    'data': [
        'security/ir.model.access.csv',

        'views/crm_lead_views.xml',
        'views/crm_stage_views.xml',
        'views/vendor_type_views.xml',
        'views/res_partner_views.xml',
        'views/purchase_order_views.xml',
        'views/vendor_type_menus.xml',

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
