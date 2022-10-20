def caesar(email):
    s = str(input("enter email address"))
    h = "@"
    h1 = "."
    le = len(s)
    for i in s:
        if i == h:
            print("PASS 1")
            break
            
    else:
        print("fail 1")
    
    for i in s:
        if i == h1:
            print("PASS 2")
            break
            
    else:
        print("fail 2")
    
    
    if le > 10:
        print("PASS 3")
        
            
    else:
        print("fail 3") 
    print("if all pass, address is valid, if fails => 1 then invalid ") 
caesar(email ="123@gmail.com")