import requests
import pprint

token='8314670c08d7a09936bb354af2a35f76d68c349d'
headers= {'Authorization': f'Token {token}'}
response=requests.get('http://127.0.0.1:8000/api/v0/tags/', headers=headers)
pprint.pprint(response.json())