import requests as re
import json

url = 'http://cit-home1.herokuapp.com/api/register'
headers = {'content-type': 'application/json'}
data = {'student': 'marshk'}

r=re.post(url, data=json.dumps(data), headers=headers)

r=re.get('http://cit-home1.herokuapp.com/api/check_me')
print(r.json())