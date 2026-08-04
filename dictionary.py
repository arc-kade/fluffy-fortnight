print("_______BANK MANAGEMENT SYSTEM_________")
print("MENU")
print("1. Create Account\n2. Deposit Money\n3. Withdraw Money\n4. View Account \n5. View Account \n6. Exit \n_____________________________________")

while True:
    option = int(input("What would you like to do?: "))

    if option==1:
        name=input("Enter your name: ")
        age=int(input("Enter your age: "))
        phone=int(input("Enter your phone number: "))
        balance=int(input("Enter your initial deposit: "))
        continue

    if option==2:
        phoneCh=int(input("Enter your phone number: "))
        deposit=int(input("Enter your deposit amount: "))
        balance=balance+deposit
        continue

    if option==3:
        phoneCh=int(input("Enter your phone number: "))
        withdraw=int(input("Enter withdraw amount: "))
        if withdraw>balance:
            print("Insufficient balance.")
        else:
            balance=balance-withdraw
    elif option == 6:
        break
