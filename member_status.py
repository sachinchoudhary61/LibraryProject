import tkinter as t
import os
from tkinter import messagebox
import interface_window
global con, mycursor
import connections as c
con, mycursor = c.myconnections()

def vmsw(top):

    top.destroy()
    os.chdir("C:\\LibraryProject\\images\\background_images\\")
    root6 = t.Tk()
    screen_width = root6.winfo_screenwidth()  # by this we can get the width of the tkinter window
    screen_height = root6.winfo_screenheight()  # by this we can get the height of the tkinter window
    dim1 = str(screen_width)  # here we store the screen width of the tkinter window as a string in the dim1 variable
    dim2 = str(screen_height)  # here we store the screen height of the tkinter window as a string in the dim1 variable
    dim3 = "%sx%s" % (dim1, dim2)  # in the dim3 variable we set the dimension of the tkinter window
    root6.geometry(dim3)  # Dimension of the returning window
    root6.iconbitmap("Graphicloads-Colorful-Long-Shadow-Book.ico")
    root6.title("Borrowing Process")
    root6.configure(bg="seagreen1")
    root6.state('zoomed')
    vmswl1 = t.Label(root6, text="HERE YOU CAN CHECK MEMBER STATUS:", font="Century 15 bold", fg="black", bg="RoyalBlue3")
    vmswl1.place(x=500)

    vmswl2 = t.Label(root6, text="STUDENT UNIQUE ID:", font="Century 15 bold", fg="black", bg="RoyalBlue3")
    vmswl2.grid(row=1, column=0, padx=100, pady=60)

    vmswt1 = t.Entry(root6, width=40, bd=3)
    vmswt1.grid(row=2, column=0, padx=100, pady=1)

    def backbtn1():  # back button function

        root6.destroy()
        interface_window.mainwindow()

    vmsmwbtn1 = t.Button(root6, text=" HOME ", bg="black", fg="white", bd=2, command=backbtn1, font="Century 10 bold")
    vmsmwbtn1.place(x=700, y=28)

    def mswdf():

        mstg = vmswt1.get()

        if len(mstg) > 0:

            query = "SELECT * FROM member_details WHERE unique_id='%s'"%(mstg)
            mycursor.execute(query)
            data = mycursor.fetchall()

            #if bpt0g in data:
            for i in data:
                vmswl_3 = t.Label(root6, text="STUDENT DETAILS", font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl_3.grid(row=3, column=1, pady=20, padx=80, sticky=t.W)

                vmswl3 = t.Label(root6, text="(1).NAME                "
                                             "                        "
                                             ":", font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl3.grid(row=4, column=0, pady=20, padx=80, sticky=t.W)

                vmswl4 = t.Label(root6, font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl4.configure(text=i[1])
                vmswl4.grid(row=4, column=1)

                vmswl5 = t.Label(root6, text="  (2).FATHER NAME                     "
                                             "   :", font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl5.grid(row=5, column=0, pady=10, padx=70, sticky=t.W)

                vmswl6 = t.Label(root6, font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl6.configure(text=i[2])
                vmswl6.grid(row=5, column=1, padx=5, pady=10)

                vmswl7 = t.Label(root6, text=" (3).UNIVERSITY ROLL NO.          :     ", font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl7.grid(row=6, column=0, pady=10, padx=75, sticky=t.W)

                vmswl8 = t.Label(root6, font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl8.configure(text=i[3])
                vmswl8.grid(row=6, column=1, padx=20, pady=10)

                vmswl9 = t.Label(root6, text="     (4).STUDENT EMAIL-ID             "
                                             "  : ", font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl9.grid(row=7, column=0, pady=10, padx=55, sticky=t.W)

                vmswl10 = t.Label(root6, font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl10.configure(text=i[4])
                vmswl10.grid(row=7, column=1, padx=20, pady=10)

                vmswl11 = t.Label(root6, text="(5).SEMESTER                     "
                                             "           :", font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl11.grid(row=8, column=0, pady=10, padx=80, sticky=t.W)

                vmswl12 = t.Label(root6, font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl12.configure(text=i[5])
                vmswl12.grid(row=8, column=1, padx=20, pady=10)

                vmswl13 = t.Label(root6, text="(6).ENGG. BRANCH        "
                                             "                :", font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl13.grid(row=9, column=0,pady=10, padx=80, sticky=t.W)

                vmswl14 = t.Label(root6, font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl14.configure(text=i[6])
                vmswl14.grid(row=9, column=1, padx=20, pady=10)

                vmswl15 = t.Label(root6, text="(7).ADDRESS        "
                                             "                    "
                                             "       :", font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl15.grid(row=10, column=0, pady=10, padx=80, sticky=t.W)

                vmswl16 = t.Label(root6, font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl16.configure(text=i[7])
                vmswl16.grid(row=10, column=1, padx=20, pady=10)

                vmswl17 = t.Label(root6, text="(8).MOBILE NO.          "
                                             "                 "
                                             "   :", font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl17.grid(row=11, column=0, pady=10, padx=80, sticky=t.W)

                vmswl18 = t.Label(root6, font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl18.configure(text=i[8])
                vmswl18.grid(row=11, column=1, padx=20,pady=10)

                vmswl19 = t.Label(root6, text="(9).D.O.B                 "
                                             "                          "
                                             ":", font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl19.grid(row=12, column=0, pady=10, padx=80, sticky=t.W)

                vmswl20 = t.Label(root6, font="Century 12 bold", fg="black",bg="RoyalBlue3")
                vmswl20.configure(text=i[9])
                vmswl20.grid(row=12, column=1, padx=20,pady=10)

                vmswbtn3 = t.Button(root6, text="EXIT", font="Century 15 bold", fg="white", bg="blue", command=root6.destroy)
                vmswbtn3.grid(row=13, column=1, padx=20, pady=30)
        else:
            messagebox.showinfo("Warning", "Insert ACC no. ")

    vmswbtn2 = t.Button(root6, text="CLICK", font="Century 8 bold", fg="blue", command=mswdf)
    vmswbtn2.grid(row=2, column=1)
    root6.mainloop()

