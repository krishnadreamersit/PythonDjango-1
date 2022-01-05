# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def get_all():
    url = 'http://127.0.0.1:8000/customers/'
    response = requests.get(url)
    if response.status_code==200:
        customers = response.json()
        for customer in customers:
            print(customer)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    get_all()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
