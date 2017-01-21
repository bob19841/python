import xml.etree.ElementTree as ET
import requests
import smtplib

def send_email():
    ### read prtg_api_notifications-v3.py
    filename = 'prtgout.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
    for line in lines:
        line.rstrip()

    #print(lines)
    str1 = ''.join(lines)
    #print(str1)
    ### send email
    fromaddr = ''
    toaddrs = ''
    msg = "Subject: PRTG Notification settings that need Addressed\n"  + str1

    # Credentials (if needed)
    username = ''
    password = ''

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


### stage vaiables
user_name = ""
user_hash = ""
prtg_server = ""

message = ['****** This is the status of The PRTG Notifications ******\n']
paused_alerts = 0
active_alerts = 0


url = prtg_server + "/api/table.xml?content=notifications&columns=name,active&username=" + user_name + "&passhash=" + user_hash
response = requests.get(url, verify=False)
root = ET.fromstring(response.content)

#print('\n\n ****** This is the status of The PRTG Notifications ******')
for item in root.iter('item'):
    name = item.find('name')
    active = item.find('active')
    if active.text == "Paused":
        paused_alerts += 1
        line = ("The Notification Rule Called = " + name.text + " -- is currently set to = " + active.text)
        message.append(line)
        #print("The Notification Rule Called = " + name.text + " -- is currently set to = " + active.text)
    else:
        active_alerts += 1


#if paused_alerts != 0:
#    a = str(paused_alerts)
#    print("\nThere are this many paused alerts " + a)
#if active_alerts != 0:
#    b = str(active_alerts)
#    print("There are this many active alerts " + b)

thefile = open('prtgout.txt', 'w')
for item in message:
  thefile.write("%s\n" % item)
thefile.close()

if paused_alerts != 0:
    send_email() 
