import tkinter as t  # import tkinter library  for GUI as t
from tkcalendar import DateEntry  # from tkcalender library import Date Entry module
import interface_window  # import final_library_for_project module into this module to run in this module
import os  # this is import to change the directory
from tkinter import messagebox  # from tkinter library import messagebox module to show messages
from tkcalendar import Calendar  # from tkcalender import calender
from datetime import date  # from datetime module import date
from PIL import Image, ImageTk  # used to import the photo in the background
global con, mycursor
import connections as c  # import connections module as c
con, mycursor = c.myconnections()

def rpw(top):
    # returning process window main function

    top.destroy()  # to destroy the main library window
    os.chdir("C:\\LibraryProject\\images\\background_images\\")  # here we change the directory
    root7 = t.Tk()  # through this we create the  returning process main window
    root7.title("Returning window")  # title of the returning process  window
    screen_width = root7.winfo_screenwidth()  # by this we can get the width of the tkinter window
    screen_height = root7.winfo_screenheight()  # by this we can get the height of the tkinter window
    dim1 = str(screen_width)  # here we store the screen width of the tkinter window as a string in the dim1 variable
    dim2 = str(screen_height)  # here we store the screen height of the tkinter window as a string in the dim1 variable
    dim3 = "%sx%s" % (dim1, dim2)  # in the dim3 variable we set the dimension of the tkinter window
    root7.geometry(dim3)  # Dimension of the returning window
    root7.state('zoomed')
    # rpwl= retuning process label
    rpwl_1 = t.Label(root7, text="RETURNING PROCESS", font="Century 12 bold")
    rpwl_1.place(x=600)  # place of the label in the returning window

    rpwl1 = t.Label(root7, text="STUDENT UNIQUE ID : ", font="Century 12 bold")
    rpwl1.place(x=150, y=100)  # place of the label in the returning window

    rpwt1 = t.Entry(root7, width=40)  # Entry box in the root7 window with width = 40
    rpwt1.place(x=400, y=105)  # place of the text in the returning window

# we can't call another function into directly into this function so, we use lambda to calling in this function
    def calan():
        def print_sel():
            global dobvg
            dobvg = cal.selection_get()
           # print(cal.selection_get())

            date1 = t.Label(root7, text=" :    %s" % dobvg, font="Century 15 bold", fg="blue")

            date1.place(x=890, y=110)
            top.destroy()

        top = t.Toplevel(root7)

        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=2019, month=3, day=2)
        cal.pack(fill="both", expand=True)
        t.Button(top, text="OK", command=print_sel).pack()

    rpwlabel = t.Label(root7, text="LAST BORROWED BOOK DATE ", font="Century 10 bold", fg="black")
    rpwlabel.place(x=770, y=80)

    calbtnb1 = t.Button(root7, text=' CALENDER ', command=calan, font="Century 10 bold")  # ,bg="seagreen",fg="white", width=15
    calbtnb1.place(x=750, y=110)

    def backbtn():  # back button function

        root7.destroy()  # here we destroy returning process window
        interface_window.mainwindow()  # here we call the returning process window

    rpwbtn2 = t.Button(root7, text="HOME ", bg="black", fg="white", command=backbtn, font="Century 10 bold")
    rpwbtn2.place(x=650, y=35)  # place of the button in the returning process window

    def rp_fun(): # returning process information dispaly function
        rptg1 = rpwt1.get()  # rptg1 = return process text get 1-> variable(1) = rpwt1.get()-returning process window text 1

        if len(rptg1) > 0:  # if the length of variable(1) is gretaer than zero than it execute below satements
            query3 = "SELECT * FROM borrowing_process_table WHERE borrower_unique_id ='%s'  AND issue_date ='%s'" % (rptg1, dobvg)
            mycursor.execute(query3)  # through this we can execute the query3
            data1 = mycursor.fetchall()  # fetched data store in data1, data is fetched with the help of mycursor.fetchall()
            print(data1)
            #print(data1)
            d1 = data1[0][0]  # now d1 contain data1           print(d1)
            print(d1)
            d3 = data1[0][4]
            print(d3)
            if rptg1 == d1 or dobvg == d3:  # in the d1 data we select particular row and column  i.e., borrower unique
                    # select no of the book that stn had borrowed from the borrowing process table where unique id is rptg1
                    query2 = "SELECT no_bk_stn_borrowed FROM borrowing_process_table WHERE borrower_unique_id ='%s'AND issue_date='%s'" % (rptg1, dobvg)
                    mycursor.execute(query2)  # this is used to execute the query2
                    data2 = mycursor.fetchall()  # by this we fetch the data & fetched data store data2
                    d2 = data2[0][0]  # in the contain d2 data we select particular row and column
                    print(d2)                  # d2 contain the number of book that student had borrowed

                    if d2 == 1:  # if d2 is equal to one then it execute  the below code
                        # select all from borrowing_process_table where borrower unique id is rptg1
                        query = "SELECT * FROM borrowing_process_table WHERE borrower_unique_id ='%s' AND issue_date='%s'" % (rptg1,  dobvg)
                        mycursor.execute(query)  # this is used to execute to query
                        data3 = mycursor.fetchall()  # this is used to fecth the data from the database
                        # data3 contain all the information of book that student had boorowed
                        #print(data3)

                        for i in data3:  # apply for loop in the data3 to print the borrower details in the window
                            # apply for loop in tables of the data3 and fetch the details and display into existing window



                            rpwl2 = t.Label(root7, text="Book borrowed detail of Student   ", font="Century 15 bold", fg="black")
                            rpwl2.place(x=350, y=140)

                            rpwl3 = t.Label(root7, text="(1). ACC NO.                       "
                                                        "  :", font="Century 12 bold", fg="black")
                            rpwl3.place(x=150, y=200)
                            ac_no = i[1]
                            rpwl4 = t.Label(root7, font="Century 12 bold", fg="black")
                            rpwl4.configure(text=ac_no)
                            rpwl4.place(x=700, y=200)

                            lctn = "C:\\LibraryProject\\images\\book_label\\%s.png" % ac_no
                            print(lctn)
                            img = ImageTk.PhotoImage(Image.open(lctn))
                            canvas = t.Canvas(height=250,width=200)

                            canvas.create_image(0, 0, image=img)
                            canvas.image = img
                            rpw__l5 = t.Label(root7, image=img)
                            rpw__l5.place(x=900, y=200)

                            rpwl5 = t.Label(root7, text="(2). RETURN DATE.            "
                                                        " :", font="Century 12 bold", fg="black")
                            rpwl5.place(x=150, y=270)

                            a = i[5]
                            rpwl6 = t.Label(root7, font="Century 12 bold", fg="black")
                            rpwl6.configure(text=i[5])
                            rpwl6.place(x=700, y=270)

                            rpwl27 = t.Label(root7, text="               TODAY DATE            :", font="Century 12 bold", fg="black")
                            rpwl27.place(x=150, y=340)

                            cal = DateEntry(root7, width=12, background='darkblue', foreground='white', borderwidth=2, bd=3)
                            cal.place()
                            vgcal = cal.get_date()
                            vgcaltd = str(vgcal)
                            print(vgcal)
                            rpwl_27 = t.Label(root7, text=vgcal, font="Century 12 bold", fg="black")
                            rpwl_27.place(x=508, y=340)

                            yr = int(a[0]+a[1]+a[2]+a[3])
                            yr1 = int(vgcaltd[0]+vgcaltd[1]+vgcaltd[2]+vgcaltd[3])

                            mn1 = int(a[5]+a[6])
                            mn2 = int(vgcaltd[5]+vgcaltd[6])

                            dt1 = int(a[8]+a[9])
                            dt2 = int(vgcaltd[8]+vgcaltd[9])

                            d0 = date(yr1, mn2, dt2)
                            d1 = date(yr, mn1, dt1)
                            delta = d0 - d1
                            days = delta.days

                            print("days : ", days)

                            if days <= 0:

                                rpwl30 = t.Label(root7, text="STUDENT DON'T HAVE FINE   ", font="Century 12 bold", fg="black")
                                rpwl30.place(x=300, y=420)

                            else:
                                rpwl31 = t.Label(root7, text="STUDENT  HAVE FINE   ", font="Century 12 bold", fg="black")
                                rpwl31.place(x=300, y=420)
                                fine = days*5

                                rpwl__6 = t.Label(root7, font="Century 12 bold", fg="black")
                                rpwl__6.configure(text=":  %s  INR" % fine)
                                rpwl__6.place(x=800, y=420)

                            def update():  # update function for the update the number of the stock in the book detail table
                                # when we update the data this message is shown that book is sucessfully return to the library
                                messagebox.showinfo("Message", " Book is sucessfully return to the Library ")  # when student click on return button  this message shown after click of return button
                                # select all from the book detail table where acc_no is ac_no
                                mycursor.execute("SELECT * FROM book_detail_table WHERE acc_no=%s" % ac_no)
                                data_udt = mycursor.fetchall()
                                #print(data_udt[0][2])

                                # data_udt[0][2] we doing this to select no_of_copies in the book detail table

                                d_upd = data_udt[0][2]+1  # we add 1 in the selected data means we increment no of copies by one, by doing this
                                #print(d_upd)         # & store in the d_upd

                                # update book detail table set no of copies -1 where acc no is ac_no
                                mycursor.execute("UPDATE book_detail_table SET no_of_copies=%s WHERE acc_no=%s" % (d_upd, ac_no))
                                con.commit()  # this is used to make the changes

                            rpwbtn3 = t.Button(root7, text="RETURN BOOK", font="Century 10 bold", fg="white", bg="blue", command=update)
                            rpwbtn3.place(x=300, y=500)  # return book button

                            # anbwbbtn = return book  window back button
                            rpwbtn4 = t.Button(root7, text="BACK ", bg="blue", fg="white", command=backbtn, font="Century 10 bold")
                            rpwbtn4.place(x=750, y=500)

                    if d2 == 2:  # if d2 is equal to two then it execute  the below code
                        # select all from borrowing_process_table where borrower unique id is rptg1
                        query = "SELECT * FROM borrowing_process_table WHERE borrower_unique_id ='%s' AND issue_date='%s'" % (rptg1,  dobvg)
                        mycursor.execute(query)  # this is used to execute to query
                        data4 = mycursor.fetchall()  # this is used to fecth the data from the database
                        # data4 contain all the information of book that student had boorowed

                        for i in data4:  # apply for loop in the data4 to print the borrower details in the window
                            # apply for loop in tables of the data4 and fetch the details and display into existing window

                            rpwl7 = t.Label(root7, text="Book borrowed detail of Student   ", font="Century 15 bold", fg="black")
                            rpwl7.place(x=350, y=140)

                            rpwl8 = t.Label(root7, text="(1). ACC NO.(Book(1))               "
                                                        "          :", font="Century 12 bold", fg="black")
                            rpwl8.place(x=150, y=200)

                            ac_no1 = i[1]
                            rpwl9 = t.Label(root7, font="Century 12 bold", fg="black")
                            rpwl9.configure(text=ac_no1)
                            rpwl9.place(x=700, y=200)

                            rpwl10 = t.Label(root7, text="(2). ACC NO.(Book(2))               "
                                                        "          :", font="Century 12 bold", fg="black")
                            rpwl10.place(x=150, y=250)

                            ac_no2 = i[2]
                            rpwl11 = t.Label(root7, font="Century 12 bold", fg="black")
                            rpwl11.configure(text=ac_no2)
                            rpwl11.place(x=700, y=250)

                            rpwl14 = t.Label(root7, text="(3). RETURN DATE.             "
                                                        "              :", font="Century 12 bold", fg="black")
                            rpwl14.place(x=150, y=300)

                            b = i[5]
                            rpwl15 = t.Label(root7, font="Century 12 bold", fg="black")
                            rpwl15.configure(text=i[5])
                            rpwl15.place(x=700, y=300)

                            rpwl28 = t.Label(root7, text="               TODAY DATE             "
                                                        " :", font="Century 12 bold", fg="black")
                            rpwl28.place(x=150, y=360)

                            cal2 = DateEntry(root7, width=12, background='darkblue', foreground='white', borderwidth=2, bd=3)
                            cal2.place()
                            vgcal2 = cal2.get_date()  # vgcal2 = value get for calender 2
                            vgcal2td = str(vgcal2)
                            rpwl_28 = t.Label(root7, text=vgcal2, font="Century 12 bold", fg="black")
                            rpwl_28.place(x=508, y=365)

                            yr = int(b[0]+b[1]+b[2]+b[3])
                            yr1 = int(vgcal2td[0]+vgcal2td[1]+vgcal2td[2]+vgcal2td[3])

                            mn1 = int(b[5]+b[6])
                            mn2 = int(vgcal2td[5]+vgcal2td[6])

                            dt1 = int(b[8]+b[9])
                            dt2 = int(vgcal2td[8]+vgcal2td[9])

                            d0 = date(yr1, mn2, dt2)
                            d1 = date(yr, mn1, dt1)
                            delta = d0 - d1
                            days = delta.days

                            if days <= 0:
                                rpwl30 = t.Label(root7, text="STUDENT DON'T HAVE FINE   ", font="Century 12 bold", fg="black")
                                rpwl30.place(x=300, y=420)

                            else:
                                rpwl31 = t.Label(root7, text="STUDENT  HAVE FINE   ", font="Century 12 bold", fg="black")
                                rpwl31.place(x=300, y=420)
                                fine = days*5

                                rpwl__6 = t.Label(root7, font="Century 12 bold", fg="black")
                                rpwl__6.configure(text="  %s  INR" % fine)
                                rpwl__6.place(x=800, y=420)

                            def update1():  # update function for the update the number of the stock in the book detail table
                                # when we update the data this message is shown that (2). books is sucessfully return to the library
                                messagebox.showinfo("Message", " (2). Books are sucessfully return to the Library ")  # when student click on return button  this message shown after click of return button
                                mycursor.execute("SELECT * FROM book_detail_table WHERE acc_no=%s" % ac_no1)
                                # select all from the book detail table where acc_no is ac_no
                                data_udt1 = mycursor.fetchall()
                                print(data_udt1[0][2])
                                # data_udt[0][2] we doing this to select no_of_copies in the book detail table
                                d_upd1 = data_udt1[0][2]+1      # we add 1 in the selected data means we increment no of copies by one, by doing this
                                        # & store in the d_upd1
                                print(d_upd1)
                                # update book detail table set no of copies -1 where acc no is ac_no
                                mycursor.execute("UPDATE book_detail_table SET no_of_copies=%s WHERE acc_no=%s" % (d_upd1, ac_no1))
                                con.commit()  # this is used to make changes

                                #  second book update entry
                                mycursor.execute("SELECT * FROM book_detail_table WHERE acc_no=%s" % ac_no2)
                                data_udt2 = mycursor.fetchall()
                                print(data_udt2[0][2])

                                d_upd2 = data_udt2[0][2]+1
                                print(d_upd2)

                                mycursor.execute("UPDATE book_detail_table SET no_of_copies=%s WHERE acc_no=%s" % (d_upd2, ac_no2))
                                con.commit()

                            rpwbtn5 = t.Button(root7, text="RETURN BOOKS", font="Century 10 bold", fg="white", bg="blue", command=update1)
                            rpwbtn5.place(x=300, y=500)

                            # anbwbbtn = return book  window back button
                            rpwbtn6 = t.Button(root7, text="BACK ", bg="blue", fg="white", command=backbtn, font="Century 10 bold")
                            rpwbtn6.place(x=750, y=500)

                    if d2 == 3:  # d2 contain the number of book that student had borrowed
                                # if d2 is equal to three then it execute  the below code

                        query = "SELECT * FROM borrowing_process_table WHERE borrower_unique_id ='%s' AND issue_date='%s'" % (rptg1,  dobvg)
                        mycursor.execute(query)
                        data5 = mycursor.fetchall()

                        # data3 contain all the information of book that student had boorowed
                        for i in data5:
                            # apply for loop in tables of the data3 and fetch the details and display into existing window

                            rpwl16 = t.Label(root7, text="Book borrowed detail of Student   ", font="Century 15 bold", fg="black")
                            rpwl16.place(x=350, y=140)

                            rpwl17 = t.Label(root7, text="(1). ACC NO.(Book(1))              "
                                                        "          :", font="Century 12 bold", fg="black")
                            rpwl17.place(x=150, y=200)

                            ac_no3 = i[1]
                            rpwl18 = t.Label(root7, font="Century 12 bold", fg="black")
                            rpwl18.configure(text=ac_no3)
                            rpwl18.place(x=700, y=200)

                            rpwl19 = t.Label(root7, text="(2). ACC NO.(Book(2))              "
                                                        "          :", font="Century 12 bold", fg="black")
                            rpwl19.place(x=150, y=250)

                            ac_no4 = i[2]

                            rpwl20 = t.Label(root7, font="Century 12 bold", fg="black")
                            rpwl20.configure(text=ac_no4)
                            rpwl20.place(x=700, y=250)

                            rpwl21 = t.Label(root7, text="(3). ACC NO.(Book(3))              "
                                                        "          :", font="Century 12 bold", fg="black")
                            rpwl21.place(x=150, y=300)

                            ac_no5 = i[3]
                            rpwl22 = t.Label(root7, font="Century 12 bold", fg="black")
                            rpwl22.configure(text=ac_no5)
                            rpwl22.place(x=700, y=300)

                            rpwl25 = t.Label(root7, text="(4). RETURN DATE.               "
                                                        "           :", font="Century 12 bold", fg="black")
                            rpwl25.place(x=150, y=350)
                            c = i[5]
                            rpwl26 = t.Label(root7, font="Century 12 bold", fg="black")
                            rpwl26.configure(text=i[5])
                            rpwl26.place(x=700, y=350)

                            rpwl29 = t.Label(root7, text="                  TODAY DATE             "
                                                        " :", font="Century 12 bold", fg="black")
                            rpwl29.place(x=150, y=420)

                            cal3 = DateEntry(root7, width=12, background='darkblue', foreground='white', borderwidth=2, bd=3)
                            cal3.place()
                            vgcal3 = cal3.get_date()  # vgcal3 = value get of the calender 3
                            vgcal3td = str(vgcal3)
                            rpwl_29 = t.Label(root7, text=vgcal3, font="Century 12 bold", fg="black")
                            rpwl_29.place(x=500, y=420)

                            yr = int(c[0]+c[1]+c[2]+c[3])
                            yr1 = int(vgcal3td[0]+vgcal3td[1]+vgcal3td[2]+vgcal3td[3])

                            mn1 = int(c[5]+c[6])
                            mn2 = int(vgcal3td[5]+vgcal3td[6])

                            dt1 = int(c[8]+c[9])
                            dt2 = int(vgcal3td[8]+vgcal3td[9])

                            d0 = date(yr1, mn2, dt2)
                            d1 = date(yr, mn1, dt1)
                            delta = d0 - d1
                            days = delta.days

                            if days <= 0:
                                rpwl30 = t.Label(root7, text="STUDENT DON'T HAVE FINE   ", font="Century 12 bold", fg="black")
                                rpwl30.place(x=300, y=500)
                            else:
                                rpwl31 = t.Label(root7, text="STUDENT  HAVE FINE   ", font="Century 12 bold", fg="black")
                                rpwl31.place(x=300, y=500)
                                fine = days*5

                                rpwl__6 = t.Label(root7, font="Century 12 bold", fg="black")
                                rpwl__6.configure(text="  %s  INR" % fine)
                                rpwl__6.place(x=800, y=500)

                            def update2():  # update function for the update the number of the stock in the book detail table

                                # when we update the data this message is shown that (3). books is sucessfully return to the library
                                messagebox.showinfo("Message", " (3). Books are sucessfully return to the Library")
                                # select all from the book detail table where acc_no is ac_no

                                mycursor.execute("SELECT * FROM book_detail_table WHERE acc_no=%s" % ac_no3)
                                data_udt3 = mycursor.fetchall()
                                print(data_udt3[0][2])

                                # data_udt[0][2] we doing this to select no_of_copies in the book detail table
                                d_upd3 = data_udt3[0][2]+1  # we add 1 in the selected data means we increment no of copies by one, by doing this
                                # & store in the d_upd
                                print(d_upd3)

                                # update book detail table set no of copies -1 where acc no is ac_no
                                mycursor.execute("UPDATE book_detail_table SET no_of_copies=%s WHERE acc_no=%s" % (d_upd3, ac_no3))
                                con.commit()
                                #  second book update entry
                                mycursor.execute("SELECT * FROM book_detail_table WHERE acc_no=%s" % ac_no4)
                                data_udt4 = mycursor.fetchall()
                                print(data_udt4[0][2])

                                d_upd4 = data_udt4[0][2]+1
                                print(d_upd4)

                                mycursor.execute("UPDATE book_detail_table SET no_of_copies=%s WHERE acc_no=%s" % (d_upd4, ac_no4))
                                con.commit()
                                # third book update stock
                                mycursor.execute("SELECT * FROM book_detail_table WHERE acc_no=%s" % ac_no5)
                                data_udt5 = mycursor.fetchall()
                                print(data_udt5[0][2])

                                d_upd5 = data_udt5[0][2]+1
                                print(d_upd5)

                                mycursor.execute("UPDATE book_detail_table SET no_of_copies=%s WHERE acc_no=%s" % (d_upd5, ac_no5))
                                con.commit()

                            rpwbtn7 = t.Button(root7, text="RETURN BOOKS", font="Century 10 bold", fg="white", bg="blue", command=update2)
                            rpwbtn7.place(x=300, y=580)  # return book button

                            # anbwbbtn = return book  window back button
                            rpwbtn8 = t.Button(root7, text="BACK ", bg="blue", fg="white", command=backbtn, font="Century 10 bold")
                            rpwbtn8.place(x=750, y=580)
            else:
                messagebox.showinfo("warning", "This Student had not borrowed any book or Book Issued Date is incorrect")

        else:
            messagebox.showinfo("Warning", "Input Student Unique id.")  # this message is shown if user won't Enter student unique id
    rpwbtn1 = t.Button(root7, text="CONFIRM", font="Century 10 bold", fg="white", bg="blue", command=rp_fun)
    rpwbtn1.place(x=1150, y=105)  # place of the button in the returning process window
    root7.mainloop()  # this is used for showing the window in the screeen

