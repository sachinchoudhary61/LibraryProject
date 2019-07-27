import tkinter as tk
import os
from tkinter import messagebox

global con, mycursor
import connections as c
con, mycursor = c.myconnections()

def remove_book():

    os.chdir("C:\\LibraryProject\\images\\background_images\\")
    root9 = tk.Tk()  # this is used to create a window
    root9.title("Remove student")  # title of the window
    root9.geometry("600x200")  # dimension of the window
    root9.iconbitmap("Graphicloads-Colorful-Long-Shadow-Book.ico")  # here we set the icon of the window
    root9.configure(bg="RoyalBlue3")
    root9.resizable(0, 0)  # Don't allow resizing in the x or y direction
    rbwl1 = tk.Label(root9, text=" REMOVE BOOK ", font="Century 18 bold", fg="black",bg="RoyalBlue3")
    rbwl1.place(x=180)

    rbwl2 = tk.Label(root9, text="ACC NO. ", font="Century 15 bold", fg="black", bg="RoyalBlue3")
    rbwl2.place(x=100, y=70)

    rbwt1 = tk.Entry(root9, width=25, bd=5)
    rbwt1.place(x=260, y=70)

      # returning book window text one get = returning book window text one

    #query = "SELECT * FROM member_details WHERE unique_id=%s"%(rswt1g)
    #mycursor.execute(query)
    #data = mycursor.fetchall()

    #if rswt1g == data:

    def remove_book_fun():
            rbwt1g = rbwt1.get()
            root9.destroy()
            print("here : ", rbwt1g)
            query = "DELETE FROM book_detail_table WHERE acc_no = %s" % (rbwt1g)
             # here we destroy the remove book window
            messagebox.showinfo("Confirmation", "Hi,Book is removed sucessfully")  # after deletion of the book this message would be shown
            mycursor.execute(query)
            con.commit()  # this is used to make the changes

    rbwbtn1 = tk.Button(root9, text="CONFIRM", fg="white", bg="blue", font="Century 15 bold", command=remove_book_fun)
    rbwbtn1.place(x=220, y=150)  # confirm button to remove the book from the library
    #else:
           # messagebox.showinfo("Warning", "You have Entered wrong Student Unique ID")
    root9.mainloop()




