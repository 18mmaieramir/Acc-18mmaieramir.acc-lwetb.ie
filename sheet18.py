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

b=[1,2,3,4,5]
p=0

for  i in b:
    if i < b[:5]:
        c = i+p
        
        
print(c)
        
