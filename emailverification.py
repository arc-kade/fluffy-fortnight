import re
emails=[]
while True:
    mailpattern = r"^[A-Za-z.!/%&+-\=?^~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    email = input("Create an email address: ")
    if email.lower() == "no":
        break
    verification = re.fullmatch(mailpattern,email)
    if bool(verification)==True:
        if email in emails:
            print("Email already exists")
        else:
            print("Email address successfully created")
            emails.append(email)
    else:
        print("Invalid name for email address")
