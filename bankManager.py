bank={}
print("-"*6,"BANK MANAGEMENT SYSTEM","-"*6)
print("MENU")
print("1. Create Account\n2. Deposit Money\n3. Withdraw Money\n4. View Account \n5. Exit\n","-"*36)

while True:
    option = int(input("What would you like to do?\n\n"))

    if option==1:
        # phone=int(input("Enter your phone number: "))
        # name=input("Enter your name: ")
        # age=int(input("Enter your age: "))
        # balance=int(input("Enter your initial deposit: "))
        bank[int(input("Enter your phone number: "))]=[input("Enter your name: "),int(input("Enter your age: ")),int(input("Enter your initial deposit: "))]
        # print(bank)
        # print(bank.keys())
        

    elif option==2:
        phoneCh=int(input("Enter your phone number: ")) 
        if phoneCh in bank.keys():
            deposit=int(input("Enter your deposit amount: "))
            bank[phoneCh][2]+=deposit
        else:
            print("Phone number not found.")
            
        # print(bank)
        
        

    elif option==3:
        phoneCh=int(input("Enter your phone number: "))
        if phoneCh in bank.keys():
            withdraw=int(input("Enter your withdraw amount: "))
            if withdraw > bank[phoneCh][2]:
                print("Insufficient balance")
                #continue
            else:
                bank[phoneCh][2]-=withdraw
        else:
            print("Phone number not found.")
        # print(bank)
        
    elif option==4:
        phoneCh=int(input("Enter your phone number: "))
        if phoneCh in bank.keys():
            print(f"""
            Name: {bank[phoneCh][0]}
            Age: {bank[phoneCh][1]}
            Phone number: {bank.keys()}
            Balance: {bank[phoneCh][2]}""")
        
    elif option == 5:
        break