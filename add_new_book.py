import tkinter as t
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import StringVar, ttk
import interface_window
import os
global con, mycursor
import connections as c
con, mycursor = c.myconnections()


def insertdata(book_name, acc_no, no_of_copies, author_name, publisher_name, price,image_location):
        mycursor.execute("INSERT INTO book_detail_table"
                     "(book_name,acc_no,no_of_copies,author_name,publisher_name,price,image_location)"
                     "values('%s',%s,%s,'%s','%s',%s,'%s')"
             % (str(book_name), acc_no, no_of_copies, str(author_name), str(publisher_name), price, str(image_location)))
        con.commit()

def anb(top):

        top.destroy()  # here we can destroy the main window

        os.chdir("C:\\LibraryProject\\images\\background_images\\")  # this is use for change the directory
        root2 = t.Tk()   # here we can create window
        root2.geometry("1920x1080")  # Dimension of the add new book window
        root2.title("ADD NEW BOOK")  # title of the add new book
        root2.state('zoomed')
        root2.iconbitmap("Graphicloads-Colorful-Long-Shadow-Book.ico")  # through this we can set icon of the window
        screen_width = root2.winfo_screenwidth()  # by this we can get the width of the tkinter window
        screen_height = root2.winfo_screenheight()  # by this we can get the height of the tkinter window
        dim1 = str(screen_width)  # here we store the screen width of the tkinter window as a string in the dim1 variable
        dim2 = str(screen_height)  # here we store the screen height of the tkinter window as a string in the dim1 variable
        dim3 = "%sx%s" % (dim1, dim2)  # in the dim3 variable we set the dimension of the tkinter window
        root2.geometry(dim3)  # Dimension of the returning window

        l10 = t.Label(root2, text="HERE YOU CAN ADD THE BOOK INTO THE LIBRARY", font="Century 15 bold", fg="black")
        l10.place(x=350)

        def backbtn1():  # back button function

            root2.destroy()
            interface_window.mainwindow()

        anbwbtn1 = t.Button(root2, text=" HOME ", bg="black", fg="white", bd=2, command=backbtn1, font="Century 10 bold")
        anbwbtn1.place(x=600, y=28)

        l10 = t.Label(root2, text="(1). ACC NUMBER                 :", font="Century 15 bold", fg="black")
        l10.place(x=150, y=10)

        at1 = t.Entry(root2, width=25, font="Montserrat")
        at1.place(x=600, y=100)

        l1 = t.Label(root2, text="(2). BOOK NAME                   :", font="Century 15 bold", fg="black")
        l1.place(x=150, y=170)
        t1 = t.Entry(root2, width=25, font="Montserrat")
        t1.place(x=600, y=170)

        l21 = t.Label(root2, text="(3). NUMBER OF COPIES       :", font="Century 15 bold", fg="black")
        l21.place(x=150, y=230)
        t21 = t.Entry(root2, width=25, font="Montserrat")
        t21.place(x=600, y=230)

        l3 = t.Label(root2, text="(4). AUTHOR NAME               :", font="Century 15 bold", fg="black")
        l3.place(x=150, y=290)
        t3 = t.Entry(root2, width=25,font="Montserrat")
        t3.place(x=600, y=293)

        l4 = t.Label(root2, text="(5). PUBLISHER NAME          :", font="Century 15 bold", fg="black")
        l4.place(x=150, y=360)
        t4 = t.Entry(root2, width=25,font="Montserrat")
        t4.place(x=600, y=363)

        l5 = t.Label(root2, text="(6). PRICE                              :", font="Century 15 bold", fg="black")
        l5.place(x=150, y=440)
        t5 = t.Entry(root2, width=25, font="Montserrat")
        t5.place(x=600, y=443)

        def anb_img_set():  # set student image as a label in the window =  function

            l9 = t.Label(root2, text=" BOOK LABEL", font="Century 12 bold")
            l9.place(x=1000, y=60)

            x = t1.get()  # =  name of the book
            print(x)
            # below line of code  is used for open the file
        def call():
                root2.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                               filetypes=(("png files", "*.png"), ("all files", "*.*")))

                img = Image.open(root2.filename)  # used to open the image
                os.chdir("C:\\LibraryProject\\images\\book_label\\")  # used to change the directory

                width = 250  # width of the student image
                height = 200  # height of the student image
                # use one of these filter options to resize the image
                im2 = img.resize((width, height), Image.NEAREST)      # use nearest neighbour

                im2.save("%s.png" % at1.get())  # used to save the image

                img = ImageTk.PhotoImage(Image.open("%s.png" % at1.get()))  # used to open the image

                stn_img = t.Label(root2, image=img)  # stn_image = student image

                stn_img.place(x=950, y=100)

                root2.mainloop()

        def uploadcall():

            anb_detail_add_button = t.Button(root2, text="UPLOAD", command=call, font="Century 10 bold", width=18, bd=4)
            anb_detail_add_button.place(x=1000, y=330)

        lctn = "C:\\LibraryProject\\images\\book_label\\%s.png" % at1.get()

        def getdata():

            book_name = t1.get()
            acc_no = at1.get()
            no_of_copies = t21.get()
            author_name = t3.get()
            publisher_name = t4.get()
            price = t5.get()
            image_location = lctn
            messagebox.showinfo("Message", "Book is sucessfully added to the library")
            anb_img_set()
            uploadcall()

            insertdata(book_name, acc_no, no_of_copies, author_name, publisher_name, price, image_location)

        anbw_button = t.Button(root2, text=" ADD ", bg="blue", bd=2, fg="white", command=getdata, font="Century 12 bold")
        anbw_button.place(x=300, y=600)

        def backbtn():  # back button function

            root2.destroy()
            interface_window.mainwindow()

        # anbwbbtn = add new book window back button
        anbwbbtn = t.Button(root2, text="BACK ", bg="blue", fg="white", bd=2, command=backbtn, font="Century 11 bold")
        anbwbbtn.place(x=600, y=600)
        root2.mainloop()
