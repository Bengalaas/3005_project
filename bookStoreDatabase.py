#main file
import sqlite3 as sl
import os
import string
#program doesent neccesarily need to be object oriented, just has some structs

#path=str(os.getcwd+"/my-test.db").isfile()
numUsers=6
current_UserID = -1
userCarts = [[['1332',3],['1337',2]],[['1337',5],['1339',1],['1351',1]],[],[],[],[]]
#con = sl.connect('my-test.db')
#reset = str(input("RESET DATABASE?(y/n)-->"))
if (True):
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
                card_Num INTEGER,
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
                card_Num INTEGER,
                user_ID INTEGER PRIMARY KEY
            );
        """)
        
        #con.execute("""
        #    CREATE TABLE CART (
        #        cart_Num INTEGER PRIMARY KEY,
        #        user_ID INTEGER
        #    );
        #""")
        #cart_Num INTEGER,
        con.execute("""
            CREATE TABLE ORDERS (
                order_Num INTEGER PRIMARY KEY,
                user_ID INTEGER,
                card_Num INTEGER,
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
    con.execute("INSERT INTO BOOKS values('catcher and the rye',1332,'suspense',21,19,20,10,01,420,'Jerome','Salinger')")
    con.execute("INSERT INTO BOOKS values('mobey dick',1333,'action',21,18,21,11,02,4666,'Dun-in','Kruger')")
    con.execute("INSERT INTO BOOKS values('simple',1334,'adventure',23,16,17,16,03,555,'Ben','Jamin')")
    con.execute("INSERT INTO BOOKS values('one and done',1335,'horror',44,15,16,22,04,435,'Ben','Jamin')")
    con.execute("INSERT INTO BOOKS values('stone',1336,'sad',12,13,31,33,01,2456,'Suma','Wrastlin')")
    con.execute("INSERT INTO BOOKS values('beggar',1337,'suspense',11,14,23,45,02,243,'Aasi','Mar')")
    con.execute("INSERT INTO BOOKS values('Chimarvamidium',1338,'action',45,15,16,33,03,12,'Beo','Wulf')")
    con.execute("INSERT INTO BOOKS values('notebook',1339,'adventure',23,15,17,25,04,433,'N/A','N/A')")
    con.execute("INSERT INTO BOOKS values('deathbrand',1340,'horror',43,16,19,12,01,776,'Razz','Elazier')")
    con.execute("INSERT INTO BOOKS values('dwarves',1341,'sad',15,13,14,36,02,346,'El','Lagarto')")
    con.execute("INSERT INTO BOOKS values('king',1342,'suspense',34,12,15,74,03,123,'War','Forged')")
    con.execute("INSERT INTO BOOKS values('olaf and the dragon',1343,'action',33,11,12,14,04,653,'Ben','Jamin')")
    con.execute("INSERT INTO BOOKS values('on oblivion',1344,'adventure',54,17,20,64,01,644,'Ben','Jamin')")
    con.execute("INSERT INTO BOOKS values('remanada',1345,'horror',32,19,21,35,02,675,'Razz','Elazier')")
    con.execute("INSERT INTO BOOKS values('shadowmarks',1346,'sad',12,18,23,57,03,4321,'Denji','Pochita')")
    con.execute("INSERT INTO BOOKS values('sithis',1347,'suspense',51,16,17,86,04,1222,'Choles','Torol')")
    con.execute("INSERT INTO BOOKS values('the art of war magic',1348,'action',21,15,22,45,01,1111,'Potas','Sium')")
    con.execute("INSERT INTO BOOKS values('the black arrow',1349,'adventure',32,13,15,24,02,121,'Ben','Jamin')")
    con.execute("INSERT INTO BOOKS values('scourge',1350,'horror',13,15,17,46,03,321,'Denji','Pochita')")
    con.execute("INSERT INTO BOOKS values('The Song of Pelinal, Book IV',1351,'sad',42,16,19,23,04,567,'Aki','Hayakawa')")

    con.execute("INSERT INTO PUBLISHERS values('remingont.Pc','44 bakers street',112369549836,'remingont@gmail.com',6138859898,0)")
    con.execute("INSERT INTO PUBLISHERS values('guronimo.Pc','43 pencil ave.',471854087227,'guronimo@gmail.com',6134604267,1)")
    con.execute("INSERT INTO PUBLISHERS values('outpost.Pc','11 frog road',372818947195,'outpost@gmail.com',6132076392,2)")
    con.execute("INSERT INTO PUBLISHERS values('books4days.Pc','65 stag street',311470951372,'books4days@gmail.com',6134194170,3)")
    con.execute("INSERT INTO PUBLISHERS values('suplexepedia.Pc','876 rear street',847138088349,'suplexepedia@gmail.com',6136315312,4)")

    con.execute("INSERT INTO USERS values('BenConabree','9 roe ave','BC@gmail.com',966061692207,0)")
    con.execute("INSERT INTO USERS values('JoeShmoo','4 sill ave','JS@gmail.com',162064667645,1)")
    con.execute("INSERT INTO USERS values('IndianaJones','5 piccolo way','IJ@gmail.com',279942305771,2)")
    con.execute("INSERT INTO USERS values('JustinTimberlake','66 avalon street','JT@gmail.com',207002434194,3)")
    con.execute("INSERT INTO USERS values('RomeoJuliet','344 soar ave.','RJ@gmail.com',844070300767,4)")
    con.execute("INSERT INTO USERS values('HomerSimpson','22 jim road','HS@gmail.com',012954054731,5)")

    #con.execute("INSERT INTO CART values(0,1)")
    #con.execute("INSERT INTO CART values(1,2)")
    #con.execute("INSERT INTO CART values(2,3)")
    #con.execute("INSERT INTO CART values(3,4)")
    #con.execute("INSERT INTO CART values(4,5)")
#with con:
#    data = con.execute("SELECT * FROM BOOKS WHERE num_Pages<=1000")
#    for row in data:
#        print(row)



while True:
    if (current_UserID==0):
        print("WELCOME TO YOUR BOOKSTORE\n owned by the CarlToad\n\nMainMenu\n\t1)Browse & add Books\n\t2)Cart\n\t3)Login & signup\n\t4)quit\n\t5)see Stats")
        table = con.execute("SELECT username FROM USERS WHERE user_ID={}".format(current_UserID))
        print("user:"+str(table.fetchmany()[0][0]))
    else:
        print("WELCOME TO OUR BOOKSTORE\n owned by the CarlToad\n\nMainMenu\n\t1)Browse & add Books\n\t2)Cart\n\t3)Login & signup\n\t4)quit")
        if not (current_UserID == -1):
            table = con.execute("SELECT username FROM USERS WHERE user_ID={}".format(current_UserID))
            print("user:"+str(table.fetchmany()[0][0]))
        else: 
            print("user: no user")
    sel = int(input("-->"))

    if (sel==1):
        #go into second loop where we look at books using query
        while True:
            print("please choose the criteria you want to filter by\n\n\t1)Book Name\n\t2)Author Last Name\n\t3)Genre\n\t4)ISBN\n\t5)leave")

            searchFilt = int(input("-->"))
            print("type search with '', ex. 'catcher and the rye' or 'suspense'...\n")
            
            if (searchFilt==1):
                searchStr = str(input("book name-->")).lower()
                table = con.execute("SELECT name,ISBN,genre,sold_Price,num_Pages,a_fname,a_lname FROM BOOKS WHERE name={}".format(searchStr))
                with con:
                    print("output...")
                    print('   name   |   ISBN   |  genre   |  price | pages | author name')
                    for row in table:
                        print(row)
                
            elif (searchFilt==2):
                searchStr = str(input("Authors Last Name-->"))
                table = con.execute("SELECT name,ISBN,genre,sold_Price,num_Pages,a_fname,a_lname FROM BOOKS WHERE a_Lname={}".format(searchStr))
                with con:
                    print("output...")
                    print('   name   |   ISBN   |  genre   |  price | pages | author name')
                    for row in table:
                        print(row)
                
            elif(searchFilt==3):
                searchStr = str(input("genre[suspense, action, adventure, horror,sad]-->")).lower()
                table = con.execute("SELECT name,ISBN,genre,sold_Price,num_Pages,a_fname,a_lname FROM BOOKS WHERE genre={}".format(searchStr))
                with con:
                    print("output...")
                    print('   name   |   ISBN   |  genre   |  price | pages | author name')
                    for row in table:
                        print(row)
                
            elif(searchFilt==4):
                searchStr = str(input("ISBN(ex. '1334')-->"))
                table = con.execute("SELECT name,ISBN,genre,sold_Price,num_Pages,a_fname,a_lname FROM BOOKS WHERE ISBN={}".format(searchStr))
                with con:
                    print("output...")
                    print('   name   |   ISBN   |  genre   |  price | pages | author name')
                    for row in table:
                        print(row)
            elif(searchFilt==5):
                break
            else:
                print("make a valid selection")
            while (True):
                    print("\ninput the ISBN of a book(ex. '1123') and quantity(ex. 5) you would like to add to your cart if any or q to quit back to search")
                    isbnInp = str(input("ISBN-->"))
                    if isbnInp=="q":
                        break
                    quantInp = int(input("quantity-->"))
#work in to add to cartTODO
                    print("adding the following to your cart")
                    table = con.execute("SELECT name,ISBN,genre,sold_Price,num_Pages,a_fname,a_lname FROM BOOKS WHERE ISBN="+isbnInp)
                    with con:
                        print('   name   |   ISBN   |  genre   |  price | pages | author name')
                        for row in table:
                            print(row)
                            print("\tx"+str(quantInp)+"\n")
                    

            
            

            
        
    
    if (sel==2):
        break
    if (sel==3):
        #login signup
        print("select user from...")
        table = con.execute("SELECT username FROM USERS")
        k=0
        with con:
            for row in table:
                print(str(k)+") ",end="")
                print(row[0])
                k+=1
        print("or n, for a new user")
        user = (input("-->"))
        if (user=="n"):
            username = (input("username?-->"))
            address = (input("address?-->"))
            email = (input("email?-->"))
            card_Num = int(input("credit card number?-->"))
            #TODO, check for overlap and other users with the same email
            con.execute("INSERT INTO USERS VALUES ({},{},{},{},{})".format(username,address,email,card_Num,numUsers))

            user=numUsers
            numUsers+=1
        current_UserID=int(user)
    if (sel==4):
        break
    if (sel==5 & current_UserID==0):
        print("Admin functions")

    






#cleanup when alls done
#con.execute("DROP table *")