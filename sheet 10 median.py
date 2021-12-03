#median
file = open("10Random.txt", "r")
list2 = []

for line in file:
    for item in line.split():
        list2.append(int(item))

list2.sort()

print(list2)

half =len(list2) // 2
print(half)
indece = [5]
extracted_elements = [list2[index] for index in indece]


print("median is" , extracted_elements)
