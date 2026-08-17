# age=17                                    if statement
# if age>=18:
#     print("correct")  #true part
# print("Hello")

# age=17                                      #if-else statement
# if age>=18:
#     print("correct")  #true part
# else:
#     print("wrong")  #false part
# print("Hello")

# day=3
# if day==1:
#     print("Sunday")
# elif day==2:
#     print("Monday")
# elif day==3:
#     print("Tuesday")
# elif day==4:                                        #if and elif are the true parts
#     print("Wednesday")
# elif day==5:
#     print("Thursday")
# elif day==6:
#     print("Friday")
# elif day==7:
#     print("Saturday")
# else:                                               #else is the false part
#     print("Invalid day")

# age=19
# student=True
#                                                     #Nested if statement
# if age>=18:
#     if student:
#         print("Eligible to vote")
#     else:
#         print("Ineligible to vote. Reason: Not a student")
# else:
#     print("Ineligible to vote. Reason: underaged")


# if
number = int (input("Enter a number: "))
if number>50:
    print("The number entered is greater than 50")
# else:
#     print("The number entered is not greater than 50")


number = int(input("Enter another number: "))
if number%5==0:
    print("The number entered is divisible by 5")
# else:
#     print("The number is not divisible by 5")

age = int (input("Enter your age: "))
if age >= 18:
    print("You are legally an adult")
# else:
#     print("You are legally a minor")

num2= int(input("Enter a negative or non-negative number:  "))
if num2 < 0:
    print("Number entered is negative")
# else:
#     print("Number entered is greater than or equal to 0")

marks = int(input("Enter your marks (out of 100): "))
if marks > 90:
    print("Eligible for cutoff")
# else:
#     print("Ineligible for cutoff")

#if-else:

oddEven = int(input("Enter a number: "))
if oddEven%2==0:
    print("Number is even.")
else:
    print("The number is odd.")

posiNega = int(input("Enter a positive or negative number: "))
if posiNega > 0:
    print("Number is +ve.")
else:
    print("Number is -ve.")

canVote = int(input("Enter your age: "))
if canVote>=18:
    print("You can vote.")
else:
    print("You can't vote.")

isDiv = int(input("Enter any number: "))
if isDiv%3 == 0:
    print("The number is divisible by 3.")
else:
    print("Not perfectly divisible by 3.")

score = int(input("Enter your marks: "))
if score>=40:
    print("Pass.")
else:
    print("Fail.")

#nested if
posOdd = int(input("Enter any integer: "))
if posOdd>0:
    print("The number is positive.")
    if posOdd%2==0:
        print("The number is also even")
    else:
        print("The number is also odd")
else:
    print("The number is either -ve or 0.")

age2 = int(input("Enter age: "))
if age2>=18:
    if age2>=60:
        print("Age qualifies for senior citizen.")
    else:
        print("Age qualifies for adult.")
else:
    print("Age qualifies for minor.")

user1 = "testUser123"
password1 = "Password@123"

user = input("Enter your username: ")
if user == user1:
    password = input("Enter the password: ")
    if password == password1:
        print("Login successful. ")
    else:
        print("Incorrect password.")
else:
    print("Invalid username.")
    
marks= int(input("Enter your marks: "))
if marks >= 40:
    if marks >=75:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")

salary = int(input("Enter your salary: "))
experience = int(input("Enter your experience in years: "))
if salary >= 20000:
    if experience>=2:
        print("Eligible")
    else:
        print("Ineligible")
else:
    print("Ineligible")


#if-else ladder
marks = int(input("Enter the marks: "))
if marks >=90:
    print("A")
elif marks >=75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail.")

day = int(input("Enter a number representing a day: "))
if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursay")
elif day == 6:
    print("Friday")
elif day == 7:
    print("Saturday")
else:
    print("Day not valid.")

price = int(input("Enter the total price: "))
discount = 0
if price >=5000:
    print("20% discount applied.")
    discount = (price*20)/100
    price = price - discount
    print("Total price: ", price)
elif price >= 3000:
    print("10% discount applied.")
    discount = (price*10)/100
    price = price = discount
    print("Total price: ", price)
elif price >= 1000:
    print("5% discount applied.")
    discount = (price*5)/100
    price = price - discount
    print("Total price: ", price)
else:
    print("No discount applied.")
    print("Total price: ", price)

temp = int(input("Enter your temperature: "))
if temp > 35:
    print("Hot")
elif temp > 25:
    print("Warm")
elif temp > 15:
    print("Cool")
else:
    print("Cold")