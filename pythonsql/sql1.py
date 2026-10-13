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
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False
    )


# cursor.execute("INSERT INTO courses(course_name,price,duration)VALUES('Data Analytics',35000,'5 months');")
def addCourse(connection):
    course = input("Enter the course name: ").strip()
    price = input("Enter the course price: ").strip()
    duration = input("Enter the duration: ").strip()

    if not course or not duration:
        print("Error: Course name and duration cannot be empty.\n")
        return

    try:
        price = Decimal(price_input)
    except InvalidOperation:
        print("Invalid operation. Please enter in number format\n")
        return

    try:
        with connection.cursor as cursor:
            cursor.execute(f"INSERT INTO courses(course_name,price,duration)VALUES('{course}','{price}','{duration}');")
        connection.commit()
    except MySQLError as err:
        connection.rollback()
        print(f"Database error while adding course {err}")

    # cursor.execute(f"INSERT INTO courses(course_name,price,duration)VALUES('{course}','{price}','{duration}');")

    # connection.commit()
    # print(f"Course {course} added successfully")

def viewCourse(connection):
    try:
        course_id = int(input("Enter course id: "))
    except ValueError:
        print("ERROR: Course ID must be an integer.")
        return
    try:
        with connection.cursor as cursor:
            cursor.execute(f"SELECT * FROM courses WHERE id='{course_id}';")
            result = cursor.fetchone()

        if result:
            print(f"\nID: {result['id']}\n")
            print(f"COURSE NAME: {result['course_name']}\n")
            print(f"DURATION: {result['duration']}\n")
            print(f"PRICE: {result['price']}\n")

        else:
            print(f"No course found with ID {course_id}.\n")

    except MySQLError as err:
            print(f"Database error: {err}\n")

UPDATABLE_FIELDS=("course name","price","duration")

def updateCourse(connection):
    try:
        course_id = int(input("Enter course id: "))
    except ValueError:
            print("Course ID must be an integer.\n")
            return
    try:
        with connection.cursor as cursor:
            cursor.execute(f"SELECT * FROM courses WHERE id='{course_id}';")
            row = cursor.fetchone()
            if row is none:
                print(f"No course found with ID {course_id}.")
                return
            
            udata = input(f"What do you want to update from {cursor.fetchone()}?\n")

            
    
    

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


