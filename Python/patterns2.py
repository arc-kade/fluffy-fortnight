# n = int(input())
# for i in range(n+1):
#     b=i
#     t=n
#     p=1
#     for j in range(i+1):
#         if j<i:
#             print(b,end=" ")
#             b+=t-p
#             p+=1
#     print()

# n=int(input("How many numbers you wish to enter: "))
# order=[]
# custom=[]
# missing=[]
# for i in range(1,n+1):
#     e = int(input("Enter the number: "))
#     custom.append(e)

# for i in range(n):
#     for j in range(n-i-1):
#         if custom[j]>custom[j+1]:
#             custom[j],custom[j+1]=custom[j+1],custom[j]

# for i in range(custom[0],custom[n-1]+1):
#     order.append(i)

# for i in range(len(order)):
#     if order[i] not in custom:
#         missing.append(order[i])

# print("Missing numbers are: ", missing)

n=int(input("Enter starting number: "))
prime=[]
while len(prime)<3:
    i=2
    is_prime=True
    if n>2:
        is_prime=False

    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            is_prime=False
            break
    if is_prime:
        prime.append(n)
        n+=1
    else:
        
        n+=1


print(prime)

# rows=int(input("Enter the rows: "))
# col=int(input("Enter the columns: "))

# matrix=[]
# row=[]
# for i in range(rows):
#     print("Row ",i)
#     for j in range(col):
#         column=int(input("Enter the number: "))
#     row.append(column)
# matrix.append(row)

# print(matrix)

# s=input("Enter a string: ")
# st=s.strip().lower()
# print(st) 
# c={}
# for i in len(st):
#     if st[i] not in c:
#         count[]
#         c.append([])
#     else:

#     c[st[i]]=count

