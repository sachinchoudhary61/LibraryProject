import tkinter as t  # import tkinter as t
from tkinter import *
from tkinter import filedialog  # from tkinter library import filedialog to open the file or save the file
from PIL import ImageTk, Image  # from PIL library import ImageTk and Image
from tkinter import StringVar, ttk
import os  # used for the work with the directory
import code128  # import code128 module with the help of this we can gen_rate the barcode
from tkcalendar import Calendar
from tkinter import messagebox
import interface_window
global con, mycursor
import connections as c
con, mycursor = c.myconnections()


def insertdata(unique_id, first_name,last_name ,father_name, student_email_id, university_roll_no, semester, engineering_branch, address, mobile_no, d_o_b):

        mycursor.execute("INSERT INTO member_details"
                         "(unique_id,first_name,last_name,father_name,student_email_id,university_roll_no,semester,engineering_branch,address,mobile_no,d_o_b)"
                         "values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                         % (str(unique_id) ,str(first_name),str(last_name) ,str(father_name), str(student_email_id), str(university_roll_no), str(semester), str(engineering_branch), str(address), str(mobile_no), str(d_o_b)))
        con.commit()  # used for make the changes in the database



def anm(top):

    top.destroy()

    os.chdir("C:\\LibraryProject\\images\\background_images\\")
    rootam1 = t.Tk()
    rootam1.title("Add New Student")
    rootam1.state('zoomed')
    #rootam1.configure(background='gray18')
    screen_width = rootam1.winfo_screenwidth()  # by this we can get the width of the tkinter window
    screen_height = rootam1.winfo_screenheight()  # by this we can get the height of the tkinter window
    dim1 = str(screen_width)  # here we store the screen width of the tkinter window as a string in the dim1 variable
    dim2 = str(screen_height)  # here we store the screen height of the tkinter window as a string in the dim1 variable
    dim3 = "%sx%s" % (dim1, dim2)  # in the dim3 variable we set the dimension of the tkinter window
    rootam1.geometry(dim3)  # Dimension of the returning window
    rootam1.iconbitmap("Graphicloads-Colorful-Long-Shadow-Book.ico")

    scrollbar = Scrollbar(rootam1)
    scrollbar.pack(side=RIGHT, fill=Y)

    l_1 = t.Label(rootam1, text="HERE YOU CAN ADD THE STUDENT ", font="Century 14 bold")  # ,bg="gray18",fg="white"
    l_1.place(x=400, y=3)

    def backbtn1():  # back button function

        rootam1.destroy()
        interface_window.mainwindow()

    anmwbtn1 = t.Button(rootam1, text=" HOME ", bg="black", fg="white", bd=2, command=backbtn1, font="Century 10 bold")
    anmwbtn1.place(x=200, y=5)

    l1 = t.Label(rootam1, text="(1).FIRST NAME                                              :", font="Century 12 bold")  # ,bg="gray18",fg="white"
    l1.place(x=40, y=80)
    t1 = t.Entry(rootam1, width=25, font=" Century ")  # ,bg="gray35",fg="white"
    t1.place(x=500, y=80)

    l__1 = t.Label(rootam1, text="(2). LAST NAME                                              :", font="Century 12 bold")  # ,bg="gray18",fg="white"
    l__1.place(x=40, y=130)
    t__1 = t.Entry(rootam1, width=25, font=" Century ")  # ,bg="gray35",fg="white"
    t__1.place(x=500, y=130)

    l1_1 = t.Label(rootam1, text="(3). UNIVERSITY ROLL NO.               :",  font="Century 12 bold")  # ,bg="gray18",fg="white"
    l1_1.place(x=40, y=180)
    t1_1 = t.Entry(rootam1, width=25, font="Century")  # ,bg="gray35",fg="white"
    t1_1.place(x=500, y=180)

    l2 = t.Label(rootam1, text="(4). FATHER'S NAME                          :", font="Century 12 bold")  # ,bg="gray18",fg="white"
    l2.place(x=40, y=230)
    t2 = t.Entry(rootam1, width=25, font="Century")  # ,bg="gray35",fg="white"
    t2.place(x=500, y=230)

    l3 = t.Label(rootam1, text="(5). STUDENT EMAIL-ID                    :", font="Century 12 bold")  # ,bg="gray18",fg="white"
    l3.place(x=40, y=280)
    t3 = t.Entry(rootam1, width=25, font="Century")  # , bg="gray35",fg="white"
    t3.place(x=500, y=280)

    l4 = t.Label(rootam1, text="(6). SEMESTER                                    :", font="Century 12 bold")  # ,bg="gray18",fg="white"
    l4.place(x=40, y=330)

    # value for semester
    valuefs = StringVar()  # string is of the type VAR
    a = valuefs.get()
    box = ttk.Combobox(rootam1, textvariable=valuefs)  # ,state='readonly'
    box['value'] = ('I', 'II', 'III', 'IV ', 'V', 'VI', 'VII', 'VII', 'VIII')
    box.current(0)
    box.place(x=500, y=330)
    a = valuefs.get()

    l_5 = t.Label(rootam1, text="(7). ENGINEERING BRANCH            :", font="Century 12 bold")  # here we set the label of the drop down widget
    l_5.place(x=40, y=380)  # place of the label widget                                             # ,bg="gray18",fg="white"

    # value for branch
    valuefb = StringVar()  # string is of the var type
    b = valuefb.get()
    #  in ttk window  make combobox as a drop_down widget
    box = ttk.Combobox(rootam1, textvariable=valuefb)  # ,state='readonly'
    box['value'] = ('CSE', 'IT')  # values  in the combobox
    box.current(0)
    box.place(x=500, y=380)  # here we set the place of this drop down widget
    b = valuefb.get()  # b variable store the value for semester

    l5 = t.Label(rootam1, text="(8). ADDRESS                                       :", font="Century 12 bold")  # ,bg="gray18",fg="white"
    l5.place(x=40, y=430)
    t5 = t.Entry(rootam1, width=25, font="Century")  # ,bg="gray35",fg="white"
    t5.place(x=500, y=430)

    l6 = t.Label(rootam1, text="(9). MOBILE NO.                                  :", font="Century 12 bold")  # ,bg="gray18",fg="white"
    l6.place(x=40, y=510)
    t6 = t.Entry(rootam1, width=25, font="Century")  # ,bg="gray35",fg="white"
    t6.place(x=500, y=510)

    l7 = t.Label(rootam1, text="(10). D.O.B                                              :", font="Century 12 bold")  # ,bg="gray18",fg="white"
    l7.place(x=40, y=560)

    def calan():
        def print_sel():
            global dobvg
            dobvg = cal.selection_get()
            print(cal.selection_get())

            date1 = t.Label(rootam1, text="%s" % dobvg, font="Century 15 bold", fg="blue")

            date1.place(x=550, y=585)
            top.destroy()

        top = t.Toplevel(rootam1)

        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=2019, month=3, day=20)
        cal.pack(fill="both", expand=True)
        t.Button(top, text="ok", command=print_sel).pack()

    calbtnb1 = t.Button(rootam1, text=' CALENDER ', command=calan, font="Century 12 bold")  # ,bg="seagreen",fg="white", width=15
    calbtnb1.place(x=550, y=560)

   # t7 = t.Entry(rootam1, width=20, bd=2)
   # t7.place(x=500, y=480)

    def insertvalue():
        x = t1.get()  # =  first name of the student
        y = t1_1.get()  # =  university roll number of the student
        global bcode
        bcode = str(x)+str(y)  # = bar code value = name+roll_no.

        messagebox.showinfo("Message", "Student add succesfully ")

        unique_id = bcode
        first_name = t1.get()
        last_name = t__1.get()
        father_name = t2.get()
        university_roll_no = t1_1.get()
        student_email_id = t3.get()
        semester = a
        engineering_branch = b
        address = t5.get()
        mobile_no = t6.get()
        d_o_b = dobvg

                    # here we call the insertdata function
        insertdata(unique_id, first_name, last_name, father_name, student_email_id, university_roll_no, semester, engineering_branch, address, mobile_no, d_o_b)

        nextb1 = t.Button(rootam1, text="NEXT", command=lambda: imagerecord(), font="Century 15 bold", fg="white", bg="blue", width=12)
        nextb1.place(x=600, y=650)

    insb = t.Button(rootam1, text="DONE", command=insertvalue, font="Century 15 bold", bg="blue", fg="white", width=12)
    insb.place(x=250, y=650)

    def imagerecord():
        print("here : ", bcode)
        rootam1.destroy()
        rootam2 = t.Tk()
        rootam2.geometry("500x480")
        rootam2.title("Add New Student")
        rootam2.resizable(0, 0)  # Don't allow resizing in the x or y direction

        #rootam2.configure(background='gray18')

        l9 = t.Label(rootam2, text="    STUDENT PHOTO   ", font="Century 14 bold")  # , bg="gray18", fg="white"
        l9.place(x=100, y=20)

        def anb_img_set():  # set student image as a label in the window =  function

            print(bcode)
            # below line of code  is used for open the file
            rootam2.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("png files", "*.png"), ("all files", "*.*")))

            img = Image.open(rootam2.filename)  # used to open the image
            os.chdir("C:\\LibraryProject\\images\\student_images\\")  # used to change the directory

            width = 250  # width of the student image
            height = 200  # height of the student image
            # use one of these filter options to resize the image
            im2 = img.resize((width, height), Image.NEAREST)      # use nearest neighbour

            im2.save("%s.png" % bcode)  # used to save the image
            img = ImageTk.PhotoImage(Image.open("%s.png" % bcode))  # used to open the image

            stn_img = t.Label(rootam2, image=img)  # stn_image = student image
            stn_img.place(x=90, y=60)
            rootam2.mainloop()

        def create_bar_codes():  # Barcode genrator function

            print(bcode)
            os.chdir("C:\\LibraryProject\\images\\student_barcode\\")  # used for change the current directory

            #  code123 barcode type(It take ASCII value)
            code128.image(bcode).save("%s.png" % bcode)  # with PIL present

            img = Image.open("%s.png" % bcode)  # Used to open the  image

            width = 200  # width of the image
            height = 60  # height of the image

            # use one of these filter options to resize the image
            im2 = img.resize((width, height), Image.NEAREST)      # use nearest neighbour

            im2.save("%s.png" % bcode)  # here we save the barcode image in the directory
            img = ImageTk.PhotoImage(Image.open("%s.png" % bcode))  # used for open the image
            # bcodeimg = bar code image label
            bcodeimg = t.Label(rootam2, image=img)  # used for place the barcode image in the window
            bcodeimg.place(x=115, y=270)  # place for set the barcode image in the label

            at1 = t.Label(rootam2, text=bcode, font="Century 10 bold")  # here we set the name of the barcode image in the current window,, bg="gray18", fg="white"
            at1.place(x=160, y=332)  # place in the window to set the above label

            messagebox.showinfo("Message", "Student Image and Unique barcode saved sucessfully")

            rootam2.mainloop()
        #  anbbcgbtn = add new book bar code genrator button

        anbbcgbtn = t.Button(rootam2, text="Generate Barcode", command=create_bar_codes, font="Century 12 bold", width=15) #, width=18, bd=10
        anbbcgbtn.place(x=250, y=360)

        anb_detail_add_button = t.Button(rootam2, text="Upload Image", command=anb_img_set, font="Century 12 bold", width=15)  # , bg="seagreen",fg="white"
        anb_detail_add_button.place(x=75, y=360)

        def backbtn2():  # back button function

            rootam2.destroy()
            interface_window.mainwindow()

        # bbwbbtn = borrowing process  window back button for going in library main window
        anmwbtn2 = t.Button(rootam2, text=" HOME ", command=backbtn2, font="Century 12 bold", bg="blue", fg="white")  #  bg="seagreen", fg="white",
        anmwbtn2.place(x=175, y=430)

        rootam2.mainloop()

    rootam1.mainloop()


