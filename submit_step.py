import requests
import random
import os

url = 'https://gg.ibushu.com/ibushu/api/submitZepp'

MIN_STEP = os.environ.get('MIN_STEP')
MAX_STEP = os.environ.get('MAX_STEP')

data = {
    'zeppAccount': os.environ.get('ZEPP_ACCOUNT'),
    'zeppPassword': os.environ.get('ZEPP_PASSWORD'),
    'step': random.randint(int(MIN_STEP), int(MAX_STEP)),
}

resp = requests.post(url=url, data=data)
print(resp.text)
