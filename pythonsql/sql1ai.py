import os
from decimal import Decimal, InvalidOperation
import pymysql
from pymysql import MySQLError


def create_connection():
    """Create and return a database connection."""
    return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),  # Note: parameter is 'password' or 'passwd'
        database=os.getenv("DB_NAME", "oneteam"),
        cursorclass=pymysql.cursors.DictCursor,  # Fixed capitalization: DictCursor
        autocommit=False,
    )


def add_course(connection):
    course = input("Enter the course name: ").strip()
    price_input = input("Enter the course price: ").strip()
    duration = input("Enter the duration: ").strip()

    if not course or not duration:
        print("Error: Course name and duration cannot be empty.\n")
        return

    try:
        price = Decimal(price_input)
    except InvalidOperation:
        print("Error: Invalid price format. Please enter a valid number.\n")
        return

    try:
        with connection.cursor() as cursor:
            query = "INSERT INTO courses (course_name, price, duration) VALUES (%s, %s, %s);"
            cursor.execute(query, (course, price, duration))
        connection.commit()
        print(f"Course '{course}' added successfully.\n")
    except MySQLError as err:
        connection.rollback()
        print(f"Database error while adding course: {err}\n")


def view_course(connection):
    try:
        course_id = int(input("Enter course ID: "))
    except ValueError:
        print("Error: Course ID must be an integer.\n")
        return

    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM courses WHERE id = %s;"
            cursor.execute(query, (course_id,))
            result = cursor.fetchone()

        if result:
            print(f"\nID: {result['id']}")
            print(f"Name: {result['course_name']}")
            print(f"Price: ${result['price']}")
            print(f"Duration: {result['duration']}\n")
        else:
            print(f"No course found with ID {course_id}.\n")
    except MySQLError as err:
        print(f"Database error: {err}\n")


def update_course(connection):
    try:
        course_id = int(input("Enter course ID: "))
    except ValueError:
        print("Error: Course ID must be an integer.\n")
        return

    new_name = input("Enter the new name for the course: ").strip()
    price_input = input("Enter the new price: ").strip()
    new_duration = input("Enter the new duration: ").strip()

    try:
        new_price = Decimal(price_input)
    except InvalidOperation:
        print("Error: Invalid price format. Please enter a valid number.\n")
        return

    try:
        with connection.cursor() as cursor:
            query = """
                UPDATE courses 
                SET course_name = %s, price = %s, duration = %s 
                WHERE id = %s;
            """
            rows_affected = cursor.execute(query, (new_name, new_price, new_duration, course_id))
        
        connection.commit()
        if rows_affected > 0:
            print(f"Course ID {course_id} updated successfully.\n")
        else:
            print(f"No course found with ID {course_id}.\n")
    except MySQLError as err:
        connection.rollback()
        print(f"Database error while updating course: {err}\n")


def delete_course(connection):
    try:
        course_id = int(input("Enter course ID: "))
    except ValueError:
        print("Error: Course ID must be an integer.\n")
        return

    try:
        with connection.cursor() as cursor:
            query = "DELETE FROM courses WHERE id = %s;"
            rows_affected = cursor.execute(query, (course_id,))
        
        connection.commit()
        if rows_affected > 0:
            print(f"Course ID {course_id} deleted successfully.\n")
        else:
            print(f"No course found with ID {course_id}.\n")
    except MySQLError as err:
        connection.rollback()
        print(f"Database error while deleting course: {err}\n")


def view_all_courses(connection):
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM courses;"
            cursor.execute(query)
            courses = cursor.fetchall()

        if courses:
            print("\n--- ALL COURSES ---")
            for course in courses:
                print(f"ID: {course['id']} | Name: {course['course_name']} | Price: ${course['price']} | Duration: {course['duration']}")
            print()
        else:
            print("No courses available.\n")
    except MySQLError as err:
        print(f"Database error: {err}\n")


def main():
    try:
        connection = create_connection()
    except MySQLError as err:
        print(f"Failed to connect to the database: {err}")
        return

    try:
        while True:
            print("=== COURSE MANAGEMENT SYSTEM ===")
            print("1. Add Course\n2. View Course\n3. Update Course\n4. Delete Course\n5. View All Courses\n6. Exit")

            try:
                choice = int(input("What would you like to do? "))
            except ValueError:
                print("Please enter a valid number.\n")
                continue

            if choice == 1:
                try:
                    count = int(input("How many courses do you wish to enter? "))
                    for _ in range(count):
                        add_course(connection)
                except ValueError:
                    print("Please enter a valid count integer.\n")
            elif choice == 2:
                view_course(connection)
            elif choice == 3:
                update_course(connection)
            elif choice == 4:
                delete_course(connection)
            elif choice == 5:
                view_all_courses(connection)
            elif choice == 6:
                print("Thank you. Exiting system.")
                break
            else:
                print("Invalid choice. Please select from 1 to 6.\n")
    finally:
        connection.close()


if __name__ == "__main__":
    main()