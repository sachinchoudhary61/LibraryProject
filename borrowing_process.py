import tkinter as t  # import tkinter library for the GUI as t
from tkinter import *
import os  # import os to change the current directory
import tkinter as tk  # import tkinter library for the GUI as tk
from PIL import Image, ImageTk  # used to import the photo in the background
import smtplib
from tkcalendar import DateEntry  # import DateEntry library from tkcalender library
from tkinter import messagebox  # from tkinter library import messagebox to show messagebox
import interface_window  # import final libray for project module because borrowing process module contain the use of this module.
from tkcalendar import Calendar  # from tkcalender module import calender
global con, mycursor1
import connections as c  # import connections as c
con, mycursor = c.myconnections()


def bp(top):  # borrowing process main window function & we pass top in this function

    os.chdir("C:\\LibraryProject\\images\\background_images\\")  # here we shift the current directory into the projrct directory
    top3 = tk.Tk()  # with the help of this we can create a window
    #top3.geometry('280x200')  # dimension of the window
    w = 280  # width for the Tk root
    h = 200  # height for the Tk root
    # get screen width and height
    ws = top3.winfo_screenwidth()  # width of the screen
    hs = top3.winfo_screenheight()  # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    # set the dimensions of the screen
    # and where it is placed
    top3.geometry('%dx%d+%d+%d' % (w, h, x, y))
    top3.iconbitmap("Graphicloads-Colorful-Long-Shadow-Book.ico")  # used to display the icon in the window
    top3.title("ID confirmation")  # used to display the title in the create window
    top3.configure(bg="royalblue3")
    top3.resizable(0, 0)  # Don't allow resizing in the x or y direction

    bpll = tk.Label(top3, text="STUDENT UNIQUE ID  :", font="Century 12 bold", fg="white", bg="RoyalBlue3")
    bpll.grid(padx=20, pady=20, row=0, column=0)

    # borrowing process login text box
    bplt = tk.Entry(top3, width=30, bd=3)
    bplt.place(x=20, y=80)  # here we place this textbox in the borrowing process window

    def loginfun():  # borrowing process login funtion
        bpltg = bplt.get()  # bpltg =  borrowing process login text get

        #  select from member deatils table where unique Id is equal to bpltg = borrowing process login text get
        bquery = "SELECT unique_id FROM member_details WHERE unique_id='%s'" % bpltg
        mycursor.execute(bquery)  # this is used to execute the query
        bdata = mycursor.fetchall()  # data store the value which follows the query(data store whole row)
        print(bdata)

        if len(bpltg) > 0:   # if the length of the user input greater than 0 then only below statement will  execute

            #bd = bdata[0][0]  # In fetched data we select particular row & column
            #print(bd)

            if bdata[0][0] == bpltg:
                print(bdata[0][0])
                top.destroy()
                top3.destroy()
                bpw(bpltg, top)  # here we call the borrowing process main window

#bd == bpltg:
            elif bdata[0][0] != bpltg:   # if data in dp is equal to student id enter by the admin
                messagebox.showinfo("ALARM", "SORRY! You have Entered wrong student unique ID")

        else:
            messagebox.showinfo("ALARM", "Please Input the Student unique ID ")  # Error shown if librarian not enter the student unique id in te borrowing process login window

    bplbtn = tk.Button(top3, text="CONFIRM", command=loginfun, font="Century 10 bold", fg="white", bg="blue")
    bplbtn.place(x=20, y=130)  # here we place this button in the borrowing process login window to enter in the borrowing process main window

    def backbtn():  # back button function

        top3.destroy()  # here we destroy the borrowing process login window

    bplbtn2 = t.Button(top3, text="EXIT", bg="blue", fg="white", command=backbtn, font="Century 10 bold")
    bplbtn2.place(x=150, y=130)  # here we place this home button  in the borrowing process window, to going back into the main window
    top3.mainloop()
# first insert data function to insert the details enter by the librarian in the data base when student want to borrow one book
def insertdata(borrower_unique_id,no_bk_stn_borrowed,acc_no_of_b1,issue_date,return_date):
    mycursor.execute("INSERT INTO borrowing_process_table"
                     "(borrower_unique_id,no_bk_stn_borrowed,acc_no_of_b1,issue_date,return_date)"
                     "values('%s',%s,%s,'%s','%s')"
                     % (str(borrower_unique_id), no_bk_stn_borrowed, acc_no_of_b1, str(issue_date), str(return_date)))
    con.commit()
# second  insert data function to insert the details enter by the librarian in the data base when student want to borrow two book
def insertdata2(borrower_unique_id,no_bk_stn_borrowed,acc_no_of_b1,acc_no_of_b2,issue_date,return_date):
    mycursor.execute("INSERT INTO borrowing_process_table"
                     "(borrower_unique_id,no_bk_stn_borrowed,acc_no_of_b1,acc_no_of_b2,issue_date,return_date)"
                     "values('%s',%s,%s,%s,'%s','%s')"
                     % (str(borrower_unique_id),no_bk_stn_borrowed ,acc_no_of_b1, acc_no_of_b2, str(issue_date), str(return_date)))
    con.commit()
# third  insert data function to insert the details enter by the librarian in the data base when student want to borrow three book
def insertdata3(borrower_unique_id,no_bk_stn_borrowed,acc_no_of_b1,acc_no_of_b2,acc_no_of_b3,issue_date,return_date):
    mycursor.execute("INSERT INTO borrowing_process_table"
                     "(borrower_unique_id,no_bk_stn_borrowed, acc_no_of_b1, acc_no_of_b2,acc_no_of_b3,issue_date,return_date)"
                     "values('%s',%s,%s,%s,%s,'%s','%s')"
                     % (str(borrower_unique_id), no_bk_stn_borrowed ,acc_no_of_b1, acc_no_of_b2, acc_no_of_b3, str(issue_date), str(return_date)))
    con.commit()

def bpw(bpltg,top):  # borrowing process window function

    os.chdir("C:\\LibraryProject\\images\\background_images\\")  # here we change the directory
    root4 = t.Tk()  # by this we create the window
    root4.iconbitmap("Graphicloads-Colorful-Long-Shadow-Book.ico")  # through this we set the icon of the window
    root4.title("Borrowing Process")  # title of the window
    root4.state('zoomed')
    screen_width = root4.winfo_screenwidth()  # by this we can get the width of the tkinter window
    screen_height = root4.winfo_screenheight()  # by this we can get the height of the tkinter window
    dim1 = str(screen_width)  # here we store the screen width of the tkinter window as a string in the dim1 variable
    dim2 = str(screen_height)  # here we store the screen height of the tkinter window as a string in the dim1 variable
    dim3 = "%sx%s" % (dim1, dim2)  # in the dim3 variable we set the dimension of the tkinter window
    root4.geometry(dim3)  # Dimension of the returning window

    scrollbar = Scrollbar(root4)
    scrollbar.pack(side=BOTTOM, fill=X)

    bpwl1 = t.Label(root4, text="HERE YOU CAN LEND A BOOKS TO THE STUDENT ", font="Century 15 bold", fg="black")
    bpwl1.place(x=400)

    bpwl1 = t.Label(root4, text="Enter the number of Books, Borrower like to borrow        :", font="Century 15 bold", fg="black")
    bpwl1.place(x=50, y=72)

    def backbtn():  # back button function

        root4.destroy()
        interface_window.mainwindow()

    # bbwbbtn = borrowing process  window back button for going in library main window
    bbwbbtn = t.Button(root4, text=" HOME ", bg="black", fg="white", bd=2, command=backbtn, font="Century 10 bold")
    bbwbbtn.place(x=650, y=30)

    bpwt1 = t.Entry(root4, width=40, bd=3)
    bpwt1.place(x=700, y=75)

    bpwbtn1 = t.Button(root4, text="CONFIRM", font="Century 8 bold", fg="blue", command=lambda: tg(top))
    bpwbtn1.place(x=1000, y=72)

    def calan():  # calender function
        def print_sel():  # select date in the calender function
            global bpcvg1  # declare below vaiable as gllobaly because we have a use of this variable in another function
            bpcvg1 = cal.selection_get()  # borrowing process calender value get one
            print(cal.selection_get())

            date1 = t.Label(root4, text="%s" % bpcvg1, font="Century 15 bold", fg="blue")
            date1.place(x=550, y=550)  # label for show the date in the calender

            top.destroy()  # through this we destroy the calender

        top = t.Toplevel(root4)  # to print the calender in the borrowing process window

        cal = Calendar(top,
                                                   font="Arial 14", selectmode='day',
                                                   cursor="hand1", year=2019, month=3, day=1, bg="blue")
        cal.pack(fill="both", expand=True)  # make calender lay-out in the top window of the calender
        t.Button(top, text="   OK   ", command=print_sel, width=15, bg="white", fg="blue").pack()  # set the ok button in the top window of  the calender

    def tg(top):  # function for text get
        nonlocal bpwt1  # we make borrowing process window text get one, bpwt1 is the number of the book
        vg = int(bpwt1.get())  # value get(vg) = make  int value of borrowing process window text one
        if vg <= 3:  # if number of the book is below than three than only below statement will execute

            if vg == 1:  # if number of the book is equal to one than below code will execute

                bpwl2 = t.Label(root4, text="BOOK(1)", font="Century 10 bold", fg="black")
                bpwl2.place(x=500, y=110)

                bpwl3 = t.Label(root4, text=" ACC NO.                            :", font="Century 15 bold", fg="black")
                bpwl3.place(x=80, y=145)  # label for the  ACC no.

                bpwt2 = t.Entry(root4, width=30, bd=2)
                bpwt2.place(x=500, y=150)  # text box for the text box

                bpwbtn3 = t.Button(root4, text="CONFIRM", font="Century 10 bold", fg="blue", command=lambda: bpwbdg())
                bpwbtn3.place(x=800, y=145)  # in this button we bind the below function using lambda because we can't
                                 # another function into this function
                def bpwbdg():  # to print the book information in the window, function
                    bpwtg = bpwt2.get()  # borrowing process window text get(variable)= borrowing process window text get 2, i.e., acc no. of the book
                    if len(bpwtg) > 0:
                        # select all from the book detail table where acc no is equal = bpwtg
                        query = "SELECT * FROM book_detail_table WHERE acc_no='%s'" % bpwtg
                        mycursor.execute(query)  # this is used to execute the query
                        data = mycursor.fetchall()  # mycursor.fetchall() fetches the data according to query & store data variable
                        #if bpt0g in data:
                        for i in data:  # apply for loop in the fetched data to print the details of the book in the window

                                lctn = "C:\\LibraryProject\\images\\book_label\\%s.png" % bpwtg
                                print(lctn)
                                img = ImageTk.PhotoImage(Image.open(lctn))
                                canvas = t.Canvas(height=250, width=200)

                                canvas.create_image(0, 0, image=img)
                                canvas.image = img
                                rpw__l5 = t.Label(root4, image=img)
                                rpw__l5.place(x=900, y=200)

                                bpwl4 = t.Label(root4, text="(1).BOOK NAME                               : ", font="Century 10 bold", fg="black")
                                bpwl4.place(x=100, y=210)
                                bn = i[0]
                                bpwl5 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl5.configure(text=bn)  # this is used to make the changes in the label
                                bpwl5.place(x=600, y=210)

                                bpwl6 = t.Label(root4, text="(2).NUMBER OF STOCKS                  : ", font="Century 10 bold", fg="black")
                                bpwl6.place(x=100, y=250)

                                bpwl7 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl7.configure(text=i[2])
                                bpwl7.place(x=600, y=250)

                                bpwl8 = t.Label(root4, text="(3).AUTHOR NAME                           : ", font="Century 10 bold", fg="black")
                                bpwl8.place(x=100, y=290)

                                bpwl9 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl9.configure(text=i[3])
                                bpwl9.place(x=600, y=290)

                                bpwl10 = t.Label(root4, text="(4).PUBLISHER NAME                      : ", font="Century 10 bold", fg="black")
                                bpwl10.place(x=100, y=330)

                                bpwl11 = t.Label(root4, font="Century 12 bold", fg="black")
                                bpwl11.configure(text=i[4])
                                bpwl11.place(x=600, y=330)

                                bpwl12 = t.Label(root4, text="(5).PRICE.(INR)                                :", font="Century 10 bold", fg="black")
                                bpwl12.place(x=100, y=370)

                                bpwl13 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl13.configure(text=i[5])
                                bpwl13.place(x=600, y=370)

                                bpwl14 = t.Label(root4, text="ISSUE DATE         :", font="Century 12 bold", fg="black",)
                                bpwl14.place(x=300, y=450)

                                cal = DateEntry(root4, width=12, background='darkblue', foreground='white', borderwidth=2, bd=3)
                                cal.place()
                                vgcal = cal.get_date()  # get today date in vgcal(variable)i.e.,  value get calender value
                                bpwl_14 = t.Label(root4, text=vgcal, font="Century 12 bold", fg="black",)
                                bpwl_14.place(x=550, y=450)  # label for show the  detail

                                bpwl15 = t.Label(root4, text="RETURN DATE     :", font="Century 12 bold", fg="black")
                                bpwl15.place(x=300, y=550)  # Return date Label

                                calbtnb1 = t.Button(root4, text=' CALENDER ', command=calan, fg="black", bd=2, font="Century 10 bold")
                                calbtnb1.place(x=550, y=500)  # calender button to print the selected return date during issue of the book


                                def sendmail():

                                        query_for_fetch = "SELECT student_email_id FROM member_details WHERE unique_id='%s'" % bpltg
                                        mycursor.execute(query_for_fetch)  # this is used to execute the query
                                        email = mycursor.fetchall()  # data store the value which follows the query(data store whole row)
                                        print(email)
                                        msg = "--*---*------WELCOME TO UIIT LIBRARY-----*---*--\n\n\n" \
                                              "          BOOK BORROWED DETAILS \n\n" \
                                              "           BOOK NAME      : %s \n\n" \
                                              "           ACC NO.            : %s \n\n" \
                                              "           ISSUE DATE      : %s \n\n" \
                                              "           RETURN DATE : %s  " % (bn, bpwtg, vgcal, bpcvg1)

                                        server = smtplib.SMTP("smtp.gmail.com", 587)
                                        server.starttls()
                                        server.login('stheartsachu@gmail.com', 'stoneheartsachu')
                                        server.sendmail('stheartsachu@gmail.com', email, msg)
                                        server.quit()

                                def ins():  # insert function to insert the borrowing book data into the database

                                    def update():  # update function to update the no. of stocks of the books in the book detail table
                                        # select all from book  detail table where acc number is eqaul to bpwtg
                                        mycursor.execute("SELECT * FROM book_detail_table WHERE acc_no=%s" % bpwtg)  # mycursor.execute is used to execute the query
                                        data_udt = mycursor.fetchall()  # mycursor.fetchall() fetchesthe all data
                                        print(data_udt[0][2])  # select particular row & column in the fecthed data
                                                # fetched data conatinn the number of the stocks
                                        d_upd = data_udt[0][2]-1  # less value by one in the number of the books
                                        print(d_upd)
                                        # UPDATE book detail table and set no. of copies,-1 where acc no is equal to bpwtg
                                        mycursor.execute("UPDATE book_detail_table SET no_of_copies=%s WHERE acc_no=%s" % (d_upd, bpwtg))
                                        con.commit()  # this is used to make the changes
                                    update()  # here we call the update function
                                    sendmail()
                                    messagebox.showinfo(" Message ", "Hi , Book is sucessfully lended to the student")
                                    borrower_unique_id = bpltg
                                    acc_no_of_b1 = bpwtg
                                    issue_date = vgcal
                                    return_date = bpcvg1
                                    no_bk_stn_borrowed = vg

                                    insertdata(borrower_unique_id, no_bk_stn_borrowed, acc_no_of_b1, issue_date, return_date)

                        bpbtn2 = t.Button(root4, text=" LEND IT ", fg="white", bg="blue", bd=2, command=lambda: ins(),  font="Century 15 bold")
                        bpbtn2.place(x=300, y=650)  # button to lend the book

                        bbwbbtn2 = t.Button(root4, text=" HOME ", bg="blue", fg="white", bd=2, command=backbtn, font="Century 15 bold")
                        bbwbbtn2.place(x=800, y=650)  # button for going into the main window
                        #else:
                            #messagebox.showinfo("ALARM", "SOORY!,YOU HAVE ENTRED WRONG ACC NO.")
                    else:
                        messagebox.showinfo("ALARM", "SOORY!, PLEASE INPUT THE ACC NO. ")  # message if user not input the acc no.

            if vg == 2:  # if number of the books enter by the user is equal to 2 then it execute the below code

                bpwl17 = t.Label(root4, text="BOOK(1)", font="Century 10 bold", fg="black")
                bpwl17.place(x=450, y=118)

                bpwl18 = t.Label(root4, text="BOOK(2)", font="Century 10 bold", fg="black")
                bpwl18.place(x=850, y=118)

                bpwl19 = t.Label(root4, text=" ACC NO.               :", font="Century 15 bold", fg="black")
                bpwl19.place(x=80, y=145)

                bpwt6 = t.Entry(root4, width=30, bd=3)
                bpwt6.place(x=400, y=150)

                bpwt7 = t.Entry(root4, width=30, bd=3)
                bpwt7.place(x=800, y=150)

                bpwbtn5 = t.Button(root4, text="OK", font="Century 10 bold", fg="blue", command=lambda: bpwbdg1())
                bpwbtn5.place(x=1000, y=145)  # in this button we bind the below function using lambda because we can't
                                  # another function into this function

                def bpwbdg1():  # to print the book information in the window, function
                    bpwtg2 = bpwt6.get()  # borrowing process window text get 2 (variable)= borrowing process window text get 6, i.e., acc no. of the book(1)
                    bpwtg3 = bpwt7.get()  # borrowing process window text get 3 (variable)= borrowing process window text get 7, i.e., acc no. of the book(2)
                    if len(bpwtg2) > 0 or len(bpwtg3) > 0:  # if the lenght of the acc number of the books is greter than 0, then below code execute

                        # select all from the book detail table where acc no is equal = bpwtg2
                        query = "SELECT * FROM book_detail_table WHERE acc_no='%s'" % bpwtg2
                        mycursor.execute(query)  # this is used to execute the query
                        data1 = mycursor.fetchall()  # mycursor.fetchall() fetches the data according to query & store data variable

                        # select all from the book detail table where acc no is equal = bpwtg3
                        query2 = "SELECT * FROM book_detail_table WHERE acc_no='%s'" % bpwtg3
                        mycursor.execute(query2)  # this is used to execute the query2
                        data2 = mycursor.fetchall()  # mycursor.fetchall() fetches the data according to query & store data variable

                        #if bpt0g in data:

                        for i in data1:  # apply for loop in the fetched data1 to print the details of the book in the window
                                bpwl20 = t.Label(root4, text="(1).BOOK NAME               :", font="Century 10 bold", fg="black")
                                bpwl20.place(x=100, y=210)
                                bn1 = i[0]
                                bpwl21 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl21.configure(text=bn1)  # this is used to make the changes in the label
                                bpwl21.place(x=400, y=210)

                                bpwl22 = t.Label(root4, text="(2).NUMBER OF STOCKS  :", font="Century 10 bold", fg="black")
                                bpwl22.place(x=100, y=250)

                                bpwl23 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl23.configure(text=i[2])
                                bpwl23.place(x=400, y=250)

                                bpwl24 = t.Label(root4, text="(3).AUTHOR NAME           :", font="Century 10 bold", fg="black")
                                bpwl24.place(x=100, y=290)

                                bpwl25 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl25.configure(text=i[3])
                                bpwl25.place(x=400, y=290)

                                bpwl26 = t.Label(root4, text="(4).PUBLISHER NAME      :", font="Century 10 bold", fg="black")
                                bpwl26.place(x=100, y=330)

                                bpwl27 = t.Label(root4, font="Century 12 bold", fg="black")
                                bpwl27.configure(text=i[4])
                                bpwl27.place(x=400, y=330)

                                bpwl28 = t.Label(root4, text="(5).PRICE.(INR)                :", font="Century 10 bold", fg="black")
                                bpwl28.place(x=100, y=370)

                                bpwl29 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl29.configure(text=i[5])
                                bpwl29.place(x=400, y=370)

                        for i in data2:  # apply for loop in the fetched data2 to print the details of the book in the window
                                bn2 = i[0]
                                bpwl30 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl30.configure(text=i[0])  # this is used to make the changes in the label
                                bpwl30.place(x=800, y=210)

                                bpwl31 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl31.configure(text=i[2])
                                bpwl31.place(x=800, y=250)

                                bpwl32 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl32.configure(text=i[3])
                                bpwl32.place(x=800, y=290)

                                bpwl33 = t.Label(root4, font="Century 12 bold", fg="black")
                                bpwl33.configure(text=i[4])
                                bpwl33.place(x=800, y=330)

                                bpwl34 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl34.configure(text=i[5])
                                bpwl34.place(x=800, y=370)

                                bpwl35 = t.Label(root4, text="ISSUE DATE         : ", font="Century 12 bold", fg="black")
                                bpwl35.place(x=300, y=450)

                                cal3 = DateEntry(root4, width=12, background='darkblue', foreground='white', borderwidth=2, bd=3)
                                cal3.place()
                                vgcal2 = cal3.get_date()
                                bpwl35 = t.Label(root4, text=vgcal2, font="Century 12 bold", fg="black")
                                bpwl35.place(x=570, y=450)

                                bpwl36 = t.Label(root4, text="RETURN DATE     : ", font="Century 12 bold", fg="black")
                                bpwl36.place(x=300, y=550)

                                calbtnb1 = t.Button(root4, text=' CALENDER ', command=calan, fg="black", bd=2, font="Century 10 bold")
                                calbtnb1.place(x=550, y=500)
                                def sendmail1():

                                        query_for_fetch = "SELECT student_email_id FROM member_details WHERE unique_id='%s'" % bpltg
                                        mycursor.execute(query_for_fetch)  # this is used to execute the query
                                        email = mycursor.fetchall()  # data store the value which follows the query(data store whole row)
                                        print(email)
                                        msg = "--*---*------WELCOME TO UIIT LIBRARY-----*---*--\n\n\n" \
                                              "          BOOK BORROWED DETAILS \n\n" \
                                              "          (1).BOOK NAME      : %s \n\n" \
                                              "           ACC NO.            : %s \n\n" \
                                              "          (2).BOOK NAME      : %s \n\n" \
                                              "           ACC NO.            : %s \n\n" \
                                              "           ISSUE DATE      : %s \n\n" \
                                              "           RETURN DATE : %s  " % (bn1, bpwtg2, bn2, bpwtg3, vgcal2, bpcvg1)

                                        server = smtplib.SMTP("smtp.gmail.com", 587)
                                        server.starttls()
                                        server.login('stheartsachu@gmail.com', 'stoneheartsachu')
                                        server.sendmail('stheartsachu@gmail.com', email, msg)
                                        server.quit()

                                def ins():  # insert function to insert the borrowing book data into the database
                                    def update1():  # update function to update the no. of stocks of the books in the book detail table
                                        # select all from book  detail table where acc number is eqaul to bpwtg2

                                        mycursor.execute("SELECT * FROM book_detail_table WHERE acc_no=%s" % bpwtg2)  # mycursor.execute is used to execute the query
                                        data_udt1 = mycursor.fetchall()  # mycursor.fetchall() fetchesthe all data
                                        print(data_udt1[0][2])  # select particular row & column in the fecthed data
                                            # fetched data contain the number of the stocks

                                        d_upd1 = data_udt1[0][2]-1  # less value by one in the number of the books
                                        print(d_upd1)
                                        # UPDATE book detail table and set no. of copies,-1 where acc no is equal to bpwtg2
                                        mycursor.execute("UPDATE book_detail_table SET no_of_copies=%s WHERE acc_no=%s" % (d_upd1, bpwtg2))
                                        con.commit()  # this is used to make the changes
                                    update1()  # here we call the update1 function

                                    def update2():  # update function to update the no. of stocks of the books in the book detail table
                                        # select all from book  detail table where acc number is eqaul to bpwtg3
                                        mycursor.execute("SELECT * FROM book_detail_table WHERE acc_no=%s" % bpwtg3)  # mycursor.execute is used to execute the query
                                        data_udt2 = mycursor.fetchall()  # mycursor.fetchall() fetchesthe all data
                                        print(data_udt2[0][2])  # select particular row & column in the fecthed data
                                            # fetched data contain the number of the stocks

                                        d_upd2 = data_udt2[0][2]-1  # less value by one in the number of the books
                                        print(d_upd2)
                                        # UPDATE book detail table and set no. of copies,-1 where acc no is equal to bpwtg3
                                        mycursor.execute("UPDATE book_detail_table SET no_of_copies=%s WHERE acc_no=%s" % (d_upd2, bpwtg3))
                                        con.commit()  # this is used to make the changes
                                    update2()  # here we call the update2 function
                                    sendmail1()
                                    messagebox.showinfo(" Message ", " Hi , (2) Books are sucessfully lended to the student")
                                    borrower_unique_id = bpltg
                                    acc_no_of_b1 = bpwtg2
                                    acc_no_of_b2 = bpwtg3
                                    issue_date = vgcal2
                                    return_date = bpcvg1
                                    no_bk_stn_borrowed = vg

                                    insertdata2(borrower_unique_id, no_bk_stn_borrowed, acc_no_of_b1, acc_no_of_b2, issue_date, return_date)

                        bpbtn4 = t.Button(root4, text=" LEND IT ", bg="blue", fg="white", width=8, bd=2, command=lambda: ins(), font="Century 15 bold")
                        bpbtn4.place(x=300, y=650)  # button to lend the book

                        bpwbbtn5 = t.Button(root4, text=" HOME ", bg="blue", fg="white", bd=2, command=backbtn, font="Century 15 bold")
                        bpwbbtn5.place(x=800, y=650)  # button for going into the main window

                    else:
                        messagebox.showinfo("ALARM", "SOORY!, PLEASE INPUT THE ACC NO. ")

            if vg == 3:

                bpwl37 = t.Label(root4, text="BOOK(1)", font="Century 10 bold", fg="black")
                bpwl37.place(x=450, y=118)

                bpwl38 = t.Label(root4, text="BOOK(2)", font="Century 10 bold", fg="black")
                bpwl38.place(x=850, y=118)

                bpwl39 = t.Label(root4, text="BOOK(3)", font="Century 10 bold", fg="black")
                bpwl39.place(x=1250, y=118)

                bpwl40 = t.Label(root4, text=" ACC NO.                     :", font="Century 15 bold", fg="black")
                bpwl40.place(x=80, y=150)

                bpwt10 = t.Entry(root4, width=30, bd=3)
                bpwt10.place(x=400, y=150)

                bpwt11 = t.Entry(root4, width=30, bd=3)
                bpwt11.place(x=800, y=150)

                bpwt12 = t.Entry(root4, width=30, bd=3)
                bpwt12.place(x=1200, y=150)

                bpwbtn5 = t.Button(root4, text="OK", font="Century 10 bold", fg="blue", command=lambda: bpwbdg2())
                bpwbtn5.place(x=1400, y=145)

                def bpwbdg2():  # to print the book information in the window, function

                    bpwtg4 = bpwt10.get()  # borrowing process window text get 4 (variable)= borrowing process window text get 6, i.e., acc no. of the book(1)
                    bpwtg5 = bpwt11.get()  # borrowing process window text get 5 (variable)= borrowing process window text get 6, i.e., acc no. of the book(2)
                    bpwtg6 = bpwt12.get()  # borrowing process window text get 6 (variable)= borrowing process window text get 6, i.e., acc no. of the book(3)

                    if len(bpwtg4) > 0 or len(bpwtg5) > 0 or len(bpwtg6) > 0:  # if the lenght of the acc number of the books is greter than 0, then below code execute

                        # select all from the book detail table where acc no is equal = bpwtg4
                        query3 = "SELECT * FROM book_detail_table WHERE acc_no='%s'" % bpwtg4
                        mycursor.execute(query3)  # this is used to execute the query
                        data3 = mycursor.fetchall()  # mycursor.fetchall() fetches the data according to query & store data variable

                        # select all from the book detail table where acc no is equal = bpwtg5
                        query4 = "SELECT * FROM book_detail_table WHERE acc_no='%s'" % bpwtg5
                        mycursor.execute(query4)  # this is used to execute the query
                        data4 = mycursor.fetchall()  # mycursor.fetchall() fetches the data according to query & store data variable

                        # select all from the book detail table where acc no is equal = bpwtg6
                        query5 = "SELECT * FROM book_detail_table WHERE acc_no='%s'" % bpwtg6
                        mycursor.execute(query5)  # this is used to execute the query
                        data5 = mycursor.fetchall()  # mycursor.fetchall() fetches the data according to query & store data variable

                        #if bpt0g in data:
                        for i in data3:  # apply for loop in the fetched data3 to print the details of the book in the window
                                bpwl41 = t.Label(root4, text="(1).BOOK NAME                      :", font="Century 10 bold", fg="black")
                                bpwl41.place(x=100, y=210)
                                bn3 = i[0]
                                bpwl42 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl42.configure(text=bn3)
                                bpwl42.place(x=400, y=210)

                                bpwl43 = t.Label(root4, text="(2).NUMBER OF STOCK           :", font="Century 10 bold", fg="black")
                                bpwl43.place(x=100, y=250)

                                bpwl44 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl44.configure(text=i[2])
                                bpwl44.place(x=400, y=250)

                                bpwl45 = t.Label(root4, text="(3).AUTHOR NAME                  :", font="Century 10 bold", fg="black")
                                bpwl45.place(x=100, y=290)

                                bpwl46 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl46.configure(text=i[3])
                                bpwl46.place(x=400, y=290)

                                bpwl47 = t.Label(root4, text="(4).PUBLISHER NAME             : ", font="Century 10 bold", fg="black")
                                bpwl47.place(x=100, y=330)

                                bpwl48 = t.Label(root4, font="Century 12 bold", fg="black")
                                bpwl48.configure(text=i[4])
                                bpwl48.place(x=400, y=330)

                                bpwdl49 = t.Label(root4, text="(5).PRICE.(INR)                       :", font="Century 10 bold", fg="black")
                                bpwdl49.place(x=100, y=370)

                                bpwl50 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl50.configure(text=i[5])
                                bpwl50.place(x=400, y=370)

                        for i in data4:  # apply for loop in the fetched data4 to print the details of the book in the window
                                bn4 = i[0]
                                bpwl51 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl51.configure(text=bn4)
                                bpwl51.place(x=800, y=210)

                                bpwl52 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl52.configure(text=i[2])
                                bpwl52.place(x=800, y=250)

                                bpwl53 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl53.configure(text=i[3])
                                bpwl53.place(x=800, y=290)

                                bpwl54 = t.Label(root4, font="Century 12 bold", fg="black")
                                bpwl54.configure(text=i[4])
                                bpwl54.place(x=800, y=330)

                                bpwl55 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl55.configure(text=i[5])
                                bpwl55.place(x=800, y=370)

                        for i in data5:  # apply for loop in the fetched data5 to print the details of the book in the window
                                bn5 = i[0]
                                bpwl56 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl56.configure(text=bn5)
                                bpwl56.place(x=1200, y=210)

                                bpwl57 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl57.configure(text=i[2])
                                bpwl57.place(x=1200, y=250)

                                bpwl58 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl58.configure(text=i[3])
                                bpwl58.place(x=1200, y=290)

                                bpwl59 = t.Label(root4, font="Century 12 bold", fg="black")
                                bpwl59.configure(text=i[4])
                                bpwl59.place(x=1200, y=330)

                                bpwl60 = t.Label(root4, font="Century 10 bold", fg="black")
                                bpwl60.configure(text=i[5])
                                bpwl60.place(x=1200, y=370)

                                bpwl61 = t.Label(root4, text="ISSUE DATE       :", font="Century 12 bold", fg="black")
                                bpwl61.place(x=300, y=450)

                                cal4 = DateEntry(root4, width=12, background='darkblue', foreground='white', borderwidth=2, bd=3)
                                cal4.place()
                                vgcal4 = cal4.get_date()  # value get for calender 4
                                bpwl_61 = t.Label(root4, text=vgcal4, font="Century 12 bold", fg="black")
                                bpwl_61.place(x=570, y=450)

                                bpwl64 = t.Label(root4, text="RETURN DATE    :", font="Century 12 bold", fg="black")
                                bpwl64.place(x=300, y=550)

                                calbtnb2 = t.Button(root4, text=' CALENDER ', command=calan, fg="black", bd=2, font="Century 10 bold")
                                calbtnb2.place(x=550, y=500)
                                def sendmail2():

                                        query_for_fetch = "SELECT student_email_id FROM member_details WHERE unique_id='%s'" % bpltg
                                        mycursor.execute(query_for_fetch)  # this is used to execute the query
                                        email = mycursor.fetchall()  # data store the value which follows the query(data store whole row)
                                        print(email)
                                        msg = "--*---*------WELCOME TO UIIT LIBRARY-----*---*--\n\n\n" \
                                              "          BOOK BORROWED DETAILS \n\n" \
                                              "          (1).BOOK NAME      : %s \n\n" \
                                              "           ACC NO.            : %s \n\n" \
                                              "          (2).BOOK NAME      : %s \n\n" \
                                              "           ACC NO.            : %s \n\n" \
                                              "          (3).BOOK NAME      : %s \n\n" \
                                              "           ACC NO.            : %s \n\n" \
                                              "           ISSUE DATE      : %s \n\n" \
                                              "           RETURN DATE : %s  " % (bn3, bpwtg4, bn4, bpwtg5, bn5, bpwtg6, vgcal4, bpcvg1)

                                        server = smtplib.SMTP("smtp.gmail.com", 587)
                                        server.starttls()
                                        server.login('stheartsachu@gmail.com', 'stoneheartsachu')
                                        server.sendmail('stheartsachu@gmail.com', email, msg)
                                        server.quit()

                                def ins():  # insert function to insert the borrowing book data into the database
                                    def update3():  # update function to update the no. of stocks of the books in the book detail table
                                        # select all from book  detail table where acc number is eqaul to bpwtg4
                                        mycursor.execute("SELECT * FROM book_detail_table WHERE acc_no=%s" % bpwtg4)  # mycursor.execute is used to execute the query
                                        data_udt3 = mycursor.fetchall()
                                        print(data_udt3[0][2])  # select particular row & column in the fecthed data
                                            # fetched data contain the number of the stocks

                                        d_upd3 = data_udt3[0][2]-1  # less value by one in the number of the books
                                        print(d_upd3)
                                        # UPDATE book detail table and set no. of copies,-1 where acc no is equal to bpwtg4
                                        mycursor.execute("UPDATE book_detail_table SET no_of_copies=%s WHERE acc_no=%s" % (d_upd3, bpwtg4))
                                        con.commit()  # this is used to make the changes
                                    update3()  # here we call the update function

                                    def update4():  # update function to update the no. of stocks of the books in the book detail table
                                        # select all from book  detail table where acc number is eqaul to bpwtg5
                                        mycursor.execute("SELECT * FROM book_detail_table WHERE acc_no=%s" % bpwtg5)  # mycursor.execute is used to execute the query
                                        data_udt4 = mycursor.fetchall()
                                        print(data_udt4[0][2])  # select particular row & column in the fecthed data
                                            # fetched data contain the number of the stocks

                                        d_upd4 = data_udt4[0][2]-1  # less value by one in the number of the books
                                        print(d_upd4)
                                        # UPDATE book detail table and set no. of copies,-1 where acc no is equal to bpwtg5
                                        mycursor.execute("UPDATE book_detail_table SET no_of_copies=%s WHERE acc_no=%s" % (d_upd4, bpwtg5))
                                        con.commit()  # this is used to make the changes
                                    update4()  # here we call the update function

                                    def update5():  # update function to update the no. of stocks of the books in the book detail table
                                        # select all from book  detail table where acc number is eqaul to bpwtg6
                                        mycursor.execute("SELECT * FROM book_detail_table WHERE acc_no=%s" % bpwtg6)  # mycursor.execute is used to execute the query
                                        data_udt5 = mycursor.fetchall()
                                        print(data_udt5[0][2])  # select particular row & column in the fecthed data
                                            # fetched data contain the number of the stocks

                                        d_upd5 = data_udt5[0][2]-1  # less value by one in the number of the books
                                        print(d_upd5)
                                        # UPDATE book detail table and set no. of copies,-1 where acc no is equal to bpwtg6
                                        mycursor.execute("UPDATE book_detail_table SET no_of_copies=%s WHERE acc_no=%s" % (d_upd5, bpwtg6))
                                        con.commit()  # this is used to make the changes
                                    update5()  # here we call the update function
                                    sendmail2()
                                    messagebox.showinfo(" Message ", "Hi , (3) Books are sucessfully lended to the student")
                                    borrower_unique_id = bpltg
                                    acc_no_of_b1 = bpwtg4
                                    acc_no_of_b2 = bpwtg5
                                    acc_no_of_b3 = bpwtg6
                                    issue_date = vgcal4
                                    return_date = bpcvg1
                                    no_bk_stn_borrowed = vg

                                    insertdata3(borrower_unique_id, no_bk_stn_borrowed, acc_no_of_b1, acc_no_of_b2, acc_no_of_b3, issue_date, return_date)

                        bpbtn4 = t.Button(root4, text=" LEND IT ", bg="blue", fg="white", width=8, bd=2, command=lambda: ins(), font="Century 15 bold")
                        bpbtn4.place(x=300, y=650)  # button to lend the book

                        bpwbbtn5 = t.Button(root4, text=" HOME ", bg="blue", fg="white", bd=2, command=backbtn, font="Century 15 bold")
                        bpwbbtn5.place(x=800, y=650)  # button for going into the main window

                    else:
                        messagebox.showinfo("ALARM", "SOORY!, PLEASE INPUT THE ACC NO. ")  # error shown if user can't enter acc number of the book
        else:
            messagebox.showinfo("ALARM", "SORRY!, Student can't borrow more than 3 books at a time ")  # error shown if user enter more than 3
    root4.mainloop()  # to show the window, without this window can't be shown
