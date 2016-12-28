import boto3
import os
import requests
from base64 import b64decode
 
 
ENCRYPTED = os.environ['test']
# Decrypt code should run once and variables stored outside of the function
# handler so that these are decrypted once per container
DECRYPTED = boto3.client('kms').decrypt(CiphertextBlob=b64decode(ENCRYPTED))['Plaintext']
encryptedweb = os.environ['webhook']
web = boto3.client('kms').decrypt(CiphertextBlob=b64decode(encryptedweb))['Plaintext']
 
def lambda_handler(event, context):
    # TODO handle the event here
    print(web)
    data = {"channel": "#general", "username": "webhookbot", "text":"hello hamed"}
    response = requests.post(web, json=data)
    print response.status_code
    return (DECRYPTED)
