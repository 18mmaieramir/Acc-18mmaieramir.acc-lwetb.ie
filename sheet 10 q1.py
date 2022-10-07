file = open("100Random.txt", "r")

#range
highest = 0
lowest= 10

for line in file:
    for item in line.split():
        if int(item)  > highest:
            highest = int(item)
             
        if int(item)  < lowest:
            lowest = int(item)
           
            
range1 = print("range =" , highest - lowest)

file.close()
file = open("10Random.txt", "r")

#frequency
list2 = []

for line in file:
    for item in line.split():
        list2.append(int(item))
        
print(list2)
list1= list2.copy()
for item in list2:
    if list2.count(item) > 1:
        list2.remove(item)
        
print(list2)
list2.sort()
print(list2)
filefre = open("filefrequency.txt" , "w")
for item in list2:
     print("freguency = ",item , "Is" , list1.count(item))
     filefre.write("freguency = " + str(item) + "Is" + str(list1.count(item)) + "\n")


filefre.close()
    
file.close()
file = open("10Random.txt", "r")    
#mean
list3 = []
for line in file:
    for item in line.split():
        list3.append(int(item))
        
print(list3)

total = sum(list3)


total1 = len(list3)

mean = (total // total1)

print("mean =" , mean)


  
file2 = open("filerange.txt" , "w")
file2.write(str(highest - lowest))
file2.close()



fileme = open("filemean.txt" , "w")
fileme.write(str(mean))
fileme.close()

    
        
        

     
        
        
            
            
            



            

            
