

#Insertion Sort
theList = [5, 7, 3, 6, 2] 
#1. Initialise an unsorted list
marker = 1

#3. Traverse through all list items
while (marker < len(theList)):
                j = marker
                while (theList[j] < theList[j-1] and j>0):
                    tmp = theList[j]
                    theList[j] =  theList[j-1]
                    theList[j-1] = tmp
                    j = j-1
                    break
                    

            
marker =  marker+1
print("Sorted LIST IS: " , theList)


