import pymysql

connection = pymysql.connect(user="root",host="localhost",password="root",database="oneteam")

cursor=connection.cursor()

from tkinter import *
window=Tk()

def addCourse():
    course = course_name.get()
    course_price=price.get()
    course_duration = duration.get()
    cursor.execute(f"INSERT INTO courses(course_name,price,duration) VALUES('{course}','{course_price}','{course_duration}');")
    connection.commit()
    print("Added successfully")
    course_name.delete(0,END)
    price.delete(0,END)

Label(window,text="Course Name").grid(row=0,column=0)

course_name=Entry(window)
course_name.grid(row=0,column=1)

Label(window,text="Price").grid(row=1,column=0)

price=Entry(window)
price.grid(row=1,column=1)

Label(window,text="Duration").grid(row=2,column=0)

duration=Entry(window)
duration.grid(row=2,column=1)

Button(window,text="Register",command=addCourse).grid(row=3,column=0,columnspan=2)

window.mainloop()