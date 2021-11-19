inp = input("enter the type of credit card")

visa = ("visa")
master = ("master")
americanexp = ("american express")
discover = ("discover")

if (inp == visa):
    num = int(input("enter the credit card number"))
    
elif (inp == master):
    num = int(input("enter the credit card number"))
    
elif (inp == americanexp):
    num = int(input("enter the credit card number"))
    
elif (inp == discover):
    num = int(input("enter the credit card number"))


 
while (num > 0):
    od = num % 10
    num = num // 10
    ev = (num % 10)%2
    num = num // 10
    
    
     

    
     