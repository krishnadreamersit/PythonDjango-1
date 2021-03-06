# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests

URL = 'http://127.0.0.1:8000/customers/'

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def get_all():
    response = requests.get(URL)
    if response.status_code==200:
        customers = response.json()
        for customer in customers:
            print(customer)

def get(id): # search customer based on id
    response = requests.get(URL + str(id))
    print(response.status_code)
    if response.status_code==200:
        print(response.json())
    else:
        print("Record not found!")

def post(record):
    response = requests.post(URL, record)
    print(response.status_code)
    if response.status_code==201:
        print("Insert record successfully")
    else:
        print("Error to insert record")

def put(record):
    response = requests.put(URL + str(record.get('id')) + '/', record)
    print(response.status_code)
    if(response.status_code==200):
        print("Record update successfully")
    else:
        print("Error to update record")

def delete(id):
    response = requests.delete(URL + str(id) + '/')
    print(response.status_code)
    if(response.status_code==204):
        print("Record delete successfully")
    else:
        print("Error to delete record")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    get_all()
    # get(1)
    # post({'fullname': 'Om', 'address': 'BHK'}) # insert record
    # put({'id': 1, 'fullname': 'Krishna Aryal', 'address': 'Kathmandu'}) # update/edit record
    # delete(4)
    # Research
        # patch()
        # Acquire balance amount/transfer of esewa/khalti wallet
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# 3rd Party API Call

# Example-1
URL = 'http://127.0.0.1:8000/customers/'
headers = {'Authorization': 'Token 749ddd5b6b256a39a1370ac68c360cf5c69b73e5'}
response = requests.get(URL, headers=headers)
if response.status_code==200:
    customers = response.json()
    for customer in customers:
        print(customer)

