while True:
    e = int(input("Enter 5 to exit: "))
    if e==5:
        break
    a = int(input("Enter the first Number: "))
    ope = input("Enter your operator(+,-,*,/): ")
    b = int(input("Enter the second Number: "))
    
    if ope == "+":
        c = a+b
        print(a,"+",b,"=",c)
        continue
    elif ope == "-":
        c=a-b
        print(a,"-",b,"=",c)
        continue
    elif ope == "*":
        c=a*b
        print(a,"*",b,"=",c)
    elif ope == "/":
        c=a/b
        print(a,"/",b,"=",c)
    else:
        print("Invalid operator. (Use only +,-,*,/)")

    