# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Website Development',
    'version': '1.1',
    'summary': 'Client Site',
    'sequence': 15,
    'description': """Client Site
    """,
    'category': 'Client',
    'website': 'https://www.odoo.com/page/billing',
    'images': [],
    'depends': ['base', 'web', 'website'],
    'data': [
        # 'security/security.xml',
        # 'security/ir.model.access.csv',
        'views/login_view.xml',
        'views/resources_assets.xml',
        # 'views/sign_up_view.xml',
        'views/sign_up_record.xml',

    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
