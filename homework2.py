import requests
import json

reg='https://cit-home1.herokuapp.com/api/register'
ch='https://cit-home1.herokuapp.com/api/check_me'
txt = json.dumps({'first name': 'Sofia','last name':'Smolyaninova'})
head={'content-type': 'application/json'}

p = requests.post(reg, data=txt, headers=head)
print(p)
gch=requests.get(ch)
print(gch.json())