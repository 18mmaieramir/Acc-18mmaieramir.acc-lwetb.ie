#bubble sort
def bs():

    def bbs(L):
        print("INPUT (initial list): ", L)
        exchange = True
        n = len(L)
        i = 0

        while (i < n) and  exchange:
            print("BEFORE PASS %d: %s " %(i+1, L))
            break
            
            
        
        exchange = False
        for j in range(n-i-1):
                print("%s " %L, end="-> ")
                if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
                    exchange = True
                    print("%s " %L)
        print("AFTER PASS %d: %s " %(i+1, L))

        i= i+1 # increment the loop counter
        print("OUTPUT (sorted list): ", L)



    Q= [5, 4 , 3, 6, 2, 4, 1]

    bbs(Q)
    
    
bs()
#insertion
def insert():
    l = [5, 7, 3, 6, 2]
    w = [1, 3, 4, 4, 6, 7]

    def insertion_sort(l):
        j = 0
    
        for i in range(len(l)):
            if i + 1 < len(l):
                if l[i] <= l[i + 1]:
                    j += 1
        if j == len(l) - 1:
            print("Already sorted")
            return l
           
    
        marker = 1

        while (marker < len(l)):
            j = marker
            while (l[j] < l[j - 1] and j > 0):
                print(l, marker)
                tmp = l[j]
                l[j] = l[j - 1]
                l[j - 1] = tmp
                j = j - 1
        
            marker += 1
        return l

    print(insertion_sort(w))
    
insert()


# Simple (Selection) Sort

def ss(aList):
    
    

    marker = 0

    while marker < len(aList):
         
        index_of_min = marker
        for j in range(marker+1, len(aList)):
            if aList[index_of_min] > aList[j]:
                
                index_of_min = j
                
        temp = aList[marker] 
        aList[marker] = aList[index_of_min] 
        aList[index_of_min] = temp
             
             
             
    
        marker = marker+1
        
        print(aList)
        
aList = [9, 6, 10, 4, 8, 5, 7]        
ss(aList)

