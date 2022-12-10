#main file
import sqlite3 as sl
import os
#program doesent neccesarily need to be object oriented, just has some structs
sl.
#path=str(os.getcwd+"/my-test.db").isfile()
if ():
    print("true")


    con = sl.connect('my-test.db')
    with con:
        con.execute("""
            CREATE TABLE BOOKS (
                name varchar(30),
                ISBN INTEGER PRIMARY KEY AUTOINCREMENT,
                genre varchar(30),
                stock_Count INTEGER,
                stock_Price INTEGER,
                sold_Price INTEGER,
                publisher_Cut INTEGER,
                publisher_ID INTEGER,
                num_Pages INTEGER,
                a_Fname varchar(20),
                a_Lname varchar(20)


            );
        """)
        con.execute("""
            CREATE TABLE PUBLISHERS (
                name varchar(30),
                address varchar(30),
                expire varchar(30),
                card_Num INTEGER,
                back_Num INTEGER,
                email varchar(30),
                phone_Num INTEGER,
                ID INTEGER RPRIMARY KEY


            );
        """)
        
        con.execute("""
            CREATE TABLE USERS (
                username varchar(30),
                address varchar(30),
                email varchar(30),
                expire varchar(30),
                card_Num INTEGER,
                back_Num INTEGER,
                user_ID INTEGER PRIMARY KEY
            );
        """)
        
        con.execute("""
            CREATE TABLE CART (
                cart_Num INTEGER PRIMARY KEY,
                user_ID INTEGER
            );
        """)
        
        con.execute("""
            CREATE TABLE ORDERS (
                order_Num INTEGER PRIMARY KEY,
                cart_Num INTEGER,
                user_ID INTEGER,
                expire varchar(30),
                card_Num INTEGER,
                back_Num INTEGER,
                address varchar(30)
            );
        """)
        
        con.execute("""
            CREATE TABLE ENTRY (
                order_Num INTEGER PRIMARY KEY,
                ISBN INTEGER,
                quantity INTEGER
            );
        """)

    #for testing we will have 20 books(starting at ISBN=1332),5 publishers(starting at id=0),4 users(starting at id=0),genre will be [suspense, action, adventure, horror,sad]
    con.execute("INSERT INTO BOOKS values('catcher and the rye',1332,'suspense',8,19,20,10,01,420,'Jerome','Salinger')")
    con.execute("INSERT INTO BOOKS values('mobey dick',1333,'action',9,18,21,11,02,4666,'Dun-in','Kruger')")
    con.execute("INSERT INTO BOOKS values('simple',1334,'adventure',8,16,17,16,03,555,'Ben','Jamin')")
    con.execute("INSERT INTO BOOKS values('rammatra',1335,'sad',7,15,16,22,04,435,'Ben','Jamin')")
    con.execute("INSERT INTO BOOKS values('rammatra',1336,'sad',6,13,31,33,01,2456,'Suma','Wrastlin')")
    con.execute("INSERT INTO BOOKS values('rammatra',1337,'sad',7,14,23,45,02,243,'Aasi','Mar')")
    con.execute("INSERT INTO BOOKS values('rammatra',1338,'sad',6,15,16,33,03,12,'Beo','Wulf')")
    con.execute("INSERT INTO BOOKS values('notebook',1339,'sad',5,15,17,25,04,433,'N/A','N/A')")
    con.execute("INSERT INTO BOOKS values('rammatra',1340,'sad',9,16,19,12,01,776,'Razz','Elazier')")
    con.execute("INSERT INTO BOOKS values('rammatra',1341,'sad',9,13,14,36,02,346,'El','Lagarto')")
    con.execute("INSERT INTO BOOKS values('rammatra',1342,'sad',8,12,15,74,03,123,'War','Forged')")
    con.execute("INSERT INTO BOOKS values('rammatra',1343,'sad',7,11,12,14,04,653,'Ben','Jamin')")
    con.execute("INSERT INTO BOOKS values('rammatra',1344,'sad',9,17,20,64,01,644,'Ben','Jamin')")
    con.execute("INSERT INTO BOOKS values('rammatra',1345,'sad',7,19,21,35,02,675,'Razz','Elazier')")
    con.execute("INSERT INTO BOOKS values('rammatra',1346,'sad',6,18,23,57,03,4321,'Denji','Pochita')")
    con.execute("INSERT INTO BOOKS values('rammatra',1347,'sad',5,16,17,86,04,1222,'Choles','Torol')")
    con.execute("INSERT INTO BOOKS values('rammatra',1348,'sad',9,15,22,45,01,1111,'Potas','Sium')")
    con.execute("INSERT INTO BOOKS values('rammatra',1349,'sad',8,13,15,24,02,121,'Ben','Jamin')")
    con.execute("INSERT INTO BOOKS values('rammatra',1350,'sad',7,15,17,46,03,321,'Denji','Pochita')")
    con.execute("INSERT INTO BOOKS values('rammatra',1351,'sad',6,16,19,23,04,567,'Aki','Hayakawa')")

    con.execute("INSERT INTO PUBLISHERS values('remingont.Pc','44 bakers street','07/23',112369549836,346,'remingont@gmail.com',6138859898,0)")
    con.execute("INSERT INTO PUBLISHERS values('guronimo.Pc','43 pencil ave.','01/23',471854087227,444,'guronimo@gmail.com',6134604267,1)")
    con.execute("INSERT INTO PUBLISHERS values('outpost.Pc','11 frog road','03/24',372818947195,532,'outpost@gmail.com',6132076392,2)")
    con.execute("INSERT INTO PUBLISHERS values('books4days.Pc','65 stag street','11/23',311470951372,122,'books4days@gmail.com',6134194170,3)")
    con.execute("INSERT INTO PUBLISHERS values('suplexepedia.Pc','876 rear street','04/26',847138088349,765,'suplexepedia@gmail.com',6136315312,4)")

    con.execute("INSERT INTO USERS values('BenConabree','9 roe ave','BC@gmail.com','05/24',966061692207,321,0)")
    con.execute("INSERT INTO USERS values('IndianaJones','5 piccolo way','IJ@gmail.com','03/24',279942305771,111,1)")
    con.execute("INSERT INTO USERS values('JustinTimberlake','66 avalon street','JT@gmail.com','06/22',207002434194,211,2)")
    con.execute("INSERT INTO USERS values('RomeoJuliet','344 soar ave.','RJ@gmail.com','07/23',844070300767,543,3)")
    con.execute("INSERT INTO USERS values('HomerSimpson','22 jim road','HS@gmail.com','09/22',012954054731,343,4)")

#with con:
#    data = con.execute("SELECT * FROM BOOKS WHERE num_Pages<=1000")
#    for row in data:
#        print(row)



while True:
    print("WELCOME TO OUR FUCKIN BOOKSTORE, BUY SHIT OR GET OUT\n owned by the CarlToad\n\nMainMenu\n\t1)Browse & add Books\n\t2)Cart\n\t3)Login & signup\n\t4)quit")
    sel = int(input("-->"))

    if (sel==1):
        #go into second loop where we look at books using query
        while True:
            print("please choose the criteria you want to filter by\n\n\t1)Book Name\n\t2)Author Last Name\n\t3)Genre\n\t4)ISBN")

            searchFilt = int(input("-->"))
            print("type search...\n")
            searchStr = str(input("-->"))
            if (searchFilt==1):
                table = con.execute("SELECT * FROM BOOKS WHERE name="+searchStr)
                break
            elif (searchFilt==2):
                table = con.execute("SELECT * FROM BOOKS WHERE a_Lname="+searchStr)
                break
            elif(searchFilt==3):
                table = con.execute("SELECT * FROM BOOKS WHERE genre="+searchStr)
                break
            elif(searchFilt==4):
                table = con.execute("SELECT * FROM BOOKS WHERE ISBN="+searchStr)
                break
            
            

            
        with con:
            for row in table:
                print(row)
    

    if (sel==4):
        break
    






#cleanup when alls done
con.execute("DROP table *")