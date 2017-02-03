import requests
import json

url = ''
sensor = ''
username = ''
hash = ''

link = (url + sensor + "&username=" + username + "&passhash=" + hash)
#print(link)
ops = requests.get(link, verify=False)
api = json.loads(ops.text)


#### troubleshooting
#for key in api:
#    print(key)


data = api['sensordata']

#### troubleshooting
#for key, value in dist.items():
#    print("\nKey:" + key)
#    print("Value:" + value)


print("This came from the " + data['info'])

print('\n\n')
