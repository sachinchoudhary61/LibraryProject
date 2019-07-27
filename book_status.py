import os
import tkinter as t
import os
import interface_window
from tkinter import messagebox
global con, mycursor
import connections as c
con, mycursor = c.myconnections()



def bsw(top):

    top.destroy()
    os.chdir("C:\\LibraryProject\\images\\background_images\\")
    root5 = t.Tk()
    root5.iconbitmap("Graphicloads-Colorful-Long-Shadow-Book.ico")
    root5.title("Borrowing Process")
    root5.configure(bg="RoyalBlue3")
    root5.state('zoomed')
    screen_width = root5.winfo_screenwidth()  # by this we can get the width of the tkinter window
    screen_height = root5.winfo_screenheight()  # by this we can get the height of the tkinter window
    dim1 = str(screen_width)  # here we store the screen width of the tkinter window as a string in the dim1 variable
    dim2 = str(screen_height)  # here we store the screen height of the tkinter window as a string in the dim1 variable
    dim3 = "%sx%s" % (dim1, dim2)  # in the dim3 variable we set the dimension of the tkinter window
    root5.geometry(dim3)  # Dimension of the returning window

    bswl1 = t.Label(root5, text="HERE YOU CAN CHECK BOOK STATUS:", font="Century 15 bold", fg="black",bg="RoyalBlue3")
    bswl1.place(x=500)

    bswl2 = t.Label(root5, text="ACC NUMBER:", font="Century 15 bold", fg="black", bg="RoyalBlue3")
    bswl2.grid(row=2, column=0, padx=100, pady=40)

    bswt1 = t.Entry(root5, width=40, bd=5)
    bswt1.grid(row=3, column=0, padx=100, pady=5)

    def backbtn1():  # back button function

        root5.destroy()
        interface_window.mainwindow()

    vbswbtn1 = t.Button(root5, text=" HOME ", bg="black", fg="white", bd=2, command=backbtn1, font="Century 10 bold")
    vbswbtn1.place(x=700, y=28)

    def bswdf():
        bstg = bswt1.get()
        if len(bstg) > 0:

            query = "SELECT * FROM book_detail_table WHERE acc_no='%s'"%(bstg)
            mycursor.execute(query)
            data = mycursor.fetchall()

            #if bpt0g in data:
            for i in data:
                bswl3 = t.Label(root5, text="(1).BOOK NAME                      :", font="Century 12 bold", fg="black",bg="RoyalBlue3")
                bswl3.grid(row=4, column=0, pady=20, padx=80, sticky=t.W)

                bswl4 = t.Label(root5, font="Century 12 bold", fg="black",bg="RoyalBlue3")
                bswl4.configure(text=i[0])
                bswl4.grid(row=4, column=1)

                bswl5 = t.Label(root5, text="  (2).NUMBER OF STOCKS      :", font="Century 12 bold", fg="black",bg="RoyalBlue3")
                bswl5.grid(row=5, column=0, pady=10, padx=70, sticky=t.W)

                bswl6 = t.Label(root5, font="Century 12 bold", fg="black",bg="RoyalBlue3")
                bswl6.configure(text=i[2])
                bswl6.grid(row=5, column=1, padx=5, pady=10)

                bswl7 = t.Label(root5, text=" (3).AUTHOR NAME                :", font="Century 12 bold", fg="black",bg="RoyalBlue3")
                bswl7.grid(row=6, column=0, pady=10, padx=75, sticky=t.W)

                bswl8 = t.Label(root5, font="Century 12 bold", fg="black",bg="RoyalBlue3")
                bswl8.configure(text=i[3])
                bswl8.grid(row=6, column=1, padx=20, pady=10)

                bswdl9 = t.Label(root5, text="     (4).PUBLISHER NAME           : ", font="Century 12 bold", fg="black", bg="RoyalBlue3")
                bswdl9.grid(row=7, column=0, pady=10, padx=55, sticky=t.W)

                bswl10 = t.Label(root5, font="Century 12 bold", fg="black", bg="RoyalBlue3")
                bswl10.configure(text=i[4])
                bswl10.grid(row=7, column=1, padx=20, pady=10)

                bswl11 = t.Label(root5,text="(5).PRICE.(INR)                      :", font="Century 12 bold", fg="black", bg="RoyalBlue3")
                bswl11.grid(row=8,column=0,pady=10, padx=80, sticky=t.W)

                bswl12 = t.Label(root5, font="Century 12 bold", fg="black",bg="RoyalBlue3")
                bswl12.configure(text=i[5])
                bswl12.grid(row=8, column=1, padx=20, pady=10)

                bswbtn3 = t.Button(root5, text="EXIT", font="Century 15 bold", fg="white", bg="blue", command=root5.destroy)
                bswbtn3.grid(row=9, column=1, padx=20, pady=50)

        else:
            messagebox.showinfo("Warning", "Insert ACC no. ")

    bswbtn2 = t.Button(root5, text="CLICK", font="Century 10 bold", fg="blue", command=bswdf)
    bswbtn2.grid(row=3, column=1)
    root5.mainloop()
