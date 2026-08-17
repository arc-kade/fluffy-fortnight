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
# numbers=[10,8,20,11,5,2]
# rev=[]
# for i in range(len(numbers)-1,-1,-1):
#     rev.append(numbers[i])
    # rev=[numbers[i]]
    
# print(rev)
# 
# print(rev)
# sor=[]
# k=0
# for i in range(len(numbers)):
#     for j in range(len(numbers)):
#         if numbers[i]<numbers[j]:
#             numbers[i],numbers[j]=numbers[j],numbers[i]
#         else:
#             numbers[i],numbers[j]=numbers[i],numbers[j]
            
# print(numbers)


# numbers=[3,8,10,45,12,17,0,78]
# print(max(numbers))
# print(min(numbers))

# squares=[]
# for x in range(5):
#     squares.append(x**2)
# print(squares)

# squares=[x**2 for x in range(5)]
# print(squares)

# numbers=[x for x in range(10)]
# print(numbers)

# evenNumbers=[x for x in range(10) if x%2==0]
# print(evenNumbers)
# matrix=[[x for x in range(3)] for y in range(3)]
# print(matrix)

# n=[[1,2],[3,4],[5,6]]
# flat=[num for sublist in n for num in sublist]
# print(flat)
# vowels=[i for i in "Hello world" if i in "aeiou"]
# print(vowels)

# list1=[1,2,3,4,5]
# print(list1[2])
# list1[2]=10
# print(list1)
# string1="hello world"
# print(string1[4])
# a="Hello \tworld"
# print(a)

# word="Python programming"
# print(word[-1])
# first_word="fullstack"
# print(first_word + word)
# print(word * 3)
# print(len(word))
# text= "python is Fun"
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())
# print(text.swapcase())
# word="  Hello world "
# print(word.strip())
# print(word.lstrip())
# print(word.rstrip())
# text="I love python, python is awesome"
# print(text.find("python"))
# print(text.rfind("python"))
# print(text.replace("python","coding"))
# sentence= "Python is fun to learn."
# words= sentence.split()
# print(words)
# joined = "-".join(words)
# print(joined)

# print("Hello@123".isalnum())
# print("123".isdigit())
# print("123".isalpha())
# print(" ".isspace())
# print("Hello".startswith("H"))
# print("Hello".endswith("o"))