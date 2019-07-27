import tkinter as t
import os
from tkinter import messagebox
global con, mycursor

import connections as c
con, mycursor = c.myconnections()

def remove_student():

    os.chdir("C:\\LibraryProject\\images\\background_images\\")  # here we change the directory, current to mension
    root8 = t.Tk()  # here we create the window
    root8.title("Remove student")  # here we set the title of the window
    root8.geometry("600x200")  # here we set the dimension of the window
    root8.iconbitmap("Graphicloads-Colorful-Long-Shadow-Book.ico")  # here we set the icon of the window
    root8.configure(bg="RoyalBlue3")  # here we set the background colour of the window
    root8.resizable(0, 0)  # Don't allow resizing in the x or y direction

    rswl1 = t.Label(root8, text=" REMOVE STUDENT ", font="Century 18 bold", fg="black",bg="RoyalBlue3")
    rswl1.place(x=150)

    rswl2 = t.Label(root8, text="Student Unique ID  : ", font="Century 15 bold", fg="black",bg="RoyalBlue3")
    rswl2.place(x=50, y=70)

    rswt1 = t.Entry(root8, width=30,bd=3)
    rswt1.place(x=330, y=73)

    #query = "SELECT * FROM member_details WHERE unique_id=%s"%(rswt1g)
    #mycursor.execute(query)
    #data = mycursor.fetchall()

    #if rswt1g == data:

    def remove_student_fun():
        rswt1g = rswt1.get()

        root8.destroy()
        messagebox.showinfo("Confirmation", "Hi,Student is removed sucessfully")

        mycursor.execute("DELETE FROM member_details WHERE unique_id = '%s'"%(rswt1g))
        con.commit()

    rswbtn1 = t.Button(root8, text="CONFIRM", fg="white", bg="blue", font="Century 15 bold", command=remove_student_fun)
    rswbtn1.place(x=220, y=150)
    #else:
           # messagebox.showinfo("Warning", "You have Entered wrong Student Unique ID")
    root8.mainloop()

