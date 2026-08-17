bank={}
account=[]
print("_"*6,"BANK MANAGEMENT SYSTEM","_"*6)



while True:
    print("-"*12,"MENU","-"*12)
    print("1. Create Account\n2. Login \n3. Exit \n","_"*32)
    option = int(input("What would you like to do?\n\n"))

    if option==1:
        phone=int(input("Enter your phone number: "))
        if phone in bank.keys():
            print("Account already exists with this phone number.\n")
            continue
        if len((str(phone)))!=10:
            print("Invalid phone number\n")
        else:
            name=input("Enter your name: ")
            age=int(input("Enter your age: "))
            balance=int(input("Enter your initial deposit: "))
            bank[phone]=[name,age,balance]
            account=list(bank.items())
            print(f"\nBank account created.\nName:{name}\nAge:{age}\nPhone number:{phone}\nBalance:{balance}\n")
        # print(bank.keys())
        # print(bank)
        # print(account)
        continue

    if option==2:
        phoneCh=int(input("Enter your phone number: "))
        if phoneCh in bank.keys():
            while True:
                print("-"*12,"MENU","-"*12)
                print("1. Deposit\n2. Withdraw \n3. View Account \n4. Logout \n","_"*32)
                optionL = int(input("What would you like to do?\n\n"))

                if optionL == 1:
                    deposit=int(input("Enter your deposit amount: "))
                    bank[phoneCh][2]+=deposit
                    print(f"Amount {deposit} has been deposited. Total balance: {bank[phoneCh][2]}")
                    continue

                elif optionL == 2:
                    withdraw=int(input("Enter withdraw amount: "))
                    if withdraw>balance:
                        print("Insufficient balance.")
                        continue
                    elif withdraw<0:
                        print("Cannot withdraw a negative amount.")
                        continue
                    else:
                        bank[phoneCh][2]-=withdraw
                        print(f"Amount {withdraw} has been withdrawn. Total balance: {bank[phoneCh][2]}")
                        continue
                elif optionL == 3:
                    print(f"""-------------Bank details--------------- 
                    Name: {name}
                    Age: {age}
                    Phone number: {phoneCh}
                    Balance: {bank[phoneCh][2]} """)
                    continue

                elif optionL == 4:
                    confirm=input("Are you sure? Y/N: ")
                    if confirm.lower()=="y" or confirm.lower()=="yes" or confirm.lower=="confirm":
                        print("Logout confrimed")
                        break
                    else:
                        print("Logout cancelled.")
                        continue

                else:
                    print("Invalid option")
                    continue
        else:
            print("Bank account does not exist with this phone number.\n")
            continue

    
    elif option==3:
        confirm=input("Are you sure? Y/N: ")
        if confirm.lower()=="y" or confirm.lower()=="yes" or confirm.lower=="confirm":
            print("-"*32,"Thank you.","-"*32)
            break
        else:
            print("Logout cancelled.")
            continue
        
    else:
        print("Invalid option")
        # continue