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
def add():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    return a+b

result=add()
print(f"The sum is {result}")