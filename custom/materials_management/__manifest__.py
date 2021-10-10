# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'MGX',
    'version' : '1.0',
    'author': 'HARHAD Selmane',
    'summary': 'Invoices & Payments',
    'sequence': 10,
    'description': """ Materials managment  """,
    'category': 'Inventory/Materials',
    'website': 'https://www.odoo.com/page/billing',
    'images' : [],
    'web_icon' :['/home/user/Odoo14/custom/materials_management/static/description/icon.png'],
    'depends' : ['purchase','product'],
    'data': [
        'security/mgx_security.xml',
        'security/ir.model.access.csv',
        'views/mgx_menu.xml',
        'views/demand.xml',
        'views/article.xml',
        'views/employeeMGX.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
