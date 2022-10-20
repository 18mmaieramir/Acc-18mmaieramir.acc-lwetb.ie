f1 = open("cs.txt", "r")

word = f1.read()


letters = "abcdefghijklmnopqrstuvwxyz"



v = -1
res = ""

for let in word:
    index = letters.index(let)
    res1 = letters[index - v]
    res = res1 + res
print("Success")

f2= open("cs2.txt", "w")
f2.write(res)
f2.close()




f1.close()

