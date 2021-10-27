import csv 
data=[]
with open("dataset(1).csv","r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        data.append(i)
headers=data[0]
planet_data=data[1:]
for i in planet_data:
    i[2]=i[2].lower()
planet_data.sort(key=lambda planet_data:planet_data[2])
with open("dataset2.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)