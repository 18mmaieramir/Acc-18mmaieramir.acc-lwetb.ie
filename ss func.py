def ss():
    
    aList = [9, 6, 10, 4, 8, 5, 7]

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
        
        
ss()

 
             
             
          
    
   
             
             
   

