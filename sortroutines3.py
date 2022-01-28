import sortRoutines2
import sys
sortRoutines2.selectionSort()

for i in sys.argv:
    print(i)
   
collection = []    
   
fi = open(sys.argv[1], "r")
for line in fi:
    for item in line.split(" "):
        if item != " " and item!= "\n":
            collection.append(int(item))
            
print(collection)