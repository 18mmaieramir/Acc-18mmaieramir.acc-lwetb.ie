from random import randrange
p1=  str(input("enter player 1 name: "))
m = 0
cm = 0
pw = 0
cw = 0

r1 = [[0],[0],[0],[0],[0],[0],[0]]
r2 = [[0],[0],[0],[0],[0],[0],[0]]
r3 = [[0],[0],[0],[0],[0],[0],[0]]
r4 = [[0],[0],[0],[0],[0],[0],[0]]
r5 = [[0],[0],[0],[0],[0],[0],[0]]
r6 = [[0],[0],[0],[0],[0],[0],[0]]
key ="  0    1    2    3    4    5    6   " 
def board():

    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(r6)
    print(key)
    print("")

board()
go = False
multi = int(input("enter 0 for singleplayer or 1 for multiplayer: "))
if multi == 0:
    cname = "Computer"
else:
    cname = str(input("enter player 2 name: "))



X = "X"
S="S"
print(p1," counter = ",X)
print(cname,"counter = ",S)
while go == False:
    co =0
    for i in r1:
        if i == [0]:
            co +=1
    if co == 0:
        print("no winner")
        go = True
        break
    t=0
    for i in r1:
        if i == [0]:
            t+=1
            if t == 0:
                print("Board full, no winner")
                go = True
    x = int(input("Player 1, Enter which column you wish to drop counter:"))
    m+=1
    def pos(j):
        if r6[j] == [0]:
            del r6[x]
            r6.insert(x,X)
            
        elif r5[j] == [0]:
            del r5[x]
            r5.insert(x,X)
            
        elif r4[j] == [0]:
            del r4[x]
            r4.insert(x,X)
            
        elif r3[j] == [0]:
            del r3[x]
            r3.insert(x,X)
            
        elif r2[j] == [0]:
            del r2[x]
            r2.insert(x,X)
            
        elif r1[j] == [0]:
            del r1[x]
            r1.insert(x,X)
        board()

        
   
    pos(x)
  

#######################################################################
    def wins(b1, o1):
        global go
        def vert5(b,o1):
           
            global go
            if r6[b] == b1 and r5[b] == b1 and r4[b] == b1 and r3[b] == b1:
                print(o1,"  Wins")
             
                go = True
                
            else:
                pass
        
        for i in range(0,7):
            vert5(i,o1)    
    #######################################################################
    #vertical win check (r6-r3)
        def vert3(b,o1):

            global go
            if r4[b] == b1 and r3[b] == b1 and r2[b] == b1 and r1[b] == b1:
                print(o1,"  Wins")
                
                go = True
                
            else:
                pass
        for i in range(0,7):
            vert3(i,o1)
    ######################################################################## vert
        def vert4(b,o1):
 
            global go
            if r5[b] == b1 and r4[b] == b1 and r3[b] == b1 and r2[b] == b1:
                print(o1,"  Wins")
               
                go = True
                
            else:
                pass
        
        for i in range(0,7):
            vert4(i,o1)
    ############################################################### horz
        def horz(k,o1):
            global pw 

            global go
            for i in k:
                if i ==b1:
                    e = k.index(i)
                    if e >= 4:
                        if k[e] == b1 and k[e-1]==b1 and k[e-2]==b1 and k[e-3]==b1:
                            print("Game over, ",o1," wins")
                            
                            go = True
                            break
                        break
                    
                    else:
                    
                        if k[e] == b1 and k[e+1]==b1 and k[e+2]==b1 and k[e+3]==b1:                       
                            print("Game over, ",o1," wins")
                            
                            go = True
                            break
                        break
        horz(r6,o1)
        horz(r5,o1)
        horz(r4,o1)
        horz(r3,o1)
        horz(r2,o1)
        horz(r1,o1)

    ################################################################################################## dia
        for i in r3:
            if i ==b1:
                e = r3.index(i)
                if e == 3:
                    if r3[e] == b1 and r4[e-1]==b1 and r5[e-2]==b1 and r6[e-3]==b1:
                        
                        print("Game over, ",o1," wins")
                       
                        go = True
                        break
                    break
                    if r3[e] == b1 and r4[e+1]==b1 and r5[e+2]==b1 and r6[e+3]==b1:
                        
                        print("Game over, ",o1," wins")
                        
                        go = True
                        break
                    break
                   
                if e >= 4:
                    if r3[e] == b1 and r4[e-1]==b1 and r5[e-2]==b1 and r6[e-3]==b1:
                        
                        print("Game over, ",o1," wins")
                        
                        go = True
                        break
                    break
                elif e < 3:
                    if r3[e] == b1 and r4[e+1]==b1 and r5[e+2]==b1 and r6[e+3]==b1:
                        
                        print("Game over, ",o1," wins")
                                             
                        go = True
                        break
                    break
        for i in r2:
            if i == b1:
                e = r2.index(i)
                if e == 3:
                    if r2[e] == b1 and r3[e-1]==b1 and r4[e-2]==b1 and r5[e-3]==b1:    
                        print("Game over, ",o1," wins")
                        
                        go = True
                        break
                    break
                    if r2[e] == b1 and r3[e+1]==b1 and r4[e+2]==b1 and r5[e+3]==b1:
                        
                        print("Game over, ",o1," wins")
                      
                        go = True
                        break
                    break

        for i in r1:
            if i ==b1:
                e = r1.index(i)
                if e == 3:
                    if r1[e] == b1 and r2[e-1]==b1 and r3[e-2]==b1 and r4[e-3]==b1:
                        print("Game over, ",o1," wins")
                        
                        go = True
                        break
                    break
                    if r1[e] == b1 and r2[e+1]==b1 and r3[e+2]==b1 and r4[e+3]==b1:
                        
                        print("Game over, ",o1," wins")
                        
                        go = True
                        break
                    break
                if e >= 4:
                    if r1[e] == b1 and r2[e-1]==b1 and r3[e-2]==b1 and r4[e-3]==b1:                       
                        print("Game over, ",o1," wins")
                        
                        go = True
                        break
                    break
                elif e < 3:
                    if r1[e] == b1 and r2[e+1]==b1 and r3[e+2]==b1 and r4[e+3]==b1:
                        
                        print("Game over, ",o1," wins")
                        
                        go = True
                        break
                    break
    wins(X,p1)
###############################################################
    if go == False:
        go = False
        def pos(j):
            if r6[j] == [0]:
                del r6[cx]
                r6.insert(cx,S)
                
            elif r5[j] == [0]:
                del r5[cx]
                r5.insert(cx,S)
                
            elif r4[j] == [0]:
                del r4[cx]
                r4.insert(cx,S)
                
            elif r3[j] == [0]:
                del r3[cx]
                r3.insert(cx,S)
                
            elif r2[j] == [0]:
                del r2[cx]
                r2.insert(cx,S)
                
            elif r1[j] == [0]:
                del r1[cx]
                r1.insert(cx,S)
                
            else:
                
                go = False
        if multi == 0:
            cx = randrange(0,7)
            cm +=1
        else:
            cx = int(input("Player 2, enter which column you wish to drop counter:"))
            cm+=1
        pos(cx)
        board()
    wins(S,cname)
######################################################################## (vert checks)

print(p1,"moves = ",m)
print(cname," moves= ",cm)