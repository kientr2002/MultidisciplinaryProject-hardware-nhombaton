import requests
url='https://api.ipify.org/'
headers=''
data = {'key1': 'value1', 'key2': 'value2'}
data = {'key1': 'value1', 'key2': 'value2'}
r=requests.post(url=url,headers=headers)
status = r.json

print(status)
