# import requests

# response = requests.get('https://logotypes.dev/random/data')

# response = response.json()

# print(response['logo'])

import requests
import json
def analyze(text_to_analyze):
    url = 'http://api.text2data.com/v3/analyze'
    payload = {
        'DocumentText': f'{text_to_analyze}', 
        'IsTwitterContent': 'false',
        'PrivateKey': 'B8989D21-BC3D-4EE2-B648-4C07294BB8F6', #add your private key here (you can find it in the admin panel once you sign-up)
        'Secret':'123', #this should be set-up in admin panel as well
        'RequestIdentifier': '' #optional, used for reporting context
    }
    
    r = requests.post(url, data=payload)
    data=r.json()
 



while True:
    menu = input("1 - logotypes, 2 - cat facts, 0 - exit: ")
    match menu:
        case "1":
            response = requests.get('https://logotypes.dev/random/data')
            response = response.json()
            if response['example_description']:
                print(response['example_description'])
                print(analyze(response['example_description']))
        case "2":
            response = requests.get('https://meowfacts.herokuapp.com')
            response = response.json()
            if response['data']:
                print(response['data'])
                print(analyze(response['data']))
        case '0':
            break
        case _:
            print('Try again')
    


