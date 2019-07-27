import tkinter as t  # creates ui window for the user
import tkinter as tk  #  import tkinter library for genrating ui for the user
from PIL import Image, ImageTk  # used to import the photo in the background

import add_new_member  # import add new member module that was present in another tab of this project to run in this module
import add_new_book  # import add new book that was present in another tab of this project to run in this module
import borrowing_process  # import borrowing process module that was present in another tab of this project to run in this module
import returning_book  # import returning book  module that was present in another tab of this project to run in this module
import book_status  # import book status module that was present in another tab of this project to run in this module
import member_status  # import member status  module that was present in another tab of this project to run in this module
import remove_student  # import add remove student  module that was present in another tab of this project to run in this module
import remove_book   # import remove book module that was present in another tab of this project to run in this module
import os  # used for change  the directory
import time
import webbrowser

def mainwindow():  # project main window function
    os.chdir("C:\\LibraryProject\\images\\background_images\\")  # here we shift the current directory into the projrct directory
    top = tk.Tk()  # with the help of this we can create a window
    screen_width = top.winfo_screenwidth()  # by this we can get the width of the tkinter window
    screen_height = top.winfo_screenheight()  # by this we can get the height of the tkinter window
    dim1 = str(screen_width)  # here we store the screen width of the tkinter window as a string in the dim1 variable
    dim2 = str(screen_height)  # here we store the screen height of the tkinter window as a string in the dim1 variable
    dim3 = "%sx%s" % (dim1, dim2)  # in the dim3 variable we set the dimension of the tkinter window
    top.geometry(dim3)  # Dimension of the returning window

    top.iconbitmap("Graphicloads-Colorful-Long-Shadow-Book.ico")  # used to display the icon in the window
    top.title("LIBRARY MANGEMENT SYSTEM")
    intdim1 = int(dim1)
    print(intdim1)
    intdim2 = int(dim2)
    image_1 = Image.open("librarypic11.jpg")  # used for open the image
    image1 = image_1.resize((intdim1, intdim2), Image.ANTIALIAS)
    background_image = ImageTk.PhotoImage(image1)  # tk.Label = tk is the window & we insert label on the window
    background = tk.Label(image=background_image)  # set background image as label in the main window
    background.pack(fill=tk.BOTH, expand=tk.YES)  # used to fill the image in the whole window

    b1 = tk.Button(background, text="Add New Student", command=lambda: add_new_member.anm(top), fg="white", font="Century 12 bold", bg="black", width=18,bd=4)
    b1.place(y=150, x=10)                  # we can't call function directly so we use lamda: module name.mainfuntion of that module

    b2 = tk.Button(background, text="Add New Book", command=lambda: add_new_book.anb(top), width=18, fg="white", font="Century 12 bold", bg="black",bd=4)
    b2.place(y=205, x=10)

    b3 = tk.Button(background, text="Borrowing Process", command=lambda: borrowing_process.bp(top), width=18, fg="white", font="Century 12 bold", bg="black",bd=4)
    b3.place(y=260, x=10)

    b4 = tk.Button(background, text="Returning Process", command=lambda: returning_book.rpw(top), width=18, fg="white", font="Century 12 bold", bg="black",bd=4)
    b4.place(y=315, x=10)

    b5 = tk.Button(background, text="View Member Status", command=lambda: member_status.vmsw(top), width=18, fg="white", font="Century 12 bold", bg="black",bd=4)
    b5.place(y=370, x=10)

    b6 = tk.Button(background, text="View Book Status", command=lambda: book_status.bsw(top), width=18, fg="white", font="Century 12 bold", bg="black",bd=4)
    b6.place(y=425, x=10)

    b7 = tk.Button(background, text="Remove Student ", command=lambda: remove_student.remove_student(), width=18, fg="white", font="Century 12 bold", bg="black",bd=4)
    b7.place(y=480, x=10)

    b8 = tk.Button(background, text="Remove Book", command=lambda: remove_book.remove_book(), width=18, fg="white", font="Century 12 bold", bg="black",bd=4)
    b8.place(y=535, x=10)

    def open_itch1():  # function for open the link
        webbrowser.open("http://www.uiit.ac.in/about/library.php")  # build in module for open the link i.e., webbrowser.open

    link1 = t.Button(background, text="Gallery", font="Century 12 bold", fg="white", bg="black", command=open_itch1, width=18, bd=4)
    link1.place(y=590, x=10)

    def tick():  # function for display the time , time_string = variable
        time_string = time.strftime("%H:%M:%S")  # build in, time display module  for the time display in window i.e.,time.strftime
        clock.config(text=time_string)  # to show changes in the label we use .config
        clock.after(200, tick)  # blink after 200 seconds

    clock = t.Label(background, font="Century 20 bold", fg="white", bg="black")
    clock.place(y=90, x=1400)  # place this label in x,y co-ordinate of this window
    tick()  # here we call the function

    def open_itch():  # function for open the link
        webbrowser.open("http://www.uiit.ac.in/")  # build in module for open the link i.e., webbrowser.open
    link = t.Button(background, text="www.uiit.ac.in", font="Century 15 bold", fg="white", bg="black", command=open_itch)
    link.place(y=132, x=700)

    def Quit():  # quit function
        root8 = t.Tk()  # creating quit window
        root8.geometry("700x120")  # dimension of the quit window
        root8.iconbitmap("Graphicloads-Colorful-Long-Shadow-Book.ico")  # to show the icon in the quit window
        root8.title("WARNING")  # title of the quit window
        quitlabel2 = t.Label(root8, text="                                      "
                                         "ARE YOU SURE TO WANT EXIT  ? \n", font="Century 13")

        quitlabel2.grid(row=0, column=0)

        def quitfun():

            root8.destroy()  # destroy the quit window
            top.destroy()  # destroy the main window
            background.destroy()

        def quitfun2():

            root8.destroy()  # destroy quit window

        b17 = t.Button(root8, text="YES", fg="black", width=10, bd=8, font="Century 12 bold", command=quitfun)
        b17.place(x=50, y=60)

        b18 = t.Button(root8, text="NO", fg="black", width=10, bd=8, font="Century 12 bold", command=quitfun2)
        b18.place(x=500, y=60)

    b8 = t.Button(background, text="EXIT", fg="white", width=18, bd=10, font="Century 12 bold", command=Quit, bg="black")
    b8.place(y=700, x=650)

    top.state('zoomed')  # through this it fitted to the whole window

    top.mainloop()  # without window_name.mainloop, the window can't be shown

