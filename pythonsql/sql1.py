import os
from decimal import Decimal, InvalidOperation

import pymysql
from pymysql import MySQLError

def create_connection():
    """Create and return a database connection."""
    return pymysql.connect(
        host = os.getenv("DB_HOST", "localhost"),
        user = os.getenv("DB_USER", "root"),
        passwd=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "oneteam"),
        cursorclass=pymysql.cursors.Dictcursor,
        # autocommit=False
    )


# cursor.execute("INSERT INTO courses(course_name,price,duration)VALUES('Data Analytics',35000,'5 months');")
def addCourse(connection):
    course = input("Enter the course name: ")
    price = input("Enter the course price: ")
    duration = input("Enter the duration: ")

    cursor.execute(f"INSERT INTO courses(course_name,price,duration)VALUES('{course}','{price}','{duration}');")

    connection.commit()
    print(f"Course {course} added successfully")

def viewCourse():
    try:
        course_id = int(input("Enter course id: "))
    except.ValueError:
        print("ERROR: Course ID must be an integer.")
        return
    try:
        
        cursor.execute(f"SELECT * FROM courses WHERE id='{course_id}';")
    print(cursor.fetchone())

def updateCourse(connection):
    course_id = int(input("Enter course id: "))
    newName = input("Enter the new name for the course: ")
    newPrice= float(input("Enter the new price: "))
    newDuration = input("Enter the new duration: ")
    cursor.execute(f"UPDATE courses SET course_name = '{newName}', price = {newPrice}, duration='{newDuration}' WHERE id='{course_id}';")
    connection.commit()
    print(f"Course ID:{course_id} updated successfully")

def deleteCourse(connection):
    course_id = int(input("Enter course id: "))
    cursor.execute(f"DELETE FROM courses WHERE id={course_id}")
    connection.commit()

while True:
    print("1.Add Course\n2.View Course\n3.Update Course\n4. Delete Course\n5.View All Courses \n6.Exit")
    choice = int(input("What would you like to do?\n"))
    if choice == 1:
        count = int(input("How many courses do you wish to enter?\n"))
        for j in range(count):
            addCourse()
        continue
    if choice == 2:
        viewCourse()
        continue
    if choice == 3:
        updateCourse()
        continue
    if choice == 4:
        deleteCourse()
    if choice == 5:
        cursor.execute(f"SELECT* FROM courses")
        print(cursor.fetchall())
    if choice ==6:
        print("Thank you.")
        break


