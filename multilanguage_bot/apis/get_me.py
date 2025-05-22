import requests
import json

from multilanguage_bot.app import TOKEN

res = requests.get(f'https://api.telegram.org/bot{TOKEN}/getMe')
res_json = json.loads(res.text)

if __name__ == '__main__':
    print(res_json)
