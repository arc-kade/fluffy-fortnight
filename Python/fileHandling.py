# File=open("bankManager.py","r")
# content=File.read()
# print(content)
# File.close()

# with open("loops.py","r") as file:
#     content=file.read()
#     print(content)

# with open("loops.py","r") as file:
    # content=file.readline()
    # print(content)
    # print(file.readline())
    # print(file.readline())


# with open("loops.py","r") as file:
#     content=file.readlines()
    # print(content)
    # for i in content:
    #     print(i)

with open("empty.py","a") as file:
    file.write("#Hello world\n")
    file.write("#Welcome to our world")

with open("bwm.jpg","rb") as sourceFile:
    content=sourceFile.read()

with open("destination.jpg","wb") as destinationFile:
    destinationFile.write(content)