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
     mode1 = print("mode is " , item)
       
file3 = open("filemode.txt" , "w")
file3.write(str(item))
file3.close()

      
