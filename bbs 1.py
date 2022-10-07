def BubbleSort1(L):
    l= [5, 7, 3, 6, 2, 4, 1]
    print("INPUT (initial list): ", l)
    exchange = True
    

n = len(l)
i = 0

while (i< n) and exchange:
   print("BEFORE PASS %d: %s " %(i+1, l))
   exchange = False
   for j in range(n-i-1):
       print("%s " %l, end="-> ")
       if l[j] > l[j+1]:
           l[j], L[j+1] = l[j+1], l[j]
           exchange = True
           print("%s " %l)
print("AFTER PASS %d: %s " %(i+1, l))



