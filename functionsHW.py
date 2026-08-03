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

# A recursive to find the power (base^exponent)
# def power(b,e):
#     if e==0:
#         return 1
#     else:
#         return b* power(b,e-1)
        
        
# a=int(input("Enter the base: "))
# b=int(input("Enter the exponent: "))
# c=power(a,b)
# print(c)
# print(a**b)

#A lambda function to find the square of a number
# x= int(input("Enter a number to output square: "))
# square = lambda x: x*x
# print(square(x))

#A lambda function to find the largest of 2 numbers
# m=int(input("Enter a number: "))
# n=int(input("Enter another number: "))
# larger= lambda a,b: a if a>b else b #no need for return function
# print(f"{larger(m,n)} is larger")

#A lambda function to filter only the even numbers in a list
# numbers=[1,2,3,4,5,6,7,8]
# filter = list(filter(lambda x:x%2==0,numbers))
# print(filter)

#A lambda function to map the squares of numbers in the list
# numbers=[1,2,3,4,5,6,7,8]
# squares = list(map(lambda x:x%2==0,numbers))
# print(squares)