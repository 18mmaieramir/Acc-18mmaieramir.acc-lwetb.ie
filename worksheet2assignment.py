#1

num1 = float(input("enter a number: "))
num2 = float(input("enter another number: "))

if (num1 > num2) and (num2 < num1):largest = num1
   
elif (num2 > num1) and (num1 < num2): largest = num2
   
    
print("largest number is",largest)

#2

age = int(input("enter your age"))
underage = int(17)
            
if (age > underage) and (underage < age): sub = "can"
    
elif (underage > age) and (age < underage): sub = "cannot"     
      
print("you",sub,"vote")

#3

num = float(input("enter a number"))
 
if (num % 2): print("your number is odd")

else: print("your number is even")

#4

num = float(input("enter a number"))
 
if (num % 7): print("your number is not divisble by 7")

else: print("your number is divisible by 7")

#5

num = float(input("enter a number"))
 
if (num % 5): print("your number is not a multiple of 5")

else: print("your number is a multiple of 5")

#6

units100 = float(input("enter the first hundred units"))
units100next = float(input("enter the next hundred units"))
units200 = float(input("enter the last 200 units"))

totalunitsfirst200 = float(units100next * 5)
totalunitslast200 = float(units200 * 10)
totalunits = float(totalunitsfirst200 + units200)
amount = float(totalunitslast200 + totalunits)

print(amount,"cents is the price")

#7

numb = float(input("enter a number"))
finalnumb = float(numb % 10)
print("the last digit of your number is",finalnumb)

#8

no_ = float(input("enter a number"))
finalno_ = float(no_ % 10)

if (finalno_ % 2): print("your numbers final digit is divisible by 3")

else: print("your numbers final digit is not divisible by 3")

#9

inputnumb = float(input("enter a number between one to seven"))

if (inputnumb == 1 ): print("one is equal to monday")

elif (inputnumb == 2 ): print ("two is equal to tuesday")

elif (inputnumb == 3 ): print ("three is equal to wednesday")
                  
elif (inputnumb == 4 ): print ("four is equal to thursday")
                 
elif (inputnumb == 5 ): print ("five is equal to friday")

elif (inputnumb == 6 ): print ("six is equal to saturday")
                  
elif (inputnumb == 7 ): print ("seven is equal to sunday")                  

#10

inputtemp = float(input("enter the temperature in degrees centigrade"))

f = (inputtemp * 9/5)  + 32 

f2 ="{:.2f}".format(f)

print("the temperature in fahrenheit is",f2)

#11
#?

                  


          
