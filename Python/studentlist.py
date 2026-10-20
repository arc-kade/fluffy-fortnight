import copy


students={}

def read_int(prompt, minimum=None, maximum=None):
    """Keep asking until the user enters a valid whole number in range."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  Invalid input. Please enter a whole number.")
            continue
 
        if minimum is not None and value < minimum:
            print(f"  Value must be at least {minimum}.")
            continue
        if maximum is not None and value > maximum:
            print(f"  Value must be at most {maximum}.")
            continue
        return value

def collect_students():
    studentCount = read_int("Enter the number of students: ", minimum=1)

    nameList=[]
    rollList=[]
    markList=[]

    for i in range (1,studentCount+1):
        studentName = input("Enter the name of student :")
        nameList.append(studentName)
        rollNumber = int(input("Enter the roll number: "))
        rollList.append(rollNumber)
        mathMarks = int(input("Enter marks for Maths: "))
        # mathList.append(mathMarks)
        scienceMarks = int(input("Enter marks for Science: "))
        # scienceList.append(scienceMarks)
        engMarks = int(input("Enter marks for English: "))
        # engList.append(engMarks)
        markList.append([mathMarks,scienceMarks,engMarks])

    for name, roll, marks in zip(nameList,rollList,markList):
        students[roll]={
            "name":name, 
            "marks":marks
        }
       
    return


    upperName = [name.upper() for name in nameList]
    print(upperName)
    longName = [name for name in nameList if len(name)>5]
    print(longName)
    a_names = [name for name in nameList if name and name[0].lower()=="a"]
    print(a_names)

    highScoreres = [name for name, m in zip(nameList,markList) if sum(m)/len(m) > 75]
    print(highScoreres)
    evenRolls = [r for r in rollList if r%2==0]
    print(evenRolls)


    first_marks = tuple(markList[0])
    print(first_marks)
    unique_marks = {m for student in markList for m in student }
    print(unique_marks)

    shallow = copy.copy(markList)
    deep = copy.deepcopy(markList)

    markList[0][0] +=1 
    print("(Changed first student's first mark in the original)\n")

    print("Original: ", markList)
    print("Shallow copy: ", shallow)
    print("Deep copy: ", deep)

