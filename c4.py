from random import randrange
import random


r1 = [[0],[0],[0],[0],[0],[0],[0]]
r2 = [[0],[0],[0],[0],[0],[0],[0]]
r3 = [[0],[0],[0],[0],[0],[0],[0]]
r4 = [[0],[0],[0],[0],[0],[0],[0]]
r5 = [[0],[0],[0],[0],[0],[0],[0]]
r6 = [[0],[0],[0],[0],[0],[0],[0]]
ky ="  1    2    3    4    5    6    7   " 
def board():

    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(r6)
    print(ky)
    print("")

board()

coords = [(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6)]
l = list(range(1, 36))  
random.shuffle(l)
# print(l)
f=0
w=0
p=0
X="X"
C="S"
go = False
sc = False
while go == False:
    t=0
    x = int(input("enter X position: "))
    y = int(input("enter Y position: "))

    pl = []
    cl = []
    scl = []
    
    
    
    while pl == cl :           
        t=0
        
        for i in l:
            t = l[f+p]
#         print(t)

        rc1=coords[t]
        
        rc2=str(rc1)
#         print(rc2)
        cx = int(rc2[1])
        cy=int(rc2[4])
#         print(cx,cy)
 
   
                
        pl.append(y)          #ensure computer doesnt choose same position as player
        pl.append(x)
        cl.append(cy)
        cl.append(cx)

        p+=1


  

    print("computer chose: ","(",cx,",",cy,")")
    
    
    x = x-1
    if cy == 6:
        for i in r6:
            
            del r6[cx]
            r6.insert(cx,C)
            sc == False
  

        
    elif cy== 5:
        for i in r5:
            del r5[cx]
            r5.insert(cx,C)
   

        
    elif cy== 4:
        for i in r4:
            del r4[cx]
            r4.insert(cx,C)

        
    elif cy==3:
        for i in r3:
            del r3[cx]
            r3.insert(cx,C)
    
        
    elif cy==2:
        for i in r2:
            del r2[cx]
            r2.insert(cx,C)

    
    elif cy==1:
        for i in r1:
            del r1[cx]
            r1.insert(cx,C)

#################################################  

    if y == 6:
        for i in r6:
            del r6[x]
            r6.insert(x,X)
        board()

        
    elif y== 5:
        for i in r5:
            del r5[x]
            r5.insert(x,X)
        board()

        
    elif y== 4:
        for i in r4:
            del r4[x]
            r4.insert(x,X)
        board()
        
    elif y==3:
        for i in r3:
            del r3[x]
            r3.insert(x,X)
        board()
        
    elif y==2:
        for i in r2:
            del r2[x]
            r2.insert(x,X)
        board()
    
    elif y==1:
        for i in r1:
            del r1[x]
            r1.insert(x,X)
        board()
        
        
        
    else:
        print("Invalid position, please enter position between 1-6!!!!")
        break

#     for i in r1:       #horizontal win check for row 1
#         if i == "X":
#             w+= 1
#             e=r1.index(i)
#             if r1[e+1] == "X":
#                 w+=1
#                 if r1[e+2] == "X":
#                     w+=1
#                     if r1[e+3] == "X":
#                         w+=2
#                         go = True
        
      
if w>4:
    print("Game Over")
    
else:
    print("")
