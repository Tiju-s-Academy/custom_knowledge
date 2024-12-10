{
    'name': 'Knowledge',
    'version': '17.0.0.0',
    'author': "Tiju's Academy",
    'category': 'Knowledge Management',
    'summary': 'Custom module for storing and organizing knowledge articles',
    'description': 'A custom knowledge management.',
    'depends': ['base', 'hr', 'web', 'web_editor'],
    'data': [
        'security/knowledge_groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rule_collabraters.xml',
        'views/knowledge_article_view.xml',
        'views/knowledge_tag_view.xml',
        'views/knowledge_menu.xml',
        'wizard/knowledge_wizard.xml',
        'wizard/knowledge_video_wizard.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'custom_knowledge/static/src/js/video.js',
            # 'custom_knowledge/static/src/js/document.js'
        ],
        'web.assets_frontend': [
            'custom_knowledge/static/src/xml/video.xml'
        ]
    },
    'application': True,
    'license': 'LGPL-3'
}
