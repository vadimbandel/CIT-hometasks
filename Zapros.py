import requests
import json
data = {'event':'Python'}
url = 'http://cit-home1.herokuapp.com/api/register'
headers = {'content-type':'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.json()['answer'])
r = requests.get('https://cit-home1.herokuapp.com/api/check_me')
print(r.json())
