# -*- coding: utf-8 -*-
{
    'name' : 'Owl Tutorial',
    'version' : '1.0',
    'summary': 'OWL Tutorial',
    'sequence': -1,
    'description': """OWL Tutorial Custom Dashboard""",
    'category': 'OWL',
    'depends' : ['base', 'web', 'sale', 'board'],
    'data': [
        'views/sales_dashboard.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'owl/static/src/components/**/*.js',
            'owl/static/src/components/**/*.xml',
            'owl/static/src/components/**/*.scss',
        ],
    },
}