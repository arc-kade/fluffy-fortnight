# a=[1,"Abilash",0.4]
# print(type(a))
# print(a[3])
# print(len(a)-1)
# print(a[1:])
# b=[]
# b.append(10)
# print(b)
# c=5
# b.append(c)
# print(b)
# a=[1,2,3,4,5]
# b=["a","b","c","d"]
# a.append(b)
# print(a)
# c=a+b
# print(c)
# b.insert(2,"e")
# print(b)
# a.extend(b)
# print(a)
# a.pop(1)
# print(a)
# print(b)
# b.remove("b")
# print(b)
# a.clear()
# print(a)
# c=["b","d","c","a"]
# print(sorted(c))
# d=[4,9,2,8,1,7,6]
# print(sorted(d))
# print(c.index("b"))
# print(d.count(1))
# d.reverse()
# print(d)
# list1=[]
# for i in d:
#     if i%2==0:
#         list1.append(i)
# print(list1)
# fruits=[["apple","grapes"],["orange","kiwi"],["dragonfruit","mango"]]
# print(fruits[0][0])
# print(fruits[1][1])
numbers=[10,8,20,11,5,2]
rev=[]
for i in range(len(numbers)-1,-1,-1):
    rev.append(numbers[i])
    
print(rev)

sor=[]
k=0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i]>numbers[j]:
            k=i
            i=j
            j=k        
        elif:
            sor.append(numbers[i])
print(sor)