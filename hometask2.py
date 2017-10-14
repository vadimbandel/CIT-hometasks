import requests
import json

# посмотрели дз
print(requests.get('https://cit-home1.herokuapp.com/api/help').text)
# сериализуем obj в строку JSON-формата
# indent-уровень отступа
json_txt = json.dumps({'Branch': 'ALECIO', 'Registration': 'Yes'}, indent=3)
# регистрация
r = requests.post('https://cit-home1.herokuapp.com/api/register', json_txt, headers={'Content-type': "application/json"})
# смотрим АШШШШИБК!!! или извещение об успехе
print(r.json())
# Выполнена ли регистрация?
print('\n', requests.get('https://cit-home1.herokuapp.com/api/check_me').json())