


inp = input("File name?")
f1= open(inp,"r")
lines = (f1.readlines())
print(len(lines))


tw=0
for i in lines:
    words = i.split()
    tw += len(words)

print(tw)



tc=0
for i in lines:
    char= i.split()
    tc += len(i)

print(tc)