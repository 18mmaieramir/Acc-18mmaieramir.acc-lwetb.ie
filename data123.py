import csv
file=open("data.csv", "w", newline= "")
 
string1 = ["title,First Name, Surname,Address,City,Postcode,Telephone"]
string2 = ["Mr,Tom,smith,42 Mill Street,London,WE13GW,10344044"]
string3 = ["Mrs,Sandra,Jones,10 Low Lane,Hull,HU237HJ,22344033"]
string4 = ["Mr,John,Jacob,8 Sherlock Court,Cambridge,CB30JB,55007788"]

db = csv.writer(file)
db.writerow(string1)
db.writerow(string2)
db.writerow(string3)
db.writerow(string4)

file.close()


#part2
f1=open("data.csv" , "r")
data = list(csv.reader(f1))
print(data)
f1.close()
for i in data:
    print(i[6])

