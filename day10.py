# def digitalRoot(n):
#         while n >= 10:
#                 sum = 0
#                 while n > 0:
#                         sum += n%10
#                         n //= 10
#                 n = sum
#         return n
# a = int(input("Enter a any number (Digital root): "))
# print(f"The sum of digits from the number {a} till it is single digit is {digitalRoot(a)}")
print()



def fibonacci(n):
        if n<=1:
                return n
        else:
                return fibonacci(n-1) + fibonacci(n-2)
        

while True:
    n=int(input("Enter a positive integer for how many numbers in the fibonacci series you want: "))
    if n <= 0:
        print("Please enter a positive integer.")
        continue
    else:
           print(f"The first {n} Fibonacci numbers are: ")
           for i in range(n):
                if i < n-1:
                      print(fibonacci(i), end=", ")
                else :
                      print(fibonacci(i),end="")
           print()
           break