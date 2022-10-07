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




