import re
# pattern = r"hello"
# text = "Hello world"
# matching = re.match(pattern,text)
# print(bool(matching))

# pattern=r"world"
# text = "Hello world"
# search = re.search(pattern,text)
# print(bool(search))

# pattern = r"\d+"
# text = "order 5 laptop, 10 desktop, 15 keyboard"
# matches = re.findall(pattern,text)
# print(matches)

# text="The sky is blue"
# newText=re.sub(r"blue","red",text)
# print(newText)

# pattern = r"^Hello"
# text ="Abilash Hello world"
# result = re.search(pattern,text)
# print(result)

# pattern = r"Hello$"
# text ="Abilash Hello world Hello"
# result = re.search(pattern,text)
# print(result)

text = "python_123"
result=re.findall(r"[a-zA-z0-9_]",text)
print(result)

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