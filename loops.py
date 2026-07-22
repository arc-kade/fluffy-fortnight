# for i in range(10):
#     print(i+1)

# n = int(input("Enter a number: "))
# for i in range(n):
#     if i == 5:
#         break
#     print(i)
# name = "Welcome to Python"
# for i in name:
#     print(i,end=" ")
# print()

# list=['apple', 'banana', 'cherry', 'kiwi']
# for i in list:
#     for j in i:
#         print(j,end=" ")
#     print()
# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()

#for loop excercises:

# for i in range(1,50):
#     if i%2==0:
#         print(i)

# n = int(input("Enter any number: "))
# sum=0
# for i in range(n):
#     sum = sum+(i+1)
# print("sum of",n,"numbers is: ",sum)

# n = int(input("Enter a number: "))
# product = 0
# for i in range(11):
#     product = (i)*n
#     print(i,"x", n,"=",product)

# word = input("Enter any string of text: ")
# vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
# count = 0
# for i in word:
#     if i in vowels:
#         count +=1
# print("The string has", count, "vowels.")

# n=int(input("Enter a number: "))
# fact = 1
# for i in range(n):
#     fact*=(i+1)
# print("The factorial of", n, "is", fact)

# n=int(input("Enter a number: "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or n-1 or j == 0 or n-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

n=int(input("Enter a number (fibonacci series): "))
fib1=0
fib2=1
print(fib1,",",fib2,end=", ")
for i in range(n-3):
    fib3=fib1+fib2
    print(fib3,end=", ")
    fib1=fib2
    fib2=fib3
print(fib1+fib2)