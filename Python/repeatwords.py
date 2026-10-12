s="The time for change is now. The time for progress is now. The time for unity is now."
print(s)
f={}
for k in s.lower().replace(".","").split():
    if k in f:
        f[k]+=1
    else:
        f[k]=1

for k,v in f.items():
    print(k,":", v)

rows = int(input("Enter the number of rows: "))

for i in range(1,rows+1):
    num=i
    a=rows-1
    print()
    for j in range(i):
        mat=i+j
        print(num,end=" ")
        num +=a
        a-=1