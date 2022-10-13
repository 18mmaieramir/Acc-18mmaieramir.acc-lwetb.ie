#1
Q=1234567

def factorial(Q):
  
    
    if (Q < 10):
        return Q
    else:
        return Q%10 + factorial(Q//10)
        
    
    
print(factorial(Q))
#2
n = int(input("number of terms"))

n1 = 0
n2 = 1

counter = 0

if n < 0:
    print("enter number > 0")
else:
    while counter < n:
        print(n1)
        
        n3 = n1 + n2
        
        n1 = n2
        n2 = n3
        counter += 1
    