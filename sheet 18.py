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
    n=int(input("enter n"))
    wa=0
    for i in range(n<= n):
        n = n*n
    print(n)
    
    
perfect_squares()

#9
def comb():
    l1=[4,5,6]
    l2=[1,2,3]
    
    l3= l1+l2
    print(l3)
comb()

#10
def com():
    l1=[4,5,6]
    l2=[1,2,3]
    
    result = [None]*(len(l1)+len(l2))
    result[::2] = l1
    result[1::2] = l2
    
    print(result)
    
com()


#11
def s1():
    l3=[8,2,6,69]
    l4=[4,5,0,1]
    
    list.sort(l3)
    list.sort(l4)
    l7=[]
    l7=l3+l4
    print(l7)
    list.sort(l7)
s1()    




    
    
    
    
    






