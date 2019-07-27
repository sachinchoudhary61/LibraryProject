import tkinter as t  # import tkinter library for GUI as t
from tkinter import messagebox  # from tkinter library import messagebox
from PIL import Image, ImageTk  # from pillow library import image & ImageTk
import os  # import os for change the directory
import interface_window  # import final library for project module in this module
global con, mycursor
import connections as c  # import connections file as c
con, mycursor = c.myconnections()
# insert data into the database,function
def insertdata(librarian_id,name,password,email_id,identity_card_num,roleid,d_o_b,address,mobile_no):

    mycursor.execute("INSERT INTO login_account_creation_details"
                     "(librarian_id,name,password,email_id,identity_card_num,roleid,d_o_b,address,mobile_no)"
                     "values('%s','%s','%s','%s',%s,%s,'%s','%s',%s)"
         % (str(librarian_id), str(name), str(password), str(email_id), identity_card_num, roleid, str(d_o_b), str(address), mobile_no))
    #  mycursor.execute used to execute the querry
    con.commit()  # this is used for the making the changes in the data-base

# this function creates the login window
def login():
    os.chdir("C:\\LibraryProject\\images\\background_images\\")  # it is used to change the the directory
    top1 = t.Tk()  # creates window
    top1.title("LOGIN")  # title  of the window
    top1.iconbitmap("Graphicloads-Colorful-Long-Shadow-Book.ico")  # to set the icon in te window
    #top1.geometry("600x200")  # set the dimensions of the window
    w = 600  # width for the Tk root
    h = 200  # height for the Tk root
    # get screen width and height

    ws = top1.winfo_screenwidth()  # width of the screen
    hs = top1.winfo_screenheight()  # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = (ws/3) - (w/3)
    y = (hs/3) - (h/3)
    # set the dimensions of the screen
    # and where it is placed
    top1.geometry('%dx%d+%d+%d' % (w, h, x, y))
    top1.resizable(0, 0)  # Don't allow resizing in the x or y direction
    image = Image.open("loginpage.jpg")  # through this we can open the image

    login_image = ImageTk.PhotoImage(image)  #
    lwbi = t.Label(image=login_image)  # set image as a label in the background of the window
    lwbi.pack(fill=t.BOTH, expand=t.YES)  # to fill the image in the background and expand the image in the background

    t1 = t.Entry(lwbi, width=30, bd=5)   # Entry box to fill the librarian id
    t1.place(x=300, y=30)  # place this entry box into the login window

    t2 = t.Entry(lwbi, show="*", width=30, bd=5)  # Entry box to fill the password, & show="*" show text in *
    t2.place(x=300, y=80)  # place this entry box into the login window

    # command=lambda: signup2(top1), we can't call another function directly into the button of this function so, we use lambda, to call directly
    b2 = t.Button(lwbi, text="CREATE NEW ACCOUNT", command=lambda: signup2(top1), font="Century 10 bold", fg="white", bg="blue")
    b2.place(x=300, y=150)  # place this Button into the login window

    def loginfun():  # this function is used to enter in the main window

        e = t1.get()  # e variable store the librarian id
        p = t2.get()  # p variable store the password

        query = "SELECT * FROM login_account_creation_details WHERE librarian_id='%s'" % e
        mycursor.execute(query)  # this is used to execute the above query
        data = mycursor.fetchall()  # mycursor.fetchall() it fecthes the all data & store in the data variable
        if len(data) > 0:  # if the lenght of the data is greater than 0 then it execute below line of code

            print(data[0][2])
            dp = data[0][2]  # in fetched data we select particular row and column i.e.,[0][2]= [row][column]
                              # & store selected data in the dp variable

            if dp == p:  # if dp is equal to password enter by the librarian the below line of code executes

                top1.destroy()  # here we destroy the login window
                interface_window.mainwindow()  # here we call the libaray project main window

            else:
                messagebox.showinfo("ALARM", "SORRY! YOU HAVE ENTERED INCORRECT PASSWORD")
        else:
            messagebox.showinfo("ALARM", "SORRY!,YOU HAVE ENTERED INCORRECT USER ID")

    b1 = t.Button(lwbi, text="LOGIN", command=loginfun, font="Century 10 bold", fg="white", bg="blue")
    b1.place(x=100, y=150)
    lwbi.mainloop()

def signup2(top1):

        top1.destroy()

        os.chdir("C:\\LibraryProject\\images\\background_images\\")

        root0 = t.Tk()
        root0.title("new account creation")
        root0.geometry("1920x1080")
        root0.iconbitmap("Graphicloads-Colorful-Long-Shadow-Book.ico")

        l_1 = t.Label(root0, text="LIBRARIAN ID CREATION", font="Century 15 bold", fg="black")
        l_1.place(x=500, y=10)

        l1 = t.Label(root0, text="(1). LIBRARIAN ID                      :", font="Century 12 bold", fg="black")
        l1.place(x=100, y=100)
        t_1 = t.Entry(root0, width=40)
        t_1.place(x=600, y=100)

        l2 = t.Label(root0, text="(2). NAME                                     :", font="Century 12 bold", fg="black")
        l2.place(x=100, y=150)
        t2 = t.Entry(root0, width=40)
        t2.place(x=600, y=150)

        l3 = t.Label(root0, text="(3). PASSWORD                            :", font="Century 12 bold", fg="black")
        l3.place(x=100, y=200)
        t3 = t.Entry(root0, width=40)
        t3.place(x=600, y=200)

        l4 = t.Label(root0, text="(4). EMAIL-ID                               :", font="Century 12 bold", fg="black")
        l4.place(x=100, y=250)
        t4 = t.Entry(root0, width=40)
        t4.place(x=600, y=250)

        l5 = t.Label(root0, text="(5). IDENTITY CARD NO.            :", font="Century 12 bold", fg="black")
        l5.place(x=100, y=300)
        t5 = t.Entry(root0, width=40)
        t5.place(x=600, y=300)

        l6 = t.Label(root0, text="(6). DATE OF BIRTH                    :", font="Century 12 bold", fg="black")
        l6.place(x=100, y=350)
        t7 = t.Entry(root0, width=40)
        t7.place(x=600, y=350)

        l8 = t.Label(root0, text="(7). ADDRESS                                :", font="Century 12 bold", fg="black")
        l8.place(x=100, y=400)
        t8 = t.Entry(root0, width=40)
        t8.place(x=600, y=400)

        l9 = t.Label(root0, text="(8). MOBILE NO                             :", font="Century 12 bold", fg="black")
        l9.place(x=100, y=450)
        t9 = t.Entry(root0, width=40)
        t9.place(x=600, y=450)

        def getdata():
            messagebox.showinfo("Message", "Account created sucessfully")
            librarian_id = t_1.get()
            name = t2.get()
            password = t3.get()
            email_id = t4.get()
            identity_card_num = t5.get()
            d_o_b = t7.get()
            address = t8.get()
            mobile_no = t9.get()
            roleid = 2

            insertdata(librarian_id, name, password, email_id, identity_card_num, roleid, d_o_b, address, mobile_no)

        account_button = t.Button(root0, text="CREATE", bg="blue", fg="white", command=getdata, font="Century 12 bold")
        account_button.place(x=200, y=600)

        def backbtn():  # back button function
            root0.destroy()
            login()

        # crtnawbbtn = create new account window back button
        crtnawbbtn = t.Button(root0, text="BACK TO LOGIN", bg="blue", fg="white", command=backbtn, font="Century 12 bold")
        crtnawbbtn.place(x=600, y=600)
        root0.mainloop()




