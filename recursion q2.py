Q=1234567

def factorial(Q):
  
    
    if (Q < 10):
        return Q
    else:
        return Q%10 + factorial(Q//10)
    
    
print(factorial(Q))