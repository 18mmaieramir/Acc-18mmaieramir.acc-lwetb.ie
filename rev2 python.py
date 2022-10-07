#1
x1= float(input("Enter first value"))
x2= float(input("Enter secondary value"))

s= x1+x2
s = round(s,2)
print("sum =",s)

d= x1-x2
d = round(d,2)
print("difference =",d)

m= x1*x2
m = round(m,2)
print("product =",m)

#2
d5= float(input("Enter 5 digit number"))

ms= d5 / 60
print(round(ms))

#3
v1= str(input("Enter first value"))
v2= str(input("Enter first value"))
v3= str(input("Enter first value"))
v4= str(input("Enter first value"))
v5= str(input("Enter first value"))

print(ord(v1))
print(ord(v2))
print(ord(v3))
print(ord(v4))
print(ord(v5))



#4
r = int(input("enter value"))
counter = 0
total = 0
while r > 0:
    total = total +r
    counter = counter+1
    
    r = int(input("enter value"))
  

    avg = total / counter

   
print(avg)

#5

v1= int(input("Enter first value"))
v2= int(input("Enter second value"))
v3= int(input("Enter third value"))
v4= int(input("Enter fourth value"))
v5= int(input("Enter fifth value"))

l1 = []
l2 = []

l1.append(v1)
l1.append(v2)
l1.append(v3)
l1.append(v4)
l1.append(v5)

print(l1)

for i in l1:
    i=i +1
    l2.append(i)
    
    
    
print(l2)

