from random import randrange
import itertools

r1 = [[0],[0],[0],[0],[0],[0],[0]]
r2 = [[0],[0],[0],[0],[0],[0],[0]]
r3 = [[0],[0],[0],[0],[0],[0],[0]]
r4 = [[0],[0],[0],[0],[0],[0],[0]]
r5 = [[0],[0],[0],[0],[0],[0],[0]]
r6 = [[0],[0],[0],[0],[0],[0],[0]]

def board():

    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(r6)
    print("")

board()


t=0
w=0
X="X"
C="S"
go = False
sc = True
while go == False:
   
    y = int(input("enter Y position: "))
    x = int(input("enter X position: "))

    pl = []
    cl = []
    scl = []
    
    
    while sc == True:
        while pl == cl:           #ensure computer doesnt choose same position as player
            cx = randrange(1,7)
            cy = randrange(1,6)        
            pl.append(y)
            pl.append(x)
            cl.append(cy)
            cl.append(cx)
        
            
        cx1= cx*cx
        cy1= cy*cy
        cxy = cx1 + cy1
        
        scl.append(cxy)
        for i in scl:
            if i == cxy:
                t+=2
            else:
                sc == False
            if t<=2:
                sc == True
            else:
                sc == False
                
 
        
        
            
        
    
#         x = range(1,7)
#         aList =[]
#         for pair in itertools.combinations(x,2):
#             for i in range(1,7):
#                 aList.append(pair)
#         print (aList)     
#          
        
        
        
        


#         if t >= 2:
#             sc = False
#         else:
#             sc = True
                
      
    
    print("computer chose: ","(",cy,",",cx,")")
    
    
    x = x-1
    if cy == 6:
        for i in r6:
            del r6[cx]
            r6.insert(cx,C)
      

        
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
