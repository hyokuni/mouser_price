import requests
import json

#need post/json type
headers = {"Content-Type":"application/json"}
MouserSearchURL = 'https://api.mouser.com/api/v1/search/keyword'
payload = {'SearchByKeywordRequest': {'keyword': 'STM32G071','records': 0,'startingRecord': 0,'searchOptions': 'string','searchWithYourSignUpLanguage': 'string'}}

#read personal apiKey
f = open("apiKey.txt",'r')
apiKey = f.readline()

if not apiKey:
    print('key is empty')

else:

    FullAddressURL = MouserSearchURL+'?apiKey='+Mouser_apiKey
    r = requests.post(FullAddressURL, headers = headers, data=json.dumps(payload))

    print(r.status_code)

    #print('## raw receive data ##')
    #print(r.text)

    #need load
    parsed = json.loads(r.text)
    print(json.dumps(parsed,indent=4, sort_keys=True))
    #print(r.text)
