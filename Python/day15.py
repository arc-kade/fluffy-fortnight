def pyramid_star(n):
    for i in range (1,n):
        print(" "*(n-i),end="")
        for j in range (i):
            print("*",end=" ")
        print()



def inverted_number(n):
    for i in range(n,0,-1):
        for j in range (i,0,-1):
            print(j,end="")
        print()
    print()


def natural_sum(n):
    if n==1:
        return 1
    else:
        return n + natural_sum(n-1)
    print()

while True:
    print("What would you like to do?")
    print("1. Star Pyramid\n2. Inverted Number Right Pyramid\n3. Natural Sum\n4. Power of a number\n5.Exit")
    p = int(input("Enter your option (1-5): "))

    if p == 1:
        a=int(input("Enter a number: "))
        pyramid_star(a)
        continue
    elif p == 2:
        b=int(input("Enter a number: "))
        inverted_number(b)
        continue
    elif p == 3:
        c=int(input("Enter the number for natural sums: "))
        print(natural_sum(c))
        continue
    elif p == 4:
        power = lambda a,b: a**b
        f = int(input("Enter base: "))
        g = int(input("Enter power: "))
        print(power(f,g))
        continue
    elif p == 5:
        break
    else:
        print("Invalid option.")
        continue