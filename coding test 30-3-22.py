
import math

#1
x = 4.20

y= 1.69

avg = x+y
avg1 = avg/2
print("average", avg1)

avg2 = x%y
print("remainder x/y =" ,avg2)

avg3 = y%x
print("remainder y/x =" , avg3)

print("power",pow(x,y))

#2
r = int(input("enter radius"))
h = int(input("enter height"))

def volume(r,h):
    
    vol=math.pi*r*r*h
    return vol
    
print(volume(r,h))

#3
str1 = str(input("enter first string"))
str2 = str(input("enter second string"))


def str_comp(str1,str2):
    return str1==str2
        
        
print(str_comp(str1,str2))
        
        
#4

num = int(input("enter number"))

for i in range (1 , num):
    if i % 2 == 1: 
        print(i)
    
    
#5

f1 = open("readme.txt" , "r")
v="aeiouAEIOU"
k=" "
for i in f1.readlines():
    for m in i:
        if m in v:
            k += m
            
print(k)            
    
    
  
    
    
    
#6
numb =  float(input("enter number"))

def recursive(n):
    if n == 0:
        return 0
    else:
        return n + recursive(n-1)

print(recursive(num))

    
    
 
