import requests
import json

json_data = {'content-type':'application/json'}
url = 'https://cit-home1.herokuapp.com/api/register'
r = requests.post(url,{},json.dumps(json_data))
print(r.json()['answer']) 
r = requests.get('https://cit-home1.herokuapp.com/api/check_me')
print(r.json())
