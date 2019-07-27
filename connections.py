import mysql.connector# to connect with datbase we need to import this module
global mycursor,con # define cursor as globaly

def myconnections():#my connection function
    global mycursor, con
    con = mysql.connector.connect(user='root', password='ironheartsachu', host='localhost')
    mycursor = con.cursor()
    mycursor.execute("USE librarylbs")

    return con, mycursor
