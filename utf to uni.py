

#x=(chr(int("20AC",16)))

#y=(ord("x"))

#p=(bin(y)[2:])

#o="20AC"

#l=["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110"]
#i = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
#if len(p) < 11:
#    print(p)
#    
#    q = p[::-1]
#    f = (q[:6] + "01" + q[6:] + "011")
#    print(f[::-1])
    
s = "U+263A"
l = ["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

x=s[2:]

l2 = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]



for i in x:
    print(l[l2.index(i) -1])