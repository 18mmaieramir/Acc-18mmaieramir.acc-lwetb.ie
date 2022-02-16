#1
l=[5,1,3,2,4]

g=list.sort(l)
print(l[4])


#2
m=[6,7,8,9]

list.reverse(m)
print(m)


#3


#4
z=m[1::2]
print(z)

#5
s=sum(m)
print(s)

#6


def Palindrome(s):
    return s == s[::-1]



s = "noon"
ans = Palindrome(s)

if ans:
    print("Yes")
else:
    print("No")

#7
#for loop
def add(b):
        c=0
        
        for  i in b:
            
            c = c+i

        return(c)
        
        
        
        
       



 
d=[1,2,3,4,5]
    
print(add(d))


#while loop
def func(a):
    v=0
    total = 0
    s = len(j)
    while v < s:
        total = total+a[v]
        v=v+1
    return(total)

j = [1,2,3,4,5]
print(func(j))


#recursion
Q=[1,2,3,4,5,6,7]

def factorial(L):
    if (len(L)==1):
        return L[0]
    else:
        return L[0] + factorial(L[1:])
    
    
print(factorial(Q))

#8
def perfect_squares():
    n=float(input("enter n"))
    for i in n:
        k=n*n


print(perfect_squares())       
    
        

    
    
    
    
    







