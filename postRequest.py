import requests
import json

url = 'http://cit-home1.herokuapp.com/api/register'
payload = {'login': 'Alexandra','Password':'ercvtybnu'}
headers = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(payload),headers=headers)
print(r)

r=requests.get("http://cit-home1.herokuapp.com/api/headers")
print(r.content)
r=requests.get("http://cit-home1.herokuapp.com/api/check_me")
print(r.json())



