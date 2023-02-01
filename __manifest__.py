# -*- coding: utf-8 -*- 


{
    'name': 'Data correction log',
    'author': 'Soft-integration',
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1',
    'category': 'Technical tools',
    'demo': [],
    'depends': ['portal'],
    'data': [
        'security/data_correction_log_security.xml',
        'security/ir.model.access.csv',
        'views/data_update_views.xml'
    ],
    'license': 'LGPL-3',
}
