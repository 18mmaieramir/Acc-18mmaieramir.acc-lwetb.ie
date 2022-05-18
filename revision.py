f=open("code.txt" ,"r")
f1=open("code2.txt" ,"a+")

x=f.readline()
#1

y=x.split()

m="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in y:
    for j in i:
        if j in m:
            f1.write(j)
            
            

        


f1.write(str(len(y)))

space=len(y) -1
f1.write(str(space))

g="1234567890"
l=[]
for r in y:
    for a in r:
        if a in g:
            l.append(a)
            f1.write(str(len(l)))
             
f1.close()