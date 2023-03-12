import requests
import json

url = 'https://63fc6ba18ef914c5559711c6.mockapi.io/users/'



file_json = open('datatugas.json','r')
payload = json.loads(file_json.read())
for data in payload:
    resp = requests.post(url, json=data)
    response= json.loads(resp.text)
    print(response)
