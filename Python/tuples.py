# variable=("a",1,"b","c",3.6,"Python")
# print(variable)
# print(variable[0]) #[-1] prints the last element in the tuple
# b=()
# print(type(b))
# b=tuple()
# print(type(b))
# print(1 in variable)
# print(variable.count("b"))
# print(variable.index(3.6))
# c=(10,11,12,13)
# print(variable+c)


# emptyset=set()
# myset={"apple","banana","cherry","Apple"}
# print(myset)
# for i in myset:
#     print(i)
# myset.add("orange")
# print(myset)
# myset.remove("kiwi")
# print(myset)
# myset.discard("kiwi")
# print(myset)
# set1={1,2,3}
# set2={3,4,5}
# print(set1|set2) #intersection
# print(set1&set2) #union
# print(set1-set2) #differrence
# print(set1^set2) #symmetric difference
# seta={1,2}
# setb={1,2,3}
# print(seta.issubset(setb))
# print(setb.issuperset(seta))
import copy
originalList=[1,2,[3,4]]
shallowCopiedList=copy.copy(originalList)
# shallowCopiedList[1]=99
# print(originalList)
# print(shallowCopiedList)

# deepCopied=copy.deepcopy(originalList)
# deepCopied[1]=99
# print(originalList)
# print(deepCopied)
# a=3
# b=0
# c=a/b
# print(c)
try:
    a=3
    b=0
    c=a/b
    print(c)
except Exception as e:
    print(e)
finally:
    print("This will always execute")