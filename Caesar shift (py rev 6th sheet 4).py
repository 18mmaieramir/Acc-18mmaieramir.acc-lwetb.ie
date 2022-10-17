f1 = open("cs.txt", "r")

word = f1.readline()


letters = "abcdefghijklmnopqrstuvwxyz"



v = int(input("enter amount "))
res = ""

for let in word:
    index = letters.index(let)
    res1 = letters[index + v]
    res = res1 + res
    
print(res)

