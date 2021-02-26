import json
import requests

def fetch(api_url):
    response = requests.get(api_url)
    print(response)
    response = json.loads(response.text)
    return response


api_url = 'https://zenquotes.io/api/random'
response = fetch(api_url)

quote = response[0]['q']
author = response[0]['a']

msg = f'{quote} -{author}'
print(msg)