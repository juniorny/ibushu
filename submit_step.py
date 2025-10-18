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

try_time = 0
while try_time < 10:
    try:
        resp = requests.post(url=url, data=data)
        print(resp.text)
        if "同步失败" in resp.text:
            raise ValueError("同步失败")
        elif "同步成功" in resp.text:
            print("同步成功")
            break
    except:
        try_time += 1
        print(f"同步失败，开始第{try_time}重试...")
        time.sleep(10)
