# def greet():
#     print("Hello, ")

# greet()
# greet()
# def greet():
#     return ("Hello, Abilash")
# # print(greet())
# a=greet()
# print(a)

# def add(a):
#     b=10
#     return a+b

# result=add(5)
# print(result)
# def add(p,q):
#     return p+q

# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# result=add(a,b)
# print(f"The sum is: {result}")

# def evenNumbers(a):
#     i=0
#     print(f"Set of even numbers from {i} to {a}: ",end="")
#     while i<=a:
#         print(i,end=", ")
#         i+=2

# n=int(input("Enter any number: "))
# set=evenNumbers(n)

#1. with arguments with return type:
# def add(a,b):
#     a=int(input("Enter a number: "))
#     b=int(input("Enter another number: "))
#     return a+b
# p=0
# q=0
# result=add(p,q)
# print(result)

# 2. With argument without return type:
# def add(a,b):
#     a=int(input("Enter a number: "))
#     b=int(input("Enter a 2nd number: "))
#     print(f"The sum is {a+b}")

# p=0
# q=0
# add(p,q)

# 3. Without argument without return type:
# def add():
#     a=int(input("Enter a number: "))
#     b=int(input("Enter a 2nd bumber: "))
#     print(f"The sum is {a+b}")

# 4. Without argument with return type:
# def add():
#     a=int(input("Enter the first number: "))
#     b=int(input("Enter the second number: "))
#     return a+b

# result=add()
# print(f"The sum is {result}")

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))

# def ap(n):
#         if n==0:
#             return 0
#         else:             
#             return n+ap(n-1)

# a=int(input("Enter a number to find the sum of numbers from 0 to n: "))
# print(ap(a))

# add=lambda a,b:a+b
# print(add(2,3))

# numbers=[1,2,3,4,5]
# evenNumbers=list(filter(lambda x:x%2==0,numbers))
# print(evenNumbers)

# numbers=[1,3,2]
# sortedNumbers=sorted(numbers,key=lambda x:x)
# print(sortedNumbers)
# print(sortedNumbers[0])
#Functuions

# def oddEven():
#     a=int(input("Enter any number to determine whether it is odd or even: "))
#     if a%2==0:
#         print(f"{a} is an even number.")
#     else:
#         print(f"{a} is an odd number.")

# oddEven()

# def largest(a,b,c):
#     if a > b:
#         if a > c:
#             print(f"{a} is the largest among {a}, {b}, and {c}.")
#         else:
#             print(f"{c} is the largest among {a}, {b}, and {c}.")
#     else:
#         if b>c:
#             print(f"{b} is the largest among {a}, {b}, and {c}.")
#         else:
#             print(f"{a} is the largest among {a}, {b}, and {c}.")

# l=int(input("Enter the first number: "))
# m=int(input("Enter the second number: "))
# n=int(input("Enter the third number: "))
# largest(l,m,n)

# def vowelsCount(s):
#     count = 0
#     vowels=["a","e","i","o","u","A","E","I","O","U"]
#     for i in s:
#         if i in vowels:
#             count+=1
#     return count

# s = input("Enter a string of text: ")
# print(f"The string contains {vowelsCount(s)} vowels")

# def fact(n):
#     if n < 0:
#         print("No -ve numbers.")
#     result=1
#     for i in range(1,n+1):
#         result *=i
#     return result
# n=int(input("Enter a number to find the factorial of: "))
# print(fact(n))

def listing():
    numbers =[]
    while True:
        c=input("Enter a number or type \"no\" to exit: ")
        if c == "no" or c == "No":
            break
        numbers.append(int(c))
        return numbers



