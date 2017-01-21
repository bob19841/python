import csv
import os
import smtplib

path="."
function_miss = 0
owner_miss = 0

def send_email():
    ### read prtg_api_notifications-v3.py
    filename = 'Output.txt'
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
    msg = "Subject: Server Inventory that needs updating\n" + newest + '\n' + str1

    # Credentials (if needed)
    username = ''
    password = ''

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

dated_files = [(os.path.getmtime(fn), os.path.basename(fn))
               for fn in os.listdir(path) if fn.lower().endswith('.csv')]
dated_files.sort()
dated_files.reverse()
newest = dated_files[0][1]

### parse
text_file = open("Output.txt", "w")
invfile = open(newest)
data = csv.reader(invfile)
for row in data:
    if row[2] == "":
        #print(row[0] + "is missing its function")
        function_miss += 1
        text_file.write(row[0] + "is missing its function\n")
    if row[3] == "":
        #print(row[0] + "is missing its owner")
        owner_miss += 1
        text_file.write(row[0] + "is missing its owner\n")

text_file.close()

if function_miss == 0 and owner_miss == 0:
    print("all good")
if function_miss > 0 or owner_miss > 0:
    #print("we got work")
    send_email()

#print(function_miss)
#print(owner_miss) 



