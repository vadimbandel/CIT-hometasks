import requests as rq


def help():
    response=rq.get("https://cit-home1.herokuapp.com/api/help")
    print(response.content.decode("utf-8"))

def check_me():
    response=rq.get("https://cit-home1.herokuapp.com/api/check_me")
    print(response.json())

def headers():
    response=rq.get("https://cit-home1.herokuapp.com/api/headers")
    print(response.content)

def register():
    str="test text"
    response=rq.post("https://cit-home1.herokuapp.com/api/register", json=str)
    print(response.content)

check_me()