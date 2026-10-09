from tkinter import *
window=Tk()

Label(window,text="Course Name").grid(row=0,column=0)

course_name=Entry(window)
course_name.grid(row=0,column=1)

Label(window,text="Price").grid(row=1,column=0)

price=Entry(window)
price.grid(row=1,column=1)

Label(window,text="Duration").grid(row=2,column=0)

duration=Entry(window)
duration.grid(row=2,column=1)

Button(window,text="Register").grid(row=3,column=0,columnspan=2)

window.mainloop()