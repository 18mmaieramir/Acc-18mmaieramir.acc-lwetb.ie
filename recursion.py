Q=[1,2,3,4,5,6,7]

def factorial(L):
    if (len(L)==1):
        return L[0]
    else:
        return L[0] + factorial(L[1:])
    
    
print(factorial(Q))