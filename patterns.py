# n=int(input("Enter a number (Hollow square): "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i== n-1 or j == 0 or j==n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n=int(input("Enter a number (right half pyramid): "))
# for i in range(n):
#     for j in range(n):
#         if j<=i:
#             print("*",end=" ")
#     print()

# n=int(input("Enter a number (number increasing pyramid): "))
# for i in range(n):
#     for j in range(n):
#         if j<=i:
#             print(j+1,end=" ")
#     print()

# n=int(input("Enter a number (number increasing reverese pyramid): "))
# for i in range(n):
#     for j in range(n):
#         if j<=n-(i+1):
#             print(j+1,end=" ")
        
#     print()

# n=int(input("Enter a number (number changing pyramid): "))
# k=1
# for i in range(n):
#     for j in range(n):
#         if j<=i:
#             print(k,end=" ")
#             k+=1
#     print()
    

# n=int(input("Enter a number (number triangular): "))
# k=1
# for i in range(n):
#     print(" "*(n-i),end="")
#     for j in range(n):
#         if j<=i:
#             print(k,end=" ")
#     print()
#     k+=1

# n=int(input("Enter a number (zero-one pyramid): "))
# k=[0,1]
# for i in range(n):
#     for j in range(n):
#         if j<=i and j%2==0:
#             print(k[1],end=" ")
#         elif j<=i:
#             print(k[0], end=" ")
        
#     print()

# n=int(input("Enter a number (rhombus): "))
# k=0
# for i in range(n):
#     print(" "*(i),end="")
#     for j in range(n):
#         if j<=n:
#             print("*",end=" ")
            
#     print()
#     k+=1

# n=int(input("Enter a number (diamond): "))
# for i in range(n):
#     print(" "*(n-i),end="")
#     for j in range(n):
#         if j<=i:
#             print("*",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     print(" "*(n-(i-1)),end="")
#     for j in range(n-1,0,-1):
#         if j<=i:
#             print("*",end=" ") 
#     print()

n=int(input("Enter a number (left half pyramid): "))
for i in range(n):
    print(" "*(n),end="")
    for j in range(i):
        if j<=i:
            print("*",end=" ")
    print()
