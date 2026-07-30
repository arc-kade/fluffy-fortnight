s="Programming"
first=""
last=""
for i in range(4):
    first+=s[i]
print(first)

for i in range(len(s)-5,len(s)):
    last+=s[i]
print(last)
skip=""
for i in range(1,len(s),2):
    skip+=s[i]
print(skip)

hello = "Hello"
python = "Python"
print(hello +" "+python)
print("hi "*5)