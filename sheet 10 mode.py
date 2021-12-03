#mode
file = open("10Random.txt", "r")
list4 = []

for line in file:
    for item in line.split():
        list4.append(int(item))
        
print(list4)
list4= list4.copy()
for item in list4:
   if list4.count(item) > 1:
       print("mean is " , item)
      
