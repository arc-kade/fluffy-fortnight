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

# A function to take a list of numbers and find their sum and average.
# n=int(input("How many numbers do you want to enter?: "))
# def listing():
#     numbers =[]
#     for i in range(n):
#         num=int(input(f"Enter number {i+1}: "))
#         numbers.append(num)
#     return numbers
# r=listing()        
# def sumAvg(numbers):
#     if not numbers:
#         return 0, 0.0
#     total_sum=sum(numbers)
#     avg= total_sum/len(numbers)
#     print(total_sum)
#     print(avg)
#     print()
    

# sumAvg(r)

# Write a recursive function to find the factorial of a given number.
# n = int(input("Enter a number: "))
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(f"The factorial of {n} is {factorial(n)}")

#Write a recursive function to calculate the sum of the first n natural numbers.

# n = int(input("Enter a number to find the sum of their natural numbers: "))
# def ap(n):
#     if n==0:
#         return 0
#     else:
#         m=n+ap(n-1)
#         return m
    
# print(ap(n))

# Write a recursive function to print the Fibonacci series up to the nth term.
# n = int(input("How many terms of the Fibonacchi series?: "))
# fibo = []
# def fib(n):
    
#         if n<=1:
#             return n
#         else:
#             return fib(n-1) + fib(n-2)
        

# for i in range(n+1):
#     fibo.append(fib(i))
    
# print(f"Fibonacchi series up to {n} terms: {fibo}")

# Write a recursive function to reverse a given string.
# s=input("Enter any string: ")
# r=[]
# # print (s[len(s)-1])
# def reverse(s):
#     # for i in s:
#     if len(s) <=1:
#         return s
#     else:
#         return reverse(s[1:])+s[0]
        
# print(reverse(s))

#A recursive function to calculate the power of a number (base^exponent)
# def exp(a,b):
#     return a**b

# n=int(input("Enter the base: "))
# m=int(input("Enter the power: "))
# print(f"The {m}th power of {n} is: {exp(m,n)}")