from random import randrange
f=open("l.txt","w")
p1=  str(input("enter player 1 email: "))
m = 0
cm = 0
pw = 0
cw = 0
dr = 0
current_game =0

for i in range(100):
    r1 = [[0],[0],[0],[0],[0],[0],[0]]
    r2 = [[0],[0],[0],[0],[0],[0],[0]]
    r3 = [[0],[0],[0],[0],[0],[0],[0]]
    r4 = [[0],[0],[0],[0],[0],[0],[0]]
    r5 = [[0],[0],[0],[0],[0],[0],[0]]
    r6 = [[0],[0],[0],[0],[0],[0],[0]]
    key ="  0    1    2    3    4    5    6   "
    
    
    current_game = i
    
    def board():

        print(r1)
        print(r2)
        print(r3)
        print(r4)
        print(r5)
        print(r6)
        print(key)
        print("")

    g = 0
    #print(g)

    cname = "C"
    
    X = "X"
    S="S"

    while g<1:
        co =0
        for i in r1:
            if i == [0]:
                co +=1
                
        if co == 0:
            print("no winner")
            dr+=1
            g+=1
            
            break


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
                
        x = randrange(0,7)
        pos(x)
        m+=1

    #######################################################################
        def wins(b1,o1,win_counter): #vert
            global g
            global pw
            global cw
            #print("currently playing vert",current_game)
         
            for b in range(0,7):
            
                if r6[b] == b1 and r5[b] == b1 and r4[b] == b1 and r3[b] == b1:
                    print(o1,"  Wins vert")
                    f.write(o1)
                    if win_counter == "p":
                        pw+=1
                        g+=1
                        break
                    else:
                        cw+=1
                        g+=1
                        break
                    
                    #print(g)
                    break
                    

                if r4[b] == b1 and r3[b] == b1 and r2[b] == b1 and r1[b] == b1:
                    print(o1,"  Wins vert")
                    f.write(o1)
                    if win_counter == "p":
                        pw+=1
                        g= True
                        break
                    else:
                        cw+=1
                        g=True
                   
                    #print(g)
                    break

                if r5[b] == b1 and r4[b] == b1 and r3[b] == b1 and r2[b] == b1:
                     print(o1,"  Winsvert")
                     f.write(o1)
                     if win_counter == "p":
                         pw+=1
                         g+=1
                         
                     else:
                         cw+=1
                         g+=1
                     
                     #print(g)
                     break
        if not g:
            wins(X,p1,"p")
 ################################################################################# horz       
        def horz(k,q,r,v):
            global pw
            global g
            global cw
            global current_game
            #print("currently playing horz",current_game)
            for i in k:
                if i ==q:
                    e = k.index(i)
                    if e >= 4:
                        if k[e] == q and k[e-1]==q and k[e-2]==q and k[e-3]==q:
                            print(v, "winshorz")
                            if r == "p":
                                pw+=1
                            else:
                                cw+=1
                            g+=1
                            #print(g)
                            break
                        
                    
                    else:
                        if k[e] == q and k[e+1]==q and k[e+2]==q and k[e+3]==q:
                            
                            print(v, "winshorz")
                            if r == "p":
                                pw+=1
                            else:
                                cw+=1                           
                            g+=1
                           # print(g)
                            break
                        
       # print(g)         
        if not g:               
            horz(r6,X,"p",p1)
        if not g:
            horz(r5,X,"p",p1)
        if not g:
            horz(r4,X,"p",p1)
        if not g:
            horz(r3,X,"p",p1)
        if not g:
            horz(r2,X,"p",p1)
        if not g:
            horz(r1,X,"p",p1)

    ################################################################################################## dia
        def diawins(b,r,t1):
            global g
            global pw
            global cw
            
            #print("currently playing dia",current_game)
            for i in r3:
                if i ==b:
                    e = r3.index(i)
                    if e == 3:
                        if r3[e] == b and r4[e-1]==b and r5[e-2]==b and r6[e-3]==b:
                            
                            print(t1, "wins dia")
                            if r == "p":
                                pw+=1
                            else:
                                cw+=1
                            g+=1
                            #print(g)
                            break


                        
                        if r3[e] == b and r4[e+1]==b and r5[e+2]==b and r6[e+3]==b:
                            
                            print(t1, "winsdia")
                            if r == "p":
                                pw+=1
                            else:
                                cw+=1
                            g+=1
                            #print(g)
                            break
                        
                  
                       
                    if e >= 4:
                        if r3[e] == b and r4[e-1]==b and r5[e-2]==b and r6[e-3]==b:
                            
                            print(t1, "winsdia")
                            if r == "p":
                                pw+=1
                            else:
                                cw+=1
                            g+=1
                            #print(g)
                            break
                      
              
                    elif e < 3:
                        if r3[e] == b and r4[e+1]==b and r5[e+2]==b and r6[e+3]==b:
                            
                            print(t1, "winsdia")
                            if r == "p":
                                pw+=1
                            else:
                                cw+=1
                            g+=1
                            #print(g)
                            break
                        
            if not g:     
                for i in r2:
                    if i == b:
                        e = r2.index(i)
                        if e == 3:
                            if r2[e] == b and r3[e-1]==b and r4[e-2]==b and r5[e-3]==b:    
                                print(t1, "winsdia2")
                                if r == "p":
                                    pw+=1
                                else:
                                    cw+=1
                                g+=1
                                #print(g)
                                break
                           
                       
                            if r2[e] == b and r3[e+1]==b and r4[e+2]==b and r5[e+3]==b:
                                
                                print(t1, "winsdia2")
                                if r == "p":
                                    pw+=1
                                else:
                                    cw+=1
                                g+=1
                                #print(g)
                                break
                           
            if not g:
                for i in r1:
                    if i ==b:
                        e = r1.index(i)
                        if e == 3:
                            if r1[e] == b and r2[e-1]==b and r3[e-2]==b and r4[e-3]==b:
                                print(t1, "winsdia3")
                                if r == "p":
                                    pw+=1
                                else:
                                    cw+=1
                                g+=1
                                #print(g)
                                break
                           
                            if r1[e] == b and r2[e+1]==b and r3[e+2]==b and r4[e+3]==b:
                                
                                print(t1, "winsdia3")
                                if r == "p":
                                    pw+=1
                                else:
                                    cw+=1
                                g+=1
                                #print(g)
                                break
                          
                       
                        if e >= 4:
                            if r1[e] == b and r2[e-1]==b and r3[e-2]==b and r4[e-3]==b:                       
                                print(t1, "winsdia3")
                                if r == "p":
                                    pw+=1
                                else:
                                    cw+=1
                                g+=1
                                #print(g)
                                break
                           
                        
                        elif e < 3:
                            if r1[e] == b and r2[e+1]==b and r3[e+2]==b and r4[e+3]==b:
                                
                                print(t1, "winsdia3")
                                if r == "p":
                                    pw+=1
                                else:
                                    cw+=1
                                g+=1
                                #print(g)
                                break
        #print(g,"dia",g)              
        if not g:   
            diawins(X,"p",p1)
        
    ############################################################### computer turn

        def pos1(j):
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
                    

        cx = randrange(0,7)
        pos1(cx)
        cm +=1 
        if not g:   
            wins(S,cname,"c")
    ########################################################################### horz        
        if not g:   
            horz(r6,S,cw,cname)
        if not g:   
            horz(r5,S,cw,cname)
        if not g:   
            horz(r4,S,cw,cname)
        if not g:   
            horz(r3,S,cw,cname)
        if not g:   
            horz(r2,S,cw,cname)
        if not g:   
            horz(r1,S,cw,cname)
############################################################################# dia
        if not g:   
            diawins(S,"c",cname)
#############################################################################
    
   
print(p1,"moves = ",m)
print(cname," moves= ",cm)
print("draws :", dr )
print(p1,"wins = ", pw)
print(cname, "wins = ", cw)
