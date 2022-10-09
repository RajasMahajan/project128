import math 
import csv

data = []
with open('archive_dataset.csv','r') as f:
    r = csv.reader(f)
    for row in r:
        data.append(row)

headers = data[0]
planetdata = data[1:]

for pd in planetdata:
    pd[2] = pd[2].lower()

planetdata.sort(key=lambda planetdata:planetdata[2])    

with open('archive_dataset_sorted.csv','a+') as f:
    a = csv.writer(f)
    a.writerow(headers)
    a.writerows(planetdata)

with open('archive_dataset_sorted.csv')as input, open ('archive_dataset_sorted1.csv','w',newline='') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(i.strip() for i in row):
            writer.writerow(row)








