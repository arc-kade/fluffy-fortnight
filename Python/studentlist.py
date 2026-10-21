import copy

SUBJECTS = 3
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

def read_name(prompt):
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Name cannot be empty")

def collect_students():
    studentCount = read_int("Enter the number of students: ", minimum=1)

    nameList=[]
    rollList=[]
    markList=[]

    for i in range (1,studentCount+1):
        print(f"\nStudent {i}")
        nameList.append(read_name("Name: "))
        while True:
            rollNumber = read_int("Enter the roll number: ", minimum=1)
            if rollNumber in rollList:
                print("Roll number already taken.")
            else:
                rollList.append(rollNumber)
                break
        student_marks = [
            read_int(f"Marks in subject {s} (0-100): ", minimum=0, maximum=100)
            for s in range(1, SUBJECTS+1)
        ]
        markList.append(student_marks)
    return nameList,rollList,markList

def show_dictionary(nameList, rollList):
    print("\n Roll Number -> Name (zip)")
    roll_name_dic = dict(zip(rollList,nameList))
    print(roll_name_dic)

def string_operations(nameList):
    print("\n String operations")
    upperName = [name.upper() for name in nameList]
    print("Upper case names: ",upperName)
    longName = [name for name in nameList if len(name)>5]
    print("Names longer than 5 characters: ",longName)
    a_names = [name for name in nameList if name and name[0].lower()=="a"]
    print("Names that start with the letter 'A': ",a_names)

def list_comprehension(nameList,rollList,markList):
    print("\nList comprehensions")
    highScoreres = [name for name, m in zip(nameList,markList) if sum(m)/len(m) > 75]
    print("Students with average marks > 75: ",highScoreres)
    evenRolls = [r for r in rollList if r%2==0]
    print("Even roll numbers: ",evenRolls)

def tuple_and_set(markList):
    print("\nTuple and set")
    first_marks = tuple(markList[0])
    print("First student's marks: ",first_marks)
    
    unique_marks = {m for student in markList for m in student }
    print("Unique marks for all students (set): ",unique_marks)

def copy_demo(markList):
    print("\n shallow copy vs deep copy")
    shallow = copy.copy(markList)
    deep = copy.deepcopy(markList)

    markList[0][0] +=1 
    print("(Changed first student's first mark in the original)\n")

    print("Original: ", markList)
    print("Shallow copy: ", shallow)
    print("Deep copy: ", deep)

def main():
    print("Student record management system\n")
    try:
        nameList, rollList, markList = collect_students()
    except (EOFError, KeyboardInterrupt):
        print("\nInput was cancelled. Exiting.")
        return
    except Exception as error:
        print(f"\nUnexpected error while reading input: {error}")
        return

    try:
        show_dictionary(rollList, nameList)
        string_operations(nameList)
        list_comprehension(nameList,rollList,markList)
        tuple_and_set(markList)
        copy_demo(markList)
    except Exception as error:
        print(f"\nSomething went wrong while processring the data: {error}")


if __name__=="__main__":
    main()