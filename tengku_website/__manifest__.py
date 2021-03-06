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
    'depends': ['base', 'web', 'website', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/login_view.xml',
        'views/resources_assets.xml',
        # 'views/sign_up_view.xml',
        'views/sign_up_record.xml',
        'views/registration_form.xml',
        'views/thank_you_page1.xml',
        'views/thank_you_page2.xml',
        'views/account_page.xml',
        'views/tengku_partner.xml',
        'views/account_page2.xml',
        'views/res_city_view.xml',
        'views/multiple_selection.xml',
        'views/merchant_signup.xml',
        'views/merchant_account1.xml',
        'views/merchant_account_page2.xml',
        'views/merchant_thank_you.xml',


    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
