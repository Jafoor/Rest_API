import requests
import json
URL = "http://127.0.0.1:8000/stuinfo/"

def get_data(id = None):
    data = {}
    headers = {'content-Type': 'application/json'}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url = URL,headers = headers, data = json_data)
    data = r.json()

    print(data)

# get_data()

URL1 = ""
def post_data():
    data = {
        'name': 'Raviii',
        'roll': 170133,
        'city': 'dhakaa'
    }
    headers = {'content-Type': 'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# post_data()

def update_data():
    data = {
        'id': 100,
        'name': 'Javvi',
        'city': 'Ctg'
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL,headers = headers, data=json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data = {
        'id': 11
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url = URL,headers = headers, data=json_data)
    data = r.json()
    print(data)
delete_data()