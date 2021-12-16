file = open("MaierChristmasTest2021.txt" , "w")


#1
list11 = [23,1,0,-12,48]
sum = sum(list11)
print(sum)

file.write(str(sum))
 


#2


list3 = [23,1,0,-12,48]

sum = 0
for line in list3:
    if line % 2!=0:
        sum = sum+line
    
   
print(sum)

file.write(str(sum))

#3

list3 = [23,1,0,-12,48]

prod = 1
for line in list3:
    if line % 2==0:
        prod = prod*line
    
   
print(prod)

file.write(str(prod))


#4


list3 = [23,1,0,-12,48]

product = 1
for line in list3:
     product = product*line
    
   
print(product)

file.write(str(product))


#5
for no in range(0,22,2):
    print(no)

file.write(str(no))


#6


string1 = (input("enter a sentence"))

while(
    



