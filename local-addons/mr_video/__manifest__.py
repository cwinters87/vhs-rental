# -*- coding: utf-8 -*-
{
    'name': "Mr Video",  # Module title
    'summary': "Every Reason to Stay Home Tonight",  # Module subtitle phrase
    'description': """Rent todays hottest movies using the lastest technology of VHS""",  # You can also rst format
    'author': "Chris Winters",
    'website': "https://www.facebook.com/mrvideosa/",
    'category': 'Uncategorized',
    'version': '12.0.1',
    'depends': ['base'],
    # This data files will be loaded at the installation (commented becaues file is not added in this example)
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml'
    ],
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}