'''
Created on Dec 26, 2016

@author: root
'''
import requests
data = {"channel": "#general", "username": "webhookbot", "text":"hello hamed"}
response = requests.post('webhook', json=data)
print response.status_code
