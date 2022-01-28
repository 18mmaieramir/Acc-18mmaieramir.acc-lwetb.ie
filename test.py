import sortRoutines2
import sys


for i in sys.argv:
    print(i)

collection = []

fi = open(sys.argv[1], "r")
for line in fi:
    for item in line.split(" "):
        if item != ' ' and item != '\n':
            collection.append(int(item))
            
sortRoutines2.selectionSort(collection)       
print(collection)