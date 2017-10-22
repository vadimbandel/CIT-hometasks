import requests
import json

request = requests.post("http://cit-home1.herokuapp.com/api/register",
                        data = json.dumps({'message':'Registration process...'}),
                        headers = {'content-type': 'application/json'})

if request.status_code == 200:
    request = requests.get("http://cit-home1.herokuapp.com/api/check_me")
    print(request.json())