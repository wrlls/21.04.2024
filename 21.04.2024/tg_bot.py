import requests
import pprint

token = '7034065280:AAF3jmtTIBhQSRMlLFC7ivse2-0ezn8RzY4'
main_url = f'https://api.telegram.org/bot{token}'
url = f'{main_url}/getUpdates'
result = requests.get(url)
pprint.pprint(result.json())
messages = result.json()['result']
for message in messages:
    chat_id = message['message']['chat']['id']
    url = f'{main_url}/sendMessage'
    params = {'chat_id': chat_id, 'text': "Привет, дорогой юзер"}
    result = requests.post(url, params=params)
