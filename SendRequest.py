import requests
import json

url = 'http://cit-home1.herokuapp.com'
register = '/api/register'
check = '/api/check_me'

request = requests.post(url + register,
                        data=json.dumps({'name': 'Dmitrii', 'surname': 'Valiaev'}),
                        headers={'content-type': 'application/json'})
print(request.json()['answer'])

request = requests.get(url + check)
print(request.json())
