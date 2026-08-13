import pickle
# students=[{"Name":"Abilash", "Age": 23},{"Name":"Naveen","Age":22}]
# with open("student.pkl","wb") as file:
#     pickle.dump(students,file)

# with open("student.pkl","rb") as file:
#     loadedStudents=pickle.load(file)
#     print(loadedStudents)

import math
# print(math.sqrt(25))
# from math import sqrt
# print(sqrt(144))

# import mymodule
# print(mymodule.add(5,8))

# from mymodule import(add,subtract)
# print(add(9,10))
# print(subtract(24,7))

# from mathoperations.mymodule import add
# print(add(11,10))
# def square(x):
#     return x*x
numbers=[1,2,3,4,5]
# squared = list(map(square,numbers))
# print(squared)

# def iseven(n):
#     return n%2==0
# evenNumbers=list(filter(iseven,numbers))
# print(evenNumbers)
# from functools import reduce
# def multiply(a,b):
#     return a*b
# product=reduce(multiply,numbers)
# print(product)


from functools import reduce
price = [100,200,300,400,500]
def applyDiscount(price):
    return price*0.9
def is_affordable(price):
    return price<350
def totalcost(a,b):
    return a+b

discountedPrices=list(map(applyDiscount,price))
afforablePrices=list(filter(is_affordable,price))
total=reduce(totalcost,afforablePrices)
print(total)