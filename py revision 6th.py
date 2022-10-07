#1
compnum = 50
counter = 0






no= int(input("guess a number"))


while no != compnum:
    if no > compnum:
        print("Try Again, number is too high")
        counter= counter + 1
        no= int(input("guess a number"))
        
    if no < compnum:
        print("Try Again, number is too low")
        counter = counter +1
        no= int(input("guess a number"))
    if no == compnum:
        print("Well done, You took", counter, "tries")
        break


#2
r = float(input("enter radius of cylinder"))
d = float(input("enter depth of cylinder"))

v= (3.141)(r^2)(d)
print(v)


    