# -*- coding: utf-8 -*-

# Created on 2023-02-016
# author: 欧度智能，https://www.odooai.cn
# email: 300883@qq.com
# resource of odooai
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Copyright (c) 2020-Present InTechual Solutions. (<https://intechualsolutions.com/>)

{
    'name': 'ChatGPT4,Google Bard, AiGC Center.Ai服务中心，聚合全网Ai',
    'version': '15.23.07.29',
    'author': 'odooai.cn',
    'company': 'odooai.cn',
    'maintainer': 'odooai.cn',
    'category': 'Website/Website',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 10,
    'images': ['static/description/banner.gif'],
    'summary': '''
    ChatGpt Odoo AI Center. Multi Ai aigc support with Google Bard Ai, Azure Ai, Baidu Ai,etc..
    Support chatgpt 4 32k image. DALLE, Integration All ChatGpt Api and Azure OpenAI.
    Easy Chat channel with several ChatGPT Robots and train.
    ''',
    'description': '''
    Allows the application to leverage the capabilities of the GPT language model to generate human-like responses,
    providing a more natural and intuitive user experience.
    Base on is_chatgpt_integration from InTechual Solutions.
    1. Multi ChatGpt openAI robot Connector. Chat and train.
    2. Multi Ai support including Google Bard Ai, Azure Ai, Chatgpt 4, Chatgpt 3.5 Turbo, Chatgpt 3 Davinci, Chatgpt 2 Code Optimized, 'Dall-E Image.
    3. Bind ChatGpt Api to user. So we can chat to robot user or use ChatGpt Channel for Group Chat.
    4. White and black List for ChatGpt.
    5. Setup Demo Chat time for every new user.
    6. Easy Start and Stop ChatGpt.
    7. Evaluation the ai robot to make better response. This training.
    8. Add api support Connect the Microsoft Azure OpenAI Service.
    9. Can set Synchronous or Asynchronous mode for Ai response.
    10.Filter Sensitive Words Setup.
    11. Multi-language Support. Multi-Company Support.
    12. Support Odoo 16,15,14,13,12, Enterprise and Community and odoo.sh Edition.
    13. Full Open Source.
    ''',
    'depends': [
        'base',
        'app_common',
        'base_setup',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_channel_data.xml',
        'data/ai_robot_data.xml',
        'data/user_partner_data.xml',
        'data/ir_config_parameter.xml',
        'views/res_config_settings_views.xml',
        'views/ai_robot_views.xml',
        'views/res_users_views.xml',
    ],
    'assets': {
        'mail.assets_messaging': [
            'app_chatgpt/static/src/models/*.js',
        ],
        'mail.assets_model_data': [
            'app_chatgpt/static/src/models_data/*.js',
        ],
    },
    'external_dependencies': {'python': ['openai']},
    'installable': True,
    'application': True,
    'auto_install': False,
}