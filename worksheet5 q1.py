#1
import math
import random

num1 = int(input("enter a number"))
num2 = int(input("enter another number"))

lower = num1
upper = num2

minNumberGuesses = round(math.log(upper - lower + 1, 2))

randomChoice = random.randint(lower, upper)
print("you have",round(math.log(upper - lower + 1, 2)),"guesses") 

x = 0

while  (x < minNumberGuesses):
    x += 1
    
    guess = int(input("guess the number"))

if (guess == randomChoice):
    print("correct")
    
elif (guess < randomChoice):
    print("number is too low")
    
    
elif (guess > randomChoice):
    print("number is too high")


    
    

















             
             