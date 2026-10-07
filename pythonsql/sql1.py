import pymysql

connection=pymysql.connect(user="root",host="localhost",password="root",database="oneteam")

cursor=connection.cursor()

# cursor.execute("INSERT INTO courses(course_name,price,duration)VALUES('Data Analytics',35000,'5 months');")
def addCourse():
    course = input("Enter the course name: ")
    price = input("Enter the course price: ")
    duration = input("Enter the duration: ")

    cursor.execute(f"INSERT INTO courses(course_name,price,duration)VALUES('{course}','{price}','{duration}');")

    connection.commit()
    print(f"Course {course} added successfully")

def viewCourse():
    course_id = int(input("Enter course id: "))
    cursor.execute(f"SELECT * FROM courses WHERE id='{course_id}';")
    print(cursor.fetchone())

while True:
    print("1.Add Course\n2.View Course\n5.Exit")
    choice = int(input("What would you like to do?"))
    if choice == 1:
        count = int(input("How many courses do you wish to enter?\n"))
        for j in range(count):
            addCourse()
        continue
    if choice == 2:
        viewCourse()
        continue
    if choice ==5:
        print("Thank you.")
        break


