import sqlite3

# define a function to create a database
def createDB():
    # creating the connection
    db = sqlite3.connect("jobs.db")

    #Creating Regestration Table
    #db.execute("create table RegTable(ID INTEGER PRIMARY KEY AUTOINCREMENT,"
     #          "name text, username text ,password text, email text,phone text, gender text)")

    db.execute("INSERT INTO RegTable(name, username, password,email, phone, gender) "
               "VALUES('Rahela', 'rahelaraha', '12345', 'rahela.jawadi@gmail.com', '0780092896','male');")
    #create table
    #db.execute("create table userReg(ID INTEGER PRIMARY KEY AUTOINCREMENT,"
    #"name, password )")

    #db.execute("create table AdLogin(ID INTEGER PRIMARY KEY AUTOINCREMENT,"
    #"name, password )")

    #db.execute("create table jobInfo(ID INTEGER PRIMARY KEY AUTOINCREMENT,"
     #          "title text, organization text ,details text, open text, close text)")

    # insert values
    db.execute("INSERT INTO jobInfo (title, organization,details, open, close) "
               "VALUES('Software Enginier ', 'SYPA', 'Bachelor Degree', '6/30/2020', '7/30.2020');")


    # insert values
    #db.execute( "INSERT INTO AdLogin (name, password) "
    #"VALUES('Admin', '12345');")

    db.commit()

    cursor = db.execute("select * from jobInfo")
    for i in cursor:
        print(i)

    db.close()



createDB()