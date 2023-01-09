from random import randrange
for i in range(1):
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
    # multi = int(input("enter 0 for singleplayer or 1 for multiplayer: "))
    # if multi == 0:
    #     cname = "Computer"
    # else:
    #     cname = "Player 2"
    cname = "Computer"
        
    # pc = str(input("Player 1, Choose your counter, X or Y: "))
    # if pc == "x":
    #     X="X"
    # elif pc == "y":
    #     X = "Y"
    # elif pc == "X":
    #     X = "X"
    # elif pc == "Y":
    #     X = "Y"
    # else:
    #     print("invalid input")
    #     go = True
    X = "X"
    S="S"
    # print("Player 1 counter = ",X)
    # print(cname,"counter = ",S)
    while go == False:
        t=0
        for i in r1:
            if i == [0]:
                t+=1
                if t == 0:
                    print("Board full, no winner")
                    go = True
        x = randrange(0,7)

        if x == 0:
            def pos(j=0):
                if r6[j] == [0]:
                    del r6[x]
                    r6.insert(x,X)
                    board()
                elif r5[j] == [0]:
                    del r5[x]
                    r5.insert(x,X)
                    board()
                elif r4[j] == [0]:
                    del r4[x]
                    r4.insert(x,X)
                    board()
                elif r3[j] == [0]:
                    del r3[x]
                    r3.insert(x,X)
                    board()
                elif r2[j] == [0]:
                    del r2[x]
                    r2.insert(x,X)
                    board()
                elif r1[j] == [0]:
                    del r1[x]
                    r1.insert(x,X)
                    board()
                else:
                    print("invalid position or column is full")
                    go = True
            pos()

        elif x==1:
            def pos(j=1):
                if r6[j] == [0]:
                    del r6[x]
                    r6.insert(x,X)
                    board()
                elif r5[j] == [0]:
                    del r5[x]
                    r5.insert(x,X)
                    board()
                elif r4[j] == [0]:
                    del r4[x]
                    r4.insert(x,X)
                    board()
                elif r3[j] == [0]:
                    del r3[x]
                    r3.insert(x,X)
                    board()
                elif r2[j] == [0]:
                    del r2[x]
                    r2.insert(x,X)
                    board()
                elif r1[j] == [0]:
                    del r1[x]
                    r1.insert(x,X)
                    board()
                else:
                    print("invalid")
                    go = True
            pos()
                
        elif x==2:
            def pos(j=2):
                if r6[j] == [0]:
                    del r6[x]
                    r6.insert(x,X)
                    board()
                elif r5[j] == [0]:
                    del r5[x]
                    r5.insert(x,X)
                    board()
                elif r4[j] == [0]:
                    del r4[x]
                    r4.insert(x,X)
                    board()
                elif r3[j] == [0]:
                    del r3[x]
                    r3.insert(x,X)
                    board()
                elif r2[j] == [0]:
                    del r2[x]
                    r2.insert(x,X)
                    board()
                elif r1[j] == [0]:
                    del r1[x]
                    r1.insert(x,X)
                    board()
                else:
                    print("invalid")
                    go = True
            pos()
        elif x==3:
            def pos(j=3):
                if r6[j] == [0]:
                    del r6[x]
                    r6.insert(x,X)
                    board()
                elif r5[j] == [0]:
                    del r5[x]
                    r5.insert(x,X)
                    board()
                elif r4[j] == [0]:
                    del r4[x]
                    r4.insert(x,X)
                    board()
                elif r3[j] == [0]:
                    del r3[x]
                    r3.insert(x,X)
                    board()
                elif r2[j] == [0]:
                    del r2[x]
                    r2.insert(x,X)
                    board()
                elif r1[j] == [0]:
                    del r1[x]
                    r1.insert(x,X)
                    board()
                else:
                    print("invalid")
                    go = True
            pos()
        elif x == 4:
            def pos(j=4):
                if r6[j] == [0]:
                    del r6[x]
                    r6.insert(x,X)
                    board()
                elif r5[j] == [0]:
                    del r5[x]
                    r5.insert(x,X)
                    board()
                elif r4[j] == [0]:
                    del r4[x]
                    r4.insert(x,X)
                    board()
                elif r3[j] == [0]:
                    del r3[x]
                    r3.insert(x,X)
                    board()
                elif r2[j] == [0]:
                    del r2[x]
                    r2.insert(x,X)
                    board()
                elif r1[j] == [0]:
                    del r1[x]
                    r1.insert(x,X)
                    board()
                else:
                    print("invalid")
                    go = True
            pos()
        elif x == 5:
                def pos(j=5):
                    if r6[j] == [0]:
                        del r6[x]
                        r6.insert(x,X)
                        board()
                    elif r5[j] == [0]:
                        del r5[x]
                        r5.insert(x,X)
                        board()
                    elif r4[j] == [0]:
                        del r4[x]
                        r4.insert(x,X)
                        board()
                    elif r3[j] == [0]:
                        del r3[x]
                        r3.insert(x,X)
                        board()
                    elif r2[j] == [0]:
                        del r2[x]
                        r2.insert(x,X)
                        board()
                    elif r1[j] == [0]:
                        del r1[x]
                        r1.insert(x,X)
                        board()
                    else:
                        print("invalid")
                        go = True
                pos()
        elif x ==6:
                def pos(j=6):
                    if r6[j] == [0]:
                        del r6[x]
                        r6.insert(x,X)
                        board()
                    elif r5[j] == [0]:
                        del r5[x]
                        r5.insert(x,X)
                        board()
                    elif r4[j] == [0]:
                        del r4[x]
                        r4.insert(x,X)
                        board()
                    elif r3[j] == [0]:
                        del r3[x]
                        r3.insert(x,X)
                        board()
                    elif r2[j] == [0]:
                        del r2[x]
                        r2.insert(x,X)
                        board()
                    elif r1[j] == [0]:
                        del r1[x]
                        r1.insert(x,X)
                        board()
                    else:
                        print("column full")
                pos()
        else:
            print("ivalid position, enter position between 1-6")
    #######################################################################

    #vertical win check (r6-r3)
        if r6[0] == X and r5[0] == X and r4[0] == X and r3[0] == X:
            print("Player 1 wins")
            go = True
            
            
        elif r6[1] == X and r5[1] == X and r4[1] == X and r3[1] == X:
            print("Player 1 wins")
            go = True

        elif r6[2] == X and r5[2] == X and r4[2] == X and r3[2] == X:
            print("Player 1 wins")
            go = True

        elif r6[3] == X and r5[3] == X and r4[3] == X and r3[3] == X:
            print("Player 1 wins")
            go = True

        elif r6[4] == X and r5[4] == X and r4[4] == X and r3[4] == X:
            print("Player 1 wins")
            go = True
        
        elif r6[5] == X and r5[5] == X and r4[5] == X and r3[5] == X:
            print("Player 1 wins")
            go = True     
        
        elif r6[6] == X and r5[6] == X and r4[6] == X and r3[6] == X:
            print("Player 1 wins")
            go = True

    #######################################################  vertical player(r4-r1)  
        if r4[0] == X and r3[0] == X and r2[0] == X and r1[0] == X:
            print("Player 1 wins")
            go = True
            
        elif r4[1] == X and r3[1] == X and r2[1] == X and r1[1] == X:
            print("Player 1 wins")
            go = True

        elif r4[2] == X and r3[2] == X and r2[2] == X and r1[2] == X:
            print("Player 1 wins")
            go = True

        elif r4[3] == X and r3[3] == X and r2[3] == X and r1[3] == X:
            print("Player 1 wins")
            go = True

        elif r4[4] == X and r3[4] == X and r2[4] == X and r1[4] == X:
            print("Player 1 wins")
            go = True
        
        elif r4[5] == X and r3[5] == X and r2[5] == X and r1[5] == X:
            print("Player 1 wins")
            go = True     
        
        elif r4[6] == X and r3[6] == X and r2[6] == X and r1[6] == X:
            print("Player 1 wins")
            go = True
       
    ############################################################### (player vert win check)
        if r5[0] == X and r4[0] == X and r3[0] == X and r2[0] == X:
            print("Player 1 wins")
            go = True
            
        elif r5[1] == X and r4[1] == X and r3[1] == X and r2[1] == X:
            print("Player 1 wins")
            go = True

        elif r5[2] == X and r4[2] == X and r3[2] == X and r2[2] == X:
            print("Player 1 wins")
            go = True

        elif r5[3] == X and r4[3] == X and r3[3] == X and r2[3] == X:
            print("Player 1 wins")
            go = True

        elif r5[4] == X and r4[4] == X and r3[4] == X and r2[4] == X:
            print("Player 1 wins")
            go = True
        
        elif r5[5] == X and r4[5] == X and r3[5] == X and r2[5] == X:
            print("Player 1 wins")
            go = True     
        
        elif r5[6] == X and r4[6] == X and r3[6] == X and r2[6] == X:
            print("Player 1 wins")
            go = True
    ############################################################### horz
        for i in r6:
            if i ==X:
                e = r6.index(i)
                if e >= 4:
                    if r6[e] == X and r6[e-1]==X and r6[e-2]==X and r6[e-3]==X:
                        go = True
                else:
                    if r6[e] == X and r6[e+1]==X and r6[e+2]==X and r6[e+3]==X:
                        go = True
                        print("Game over, Player 1 wins")
                        break

        for i in r5:
            if i ==X:
                e = r5.index(i)
                if e > 3:
                    if r5[e] == X and r5[e-1]==X and r5[e-2]==X and r5[e-3]==X:
                        go = True
                else:
                    if r5[e] == X and r5[e+1]==X and r5[e+2]==X and r5[e+3]==X:
                        go = True
                        print("Game over, Player 1 wins")
                        break                
        for i in r4:
            if i ==X:
                e = r4.index(i)
                if e > 3:
                    if r4[e] == X and r4[e-1]==X and r4[e-2]==X and r4[e-3]==X:
                        go = True
                else:
                    if r4[e] == X and r4[e+1]==X and r4[e+2]==X and r4[e+3]==X:
                        go = True
                        print("Game over, Player 1 wins")
                        break

        for i in r3:
            if i ==X:
                e = r3.index(i)
                if e >= 4:
                    if r3[e] == X and r3[e-1]==X and r3[e-2]==X and r3[e-3]==X:
                        go = True
                else:
                    if r3[e] == X and r3[e+1]==X and r3[e+2]==X and r3[e+3]==X:
                        go = True
                        print("Game over, Player 1 wins")
                        break        

        for i in r2:
            if i ==X:
                e = r2.index(i)
                if e >= 4:
                    if r2[e] == X and r2[e-1]==X and r2[e-2]==X and r2[e-3]==X:
                        go = True
                else:
                    if r2[e] == X and r2[e+1]==X and r2[e+2]==X and r2[e+3]==X:
                        go = True
                        print("Game over, Player 1 wins")
                        break
        for i in r1:
            if i ==X:
                e = r1.index(i)
                if e >= 4:
                    if r1[e] == X and r1[e-1]==X and r1[e-2]==X and r1[e-3]==X:
                        go = True
                else:
                    if r1[e] == X and r1[e+1]==X and r1[e+2]==X and r1[e+3]==X:
                        go = True
                        print("Game over, Player 1 wins")
                        break
    ################################################################################################## dia
        for i in r3:
            if i ==X:
                e = r3.index(i)
                if e == 3:
                    if r3[e] == X and r4[e-1]==X and r5[e-2]==X and r6[e-3]==X:
                        go = True
                        print("Game over, Player 1 wins")
                        break
                    if r3[e] == X and r4[e+1]==X and r5[e+2]==X and r6[e+3]==X:
                        go = True
                        print("Game over, Player 1 wins")
                        break
                    else:
                        pass
                if e >= 4:
                    if r3[e] == X and r4[e-1]==X and r5[e-2]==X and r6[e-3]==X:
                        go = True
                        print("Game over, Player 1 wins")
                        break
                elif e < 3:
                    if r3[e] == X and r4[e+1]==X and r5[e+2]==X and r6[e+3]==X:
                        go = True
                        print("Game over, Player 1 wins")
                        break
        for i in r2:
            if i == X:
                e = r2.index(i)
                if e == 3:
                    if r2[e] == X and r3[e-1]==X and r4[e-2]==X and r5[e-3]==X:
                        go = True
                        print("Game over, Player 1 wins")
                        break
                    if r2[e] == X and r3[e+1]==X and r4[e+2]==X and r5[e+3]==X:
                        go = True
                        print("Game over, Player 1 wins")
                        break
                    else:
                        pass
                    
        for i in r1:
            if i ==X:
                e = r1.index(i)
                if e == 3:
                    if r1[e] == X and r2[e-1]==X and r3[e-2]==X and r4[e-3]==X:
                        go = True
                        print("Game over, Player 1 wins")
                        break
                    if r1[e] == X and r2[e+1]==X and r3[e+2]==X and r4[e+3]==X:
                        go = True
                        print("Game over, Player 1 wins")
                        break
                    else:
                        pass
                if e >= 4:
                    if r1[e] == X and r2[e-1]==X and r3[e-2]==X and r4[e-3]==X:
                        go = True
                        print("Game over, Player 1 wins")
                        break
                elif e < 3:
                    if r1[e] == X and r2[e+1]==X and r3[e+2]==X and r4[e+3]==X:
                        go = True
                        print("Game over, Player 1 wins")
                        break    
    ###############################################################
        if go == False:
            go = False
            
            cx = randrange(0,7)


            if cx == 0:
                def pos(j=0):
                    if r6[j] == [0]:
                        del r6[cx]
                        r6.insert(cx,S)
                        board()
                    elif r5[j] == [0]:
                        del r5[cx]
                        r5.insert(cx,S)
                        board()
                    elif r4[j] == [0]:
                        del r4[cx]
                        r4.insert(cx,S)
                        board()
                    elif r3[j] == [0]:
                        del r3[cx]
                        r3.insert(cx,S)
                        board()
                    elif r2[j] == [0]:
                        del r2[cx]
                        r2.insert(cx,S)
                        board()
                    elif r1[j] == [0]:
                        del r1[cx]
                        r1.insert(cx,S)
                        board()
                    else:
                        
                        go = False
                pos()

            elif cx==1:
                def pos(j=1):
                    if r6[j] == [0]:
                        del r6[cx]
                        r6.insert(cx,S)
                        board()
                    elif r5[j] == [0]:
                        del r5[cx]
                        r5.insert(cx,S)
                        board()
                    elif r4[j] == [0]:
                        del r4[cx]
                        r4.insert(cx,S)
                        board()
                    elif r3[j] == [0]:
                        del r3[cx]
                        r3.insert(cx,S)
                        board()
                    elif r2[j] == [0]:
                        del r2[cx]
                        r2.insert(cx,S)
                        board()
                    elif r1[j] == [0]:
                        del r1[cx]
                        r1.insert(cx,S)
                        board()
                    else:
                        go = False
                pos()
                    
            elif cx==2:
                def pos(j=2):
                    if r6[j] == [0]:
                        del r6[cx]
                        r6.insert(cx,S)
                        board()
                    elif r5[j] == [0]:
                        del r5[cx]
                        r5.insert(cx,S)
                        board()
                    elif r4[j] == [0]:
                        del r4[cx]
                        r4.insert(cx,S)
                        board()
                    elif r3[j] == [0]:
                        del r3[cx]
                        r3.insert(cx,S)
                        board()
                    elif r2[j] == [0]:
                        del r2[cx]
                        r2.insert(cx,S)
                        board()
                    elif r1[j] == [0]:
                        del r1[cx]
                        r1.insert(cx,S)
                        board()
                    else:
                        go = False
                pos()
            elif cx==3:
                def pos(j=3):
                    if r6[j] == [0]:
                        del r6[cx]
                        r6.insert(cx,S)
                        board()
                    elif r5[j] == [0]:
                        del r5[cx]
                        r5.insert(cx,S)
                        board()
                    elif r4[j] == [0]:
                        del r4[cx]
                        r4.insert(cx,S)
                        board()
                    elif r3[j] == [0]:
                        del r3[cx]
                        r3.insert(cx,S)
                        board()
                    elif r2[j] == [0]:
                        del r2[cx]
                        r2.insert(cx,S)
                        board()
                    elif r1[j] == [0]:
                        del r1[cx]
                        r1.insert(cx,S)
                        board()
                    else:
                        go = False
                pos()
            elif cx == 4:
                def pos(j=4):
                    if r6[j] == [0]:
                        del r6[cx]
                        r6.insert(cx,S)
                        board()
                    elif r5[j] == [0]:
                        del r5[cx]
                        r5.insert(cx,S)
                        board()
                    elif r4[j] == [0]:
                        del r4[cx]
                        r4.insert(cx,S)
                        board()
                    elif r3[j] == [0]:
                        del r3[cx]
                        r3.insert(cx,S)
                        board()
                    elif r2[j] == [0]:
                        del r2[cx]
                        r2.insert(cx,S)
                        board()
                    elif r1[j] == [0]:
                        del r1[cx]
                        r1.insert(cx,S)
                        board()
                    else:
                        go = False
                pos()
            elif cx == 5:
                    def pos(j=5):
                        if r6[j] == [0]:
                            del r6[cx]
                            r6.insert(cx,S)
                            board()
                        elif r5[j] == [0]:
                            del r5[cx]
                            r5.insert(cx,S)
                            board()
                        elif r4[j] == [0]:
                            del r4[cx]
                            r4.insert(cx,S)
                            board()
                        elif r3[j] == [0]:
                            del r3[cx]
                            r3.insert(cx,S)
                            board()
                        elif r2[j] == [0]:
                            del r2[cx]
                            r2.insert(cx,S)
                            board()
                        elif r1[j] == [0]:
                            del r1[cx]
                            r1.insert(cx,S)
                            board()
                        else:
                            go = False
                    pos()
            elif cx ==6:
                    def pos(j=6):
                        if r6[j] == [0]:
                            del r6[cx]
                            r6.insert(cx,S)
                            board()
                        elif r5[j] == [0]:
                            del r5[cx]
                            r5.insert(cx,S)
                            board()
                        elif r4[j] == [0]:
                            del r4[cx]
                            r4.insert(cx,S)
                            board()
                        elif r3[j] == [0]:
                            del r3[cx]
                            r3.insert(cx,S)
                            board()
                        elif r2[j] == [0]:
                            del r2[cx]
                            r2.insert(cx,S)
                            board()
                        elif r1[j] == [0]:
                            del r1[cx]
                            r1.insert(cx,S)
                            board()
                        else:
                            go = False
                    pos()
    ######################################################################## (vert checks)

        if r6[0] == S and r5[0] == S and r4[0] == S and r3[0] == S:
            print(cname,"  Wins")
            go = True
            
        elif r6[1] == S and r5[1] == S and r4[1] == S and r3[1] == S:
            print(cname,"  Wins")
            go = True

        elif r6[2] == S and r5[2] == S and r4[2] == S and r3[2] == S:
            print(cname,"  Wins")
            go = True

        elif r6[3] == S and r5[3] == S and r4[3] == S and r3[3] == S:
            print(cname,"  Wins")
            go = True

        elif r6[4] == S and r5[4] == S and r4[4] == S and r3[4] == S:
            print(cname,"  Wins")
            go = True
        
        elif r6[5] == S and r5[5] == S and r4[5] == S and r3[5] == S:
            print(cname,"  Wins")
            go = True     
        
        elif r6[6] == S and r5[6] == S and r4[6] == S and r3[6] == S:
            print(cname,"  Wins")
            go = True

    #######################################################################  (Vert) 
        if r4[0] == S and r3[0] == S and r2[0] == S and r1[0] == S:
            print(cname,"  Wins")
            go = True
            
            
        elif r4[1] == S and r3[1] == S and r2[1] == S and r1[1] == S:
            print(cname,"  Wins")
            go = True

        elif r4[2] == S and r3[2] == S and r2[2] == S and r1[2] == S:
            print(cname,"  Wins")
            go = True

        elif r4[3] == S and r3[3] == S and r2[3] == S and r1[3] == S:
            print(cname,"  Wins")
            go = True

        elif r4[4] == S and r3[4] == S and r2[4] == S and r1[4] == S:
            print(cname,"  Wins")
            go = True
        
        elif r4[5] == S and r3[5] == S and r2[5] == S and r1[5] == S:
            print(cname,"  Wins")
            go = True     
        
        elif r4[6] == S and r3[6] == S and r2[6] == S and r1[6] == S:
            print(cname,"  Wins")
            go = True
    ######################################################################## vert
        if r5[0] == S and r4[0] == S and r3[0] == S and r2[0] == S:
            print(cname,"  Wins")
            go = True
            
        elif r5[1] == S and r4[1] == S and r3[1] == S and r2[1] == S:
            print(cname,"  Wins")
            go = True

        elif r5[2] == S and r4[2] == S and r3[2] == S and r2[2] == S:
            print(cname,"  Wins")
            go = True

        elif r5[3] == S and r4[3] == S and r3[3] == S and r2[3] == S:
            print(cname,"  Wins")
            go = True

        elif r5[4] == S and r4[4] == S and r3[4] == S and r2[4] == S:
            print(cname,"  Wins")
            go = True
        
        elif r5[5] == S and r4[5] == S and r3[5] == S and r2[5] == S:
            print(cname,"  Wins")
            go = True     
        
        elif r5[6] == S and r4[6] == S and r3[6] == S and r2[6] == S:
            print(cname,"  Wins")
            go = True
    ################################################################################################### horz
        for i in r6:
            if i =="S":
                e = r6.index(i)

                if e >= 4:
                    if r6[e] == "S" and r6[e-1]=="S" and r6[e-2]=="S" and r6[e-3]=="S":
                        go = True
                else:
                    if r6[e] == "S" and r6[e+1]=="S" and r6[e+2]=="S" and r6[e+3]=="S":
                        go = True
                        print("Game over", cname , "wins")
                        break

        for i in r5:
            if i =="S":
                e = r5.index(i)
                if e >= 4:
                    if r5[e] == "S" and r5[e-1]=="S" and r5[e-2]=="S" and r5[e-3]=="S":
                        go = True
                else:
                    if r5[e] == "S" and r5[e+1]=="S" and r5[e+2]=="S" and r5[e+3]=="S":
                        go = True
                        print("Game over", cname , "wins")
                        break                
        for i in r4:
            if i =="S":
                e = r4.index(i)
                if e >= 4:
                    if r4[e] == "S" and r4[e-1]=="S" and r4[e-2]=="S" and r4[e-3]=="S":
                        go = True
                else:
                    if r4[e] == "S" and r4[e+1]=="S" and r4[e+2]=="S" and r4[e+3]=="S":
                        go = True
                        print("Game over", cname , "wins")
                        break

        for i in r3:
            if i =="S":
                e = r3.index(i)
                if e >= 4:
                    if r3[e] == "S" and r3[e-1]=="S" and r3[e-2]=="S" and r3[e-3]=="S":
                        go = True
                else:
                    if r3[e] == "S" and r3[e+1]=="S" and r3[e+2]=="S" and r3[e+3]=="S":
                        go = True
                        print("Game over", cname , "wins")
                        break        

        for i in r2:
            if i =="S":
                e = r2.index(i)
                if e >= 4:
                    if r2[e] == "S" and r2[e-1]=="S" and r2[e-2]=="S" and r2[e-3]=="S":
                        go = True
                else:
                    if r2[e] == "S" and r2[e+1]=="S" and r2[e+2]=="S" and r2[e+3]=="S":
                        go = True
                        print("Game over", cname , "wins")
                        break
        for i in r1:
            if i =="S":
                e = r1.index(i)
                if e >= 4:
                    if r1[e] == "S" and r1[e-1]=="S" and r1[e-2]=="S" and r1[e-3]=="S":
                        go = True
                else:
                    if r1[e] == "S" and r1[e+1]=="S" and r1[e+2]=="S" and r1[e+3]=="S":
                        go = True
                        print("Game over", cname , "wins")
                        break
    ########################################################################################################### dia
        for i in r3:
            if i ==S:
                e = r3.index(i)
                if e == 3:
                    if r3[e] == S and r4[e-1]==S and r5[e-2]==S and r6[e-3]==S:
                        go = True
                        print("Game over", cname , "wins")
                        break
                    if r3[e] == S and r4[e+1]==S and r5[e+2]==S and r6[e+3]==S:
                        go = True
                        print("Game over", cname , "wins")
                        break
                    else:
                        pass
                if e >= 4:
                    if r3[e] == S and r4[e-1]==S and r5[e-2]==S and r6[e-3]==S:
                        go = True
                        print("Game over", cname , "wins")
                        break
                elif e < 3:
                    if r3[e] == S and r4[e+1]==S and r5[e+2]==S and r6[e+3]==S:
                        go = True
                        print("Game over", cname , "wins")
                        break
        for i in r2:
            if i == S:
                e = r2.index(i)
                if e == 3:
                    if r2[e] == S and r3[e-1]==S and r4[e-2]==S and r5[e-3]==S:
                        go = True
                        print("Game over", cname , "wins")
                        break
                    if r2[e] == S and r3[e+1]==S and r4[e+2]==S and r5[e+3]==S:
                        go = True
                        print("Game over", cname , "wins")
                        break
                    else:
                        pass
                    
        for i in r1:
            if i ==S:
                e = r1.index(i)
                if e == 3:
                    if r1[e] == S and r2[e-1]==S and r3[e-2]==S and r4[e-3]==S:
                        go = True
                        print("Game over", cname , "wins")
                        break
                    if r1[e] == S and r2[e+1]==S and r3[e+2]==S and r4[e+3]==S:
                        go = True
                        print("Game over", cname , "wins")
                        break
                    else:
                        pass
                if e >= 4:
                    if r1[e] == S and r2[e-1]==S and r3[e-2]==S and r4[e-3]==S:
                        go = True
                        print("Game over", cname , "wins")
                        break
                elif e < 3:
                    if r1[e] == S and r2[e+1]==S and r3[e+2]==S and r4[e+3]==S:
                        go = True
                        print("Game over", cname , "wins")
                        break     
