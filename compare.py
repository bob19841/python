import os

user_file = 'users.txt'
with open(user_file) as f:
    content = f.readlines()
# remove carriage return
content = [x.strip() for x in content]
content = [x.lower() for x in content]
print(content)

root = 'x:'

for subfolder in os.listdir(root):
    if subfolder.lower() not in content:
        new_line = 'This folder doesnt belong to an active citrix user "' + subfolder + '"'
        print('This folder doesnt belong to an active citrix user  "' + subfolder + '"')
 
