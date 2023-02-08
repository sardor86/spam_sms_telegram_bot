import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ['TOKEN']


PROXY = {
        "http": "http://222.74.202.242:8081",
        "http": "http://185.38.111.1:8080",
        "http": "http://222.74.202.244:8080",
        "http": "http://51.75.160.183:8080",
    }

SITE_LIST = [
        {
                'url': 'https://express24.uz/rest/v2/auth/code',
                'plus_in_number': True,
                'params_for_number': 'number'
        },
        {
                'url': 'https://api.yaponamama.uz/v1/register-code',
                'plus_in_number': False,
                'params_for_number': 'phone'
        },
        {
                'url': 'https://io.bellissimo.uz/api/verify',
                'plus_in_number': True,
                'params_for_number': 'phone'
        },
        {
                'url': 'https://api.bringo.uz/api/v1/register/phone',
                'plus_in_number': False,
                'params_for_number': 'phone'
        },
        {
                'url': 'https://api.brandstore.uz/api/auth/code/create',
                'plus_in_number': False,
                'params_for_number': 'phone'
        },
        {
                'url': 'https://bulavka.uz/api/userservice/phonee',
                'plus_in_number': True,
                'params_for_number': 'phone'
        },
        {
                'url': 'https://discord.com/api/v9/auth/forgot',
                'plus_in_number': True,
                'params_for_number': 'number'
        }
]
