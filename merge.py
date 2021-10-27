import csv
data1=[]
data2=[]
with open("final.csv","r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        data1.append(i)

with open("dataset2.csv","r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        data2.append(i)

headers1=data1[0]
planet_data1=data1[1:]     

headers2=data2[0]
planet_data2=data2[1:]    
headers=headers1+headers2
planet_data=[]
for index,row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])
with open("dataset3.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)    