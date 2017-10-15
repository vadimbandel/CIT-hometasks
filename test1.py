import requests as re
import json


headers = {'content-type': 'application/json'}
url = 'https://cit-home1.herokuapp.com/api/register'

data = {"eventType": "Some Action by Kurafeeva"}

r = re.post(url, data=json.dumps(data), headers=headers)
print(r)

r = re.get('https://cit-home1.herokuapp.com/api/check_me')
print(r.json())
print()