import csv
'''

Read a CSV file select a column and parse a value between an index position of three and the first comma for this one

'''

f = open('allnew.csv')
csv_f = csv.reader(f)
for row in csv_f:
    temp = row[13]                            ### Select Row 13 - Remember it starts at 0
    temp = temp[3:]                           ### Index in to the 4 character
    print(temp.split(',')[0])                 ### Split on the comma and select the fisrt one in the index

 
