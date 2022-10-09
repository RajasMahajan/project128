import csv

finalone = []
datasortone = []

with open('final.csv','r') as f:
    readone = csv.reader(f)
    for row in readone:
        finalone.append(row)

        
with open('archive_dataset_sorted1.csv','r') as f:
    r = csv.reader(f)
    for row in r:
        datasortone.append(row)
headerone = finalone[0]
planetone = finalone[1:]
header2 = datasortone[0]
planet2 = datasortone[1:]


header =headerone + header2
planetdata = []

for index, row in enumerate(planetone):
    planetdata.append(planetone[index]+planet2[index]) 

with open('mergeddataset.csv','a+') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(planetdata)



with open('mergeddataset.csv')as input, open ('mergeddata1.csv','w',newline='') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(i.strip() for i in row):
            writer.writerow(row)


    