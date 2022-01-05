import json
import requests
import sys
def get_all():
    try:
        response = requests.get('https://api.instantwebtools.net/v1/airlines')
        # print(response.status_code)
        if response.status_code==200:
            resords = response.json()
            for record in resords:
                print(record)
    except:
        print("Error : ", sys.exc_info()[1])

def get(id):
    try:
        response = requests.get('https://api.instantwebtools.net/v1/airlines/'+str(id))
        # print(response.status_code)
        if response.status_code == 200:
            record = response.json()
            print(record)
    except:
        print("Error : ", sys.exc_info()[1])

def post(record):
    try:
        response = requests.post('https://api.instantwebtools.net/v1/airlines', json=record)
        # print(response.status_code)
        if response.status_code == 200:
           print("record insert successfully")
    except:
        print("Error : ", sys.exc_info()[1])

def put(record):
    try:
        url = 'https://api.instantwebtools.net/v1/airlines'
        response = requests.put(url+str(record['id']), json=record)
        # print(response.status_code)
        if response.status_code == 200:
           print("record insert succesurlsfully")
    except:
        print("Error : ", sys.exc_info()[1])

# Test
# get_all()
# get(353745)
record = {'id': 353745, 'name': 'Quatar Airways', 'country': 'Quatar', 'logo': 'https://upload.wikimedia.org/wikipedia/en/thumb/9/9b/Qatar_Airways_Logo.svg/300px-Qatar_Airways_Logo.svg.png', 'slogan': 'Going Places Together', 'head_quaters': 'Qatar Airways Towers, Doha, Qatar', 'website': 'www.qatarairways.com', 'established': '1994'}
post(record)