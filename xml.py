import xml.etree.ElementTree as ET

tree = ET.parse('OK_getsensordetails.xml')
#tree = ET.parse(requests.get(url, stream=True, verify=False))
root = tree.getroot()

for child in root.iter('lastmessage'):
    message = child.text
for child in root.iter('parentdevicename'):
    device = child.text
#for child in root.iter('parentdeviceid'):
 #   pdevice = child.text


print(device.strip())
print(message.strip())
#print(pdevice.strip())

if message.strip() == 'OK':
    print("were good move on")
else:
    print("issues")

