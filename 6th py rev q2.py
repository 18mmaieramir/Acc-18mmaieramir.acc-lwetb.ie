#2
r = float(input("enter radius of cylinder"))
d = float(input("enter depth of cylinder"))

r1 =r**2
r2 = 3.141*r1
v = r2*d

print(round(v,3))



a = float(input("1. Square, 2. Triangle, Enter a number: "))
         
if a == 1:
    l = float(input("Enter Length"))
    print(l**2)
    
if a == 2:
    b = float(input("Enter base Length"))
    h = float(input("Enter height"))
    print(h*b/2)
    
if a != 1 or 2:
    print("Choose either 1 or 2.")
                 

