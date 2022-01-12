import requests
url = 'http://127.0.0.1:8000/api/v1'
headers = {'Authorization': 'Token d173bb565c34e9ea9ab37b75b4d4fb23a3620c2f'}
r = requests.get(url, headers=headers)
print(r.text)