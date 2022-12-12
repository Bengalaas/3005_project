#main file
import sqlite3 as sl
import os
import string
import math
#program doesent neccesarily need to be object oriented, just has some structs

#path=str(os.getcwd+"/my-test.db").isfile()
signedIn = False
current_UserID = None
userCarts = [[['1332',3],['1337',2]],[['1337',5],['1339',1],['1351',1]],[],[],[],[['1337',20]]]

#con = sl.connect('my-test.db')
#reset = str(input("RESET DATABASE?(y/n)-->"))
con = sl.connect('my-test.db')
reset = str(input("INIT NEW DATABASE?(y/n)-->"))
if (reset=="y"):
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
                entry_Num INTEGER PRIMARY KEY,
                order_Num INTEGER,
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
tab = con.execute("SELECT COUNT(*) FROM USERS")
numUsers = (tab.fetchall()[0][0])
for x in range(numUsers-len(userCarts)):
    userCarts.append([])
print(str(numUsers) + " users")

while True:
    if (current_UserID==0):
        print("\n\nWELCOME TO YOUR BOOKSTORE\n owned by the CarlToad\n\nMainMenu\n\t1)Browse & add Books\n\t2)Cart\n\t3)Login & signup\n\t4)quit\n\t5)see Stats")
        table = con.execute("SELECT username FROM USERS WHERE user_ID={}".format(current_UserID))
        print("user:"+str(table.fetchmany()[0][0]))
    else:
        print("WELCOME TO OUR BOOKSTORE\n owned by the CarlToad\n\nMainMenu\n\t1)Browse & add Books\n\t2)Cart\n\t3)Login & signup\n\t4)quit")
        if (signedIn):
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
                table = con.execute("SELECT name,ISBN,genre,sold_Price,num_Pages,a_fname,a_lname,stock_Count FROM BOOKS WHERE name={}".format(searchStr))
                with con:
                    print("output...")
                    print('   name   |   ISBN   |  genre   |  price | pages | author name | current Stock')
                    for row in table:
                        print(row)
                
            elif (searchFilt==2):
                searchStr = str(input("Authors Last Name-->"))
                table = con.execute("SELECT name,ISBN,genre,sold_Price,num_Pages,a_fname,a_lname,stock_Count FROM BOOKS WHERE a_Lname={}".format(searchStr))
                with con:
                    print("output...")
                    print('   name   |   ISBN   |  genre   |  price | pages | author name | current Stock')
                    for row in table:
                        print(row)
                
            elif(searchFilt==3):
                searchStr = str(input("genre[suspense, action, adventure, horror,sad]-->")).lower()
                table = con.execute("SELECT name,ISBN,genre,sold_Price,num_Pages,a_fname,a_lname,stock_Count FROM BOOKS WHERE genre={}".format(searchStr))
                with con:
                    print("output...")
                    print('   name   |   ISBN   |  genre   |  price | pages | author name | current Stock')
                    for row in table:
                        print(row)
                
            elif(searchFilt==4):
                searchStr = str(input("ISBN(ex. '1334')-->"))
                table = con.execute("SELECT name,ISBN,genre,sold_Price,num_Pages,a_fname,a_lname,stock_Count FROM BOOKS WHERE ISBN={}".format(searchStr))
                with con:
                    print("output...")
                    print('   name   |   ISBN   |  genre   |  price | pages | author name | current Stock')
                    for row in table:
                        print(row)
            elif(searchFilt==5):
                break
            else:
                print("make a valid selection")
            while (signedIn):
                    print("\ninput the ISBN of a book(ex. '1123') and quantity(ex. 5) you would like to add to your cart if any or q to quit back to search")
                    isbnInp = str(input("ISBN-->"))
                    if isbnInp=="q":
                        break
                    quantInp = int(input("quantity-->"))
#work in to add to cartTODO
#check quantities
                    
                    if (True):
                        print("adding the following to your cart")
                        table = con.execute("SELECT name,ISBN,genre,sold_Price,num_Pages,a_fname,a_lname FROM BOOKS WHERE ISBN="+isbnInp)
                        with con:
                            print('   name   |   ISBN   |  genre   |  price | pages | author name | current Stock')
                            for row in table:
                                print(row)
                                userCarts[current_UserID].append([row[1],quantInp])
                                
                                print("\tx"+str(quantInp)+"\n")
                        #print(userCarts)        


    if (sel==2):
        #cartn
        print("\nCart:")
        #print(userCarts)
        if not (signedIn):
            print("not a user, please signup to add to cart")
        else:    
            for x in userCarts[current_UserID]:
                #request the book by id
                rec = con.execute("SELECT name,ISBN,genre,sold_Price,num_Pages,a_fname,a_lname FROM BOOKS WHERE ISBN={}".format(x[0]))
                print(rec.fetchone())
                print("\tx"+str(x[1]))
            if (signedIn):
                #user is signed in
                checkout = (input("checkout y/n? or o for current orders-->"))
                if (checkout=="y"):
                    order = (input("new info n, or default d?-->"))
                    new_address = con.execute("SELECT address FROM USERS WHERE user_ID={}".format(current_UserID)).fetchall()[0][0]
                    new_address = "'"+new_address+"'"
                    #print(new_address)
                    new_card_Num = con.execute("SELECT card_Num FROM USERS WHERE user_ID={}".format(current_UserID)).fetchall()[0][0]
                    #print(new_card_Num)
                    if (order=="n"):
                        new_address = str(input("address?-->"))
                        #print(new_address)
                        new_card_Num = int(input("credit card number?-->"))
                    

                    print("the following orders can be placed due to stock\n-------------------------------------")
                    flag=1
                    orderCnt = con.execute("SELECT COUNT(*) FROM ORDERS").fetchall()[0][0]
                    for f in userCarts[current_UserID]:
                        rec = con.execute("SELECT name,ISBN,genre,sold_Price,num_Pages,a_fname,a_lname FROM BOOKS WHERE ISBN={} AND stock_Count>={}".format(f[0],f[1])).fetchone()

                        if not (rec==None):
                            print(rec)
                            print("\tx" + str(f[1]))
                            flag=0
                            entryCnt = con.execute("SELECT COUNT(*) FROM ENTRY").fetchall()[0][0]
                            con.execute("INSERT INTO ENTRY VALUES ({},{},{},{})".format(entryCnt,orderCnt,f[0],f[1]))
                            count = con.execute("SELECT stock_Count FROM BOOKS WHERE ISBN={} AND stock_Count>={}".format(f[0],f[1])).fetchone()
                            update = con.execute("UPDATE BOOKS SET stock_Count=stock_Count - {}  WHERE ISBN={}".format(f[1],f[0]))
                            #heres where we check if that took too many books out, and then email a publisher
                            if ((count[0]-f[1])<10):
                                print("STOCK BELOW 10: RESTOCKING")
                                bookPub = con.execute("SELECT publisher_ID FROM BOOKS WHERE ISBN={}".format(f[0])).fetchone()
                                pubName = con.execute("SELECT name FROM PUBLISHERS WHERE ID={}".format(bookPub[0])).fetchone()
                                print("EMAILING PUBLISHER: {}".format(pubName))
                                update = con.execute("UPDATE BOOKS SET stock_Count=stock_Count + 10  WHERE ISBN={}".format(f[0]))
                                #update sunk cost
                            
                        else:
                            print("unavailiable")
                    userCarts[current_UserID]=[]
                    print("\n-------------------------------------")
                    if (flag==0):
                        con.execute("INSERT INTO ORDERS VALUES ({},{},{},{})".format(orderCnt,current_UserID,new_card_Num,new_address))
                        print("order complete: "+str(orderCnt))
                    else:
                        print("nothing to order")
                    #order made, now for entries
                    #print out all orders
                    print("\n___________________________________")
                    orderout = con.execute("SELECT * FROM ORDERS")
                    entryout = con.execute("SELECT * FROM ENTRY")
                    #with con:
                    #    print("---All orders---")
                    #    for o in orderout:
                    #        print(o)
                    #    print("---All entries---")
                    #    for e in entryout:
                    #        print(e)
                    #now do work of subtracting from db, replacing if neccesary
                if (checkout=="o"):
                    print('Order Number|User ID|Card Number|Address')
                    print("Your Orders:\n-----------")
                    orderout2 = con.execute("SELECT * FROM ORDERS WHERE user_ID={}".format(current_UserID))
                    with con:
                        for o in orderout2:
                            print(o)
                    print("\n-----------\n")
                



        


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
            #con.execute("IF EXISTS (SELECT * FROM USERS WHERE email={})".format(email))
            if (True):
                con.execute("INSERT INTO USERS VALUES ({},{},{},{},{})".format(username,address,email,card_Num,numUsers))
                user=numUsers
                numUsers+=1
                userCarts.append([])
            else:
                print("email already in use")
                break
        signedIn=True
        current_UserID=int(user)
    if (sel==4):
        break

    if (sel==5):
        if (current_UserID==0):
            print("Admin information:\n----------------------------------\n")
            #prints out sales information
            print("sales vs expenditure:")
            #sales vs expenditure(aggregate all entries with the iddference between sales price and stock price)
            print("Spent:",end=' ')
            expenditure = con.execute("SELECT SUM(stock_Price*stock_Count) FROM BOOKS")
            with con:
                for per in expenditure:
                    print(per[0],end='.00$')
            print("Earned:",end='')
            expenditure = con.execute("SELECT SUM(BOOKS.sold_Price*ENTRY.quantity) FROM BOOKS RIGHT JOIN ENTRY ON BOOKS.ISBN=ENTRY.ISBN")
            with con:
                for per in expenditure:
                    print(per[0],end='.00$\n')
            print("Minus publisher Cut:",end='')
            PublisherCut = con.execute("SELECT SUM(BOOKS.sold_Price*ENTRY.quantity)*(BOOKS.publisher_Cut*0.01) FROM BOOKS RIGHT JOIN ENTRY ON BOOKS.ISBN=ENTRY.ISBN")
            with con:
                for feb in PublisherCut:
                    print(math.ceil(feb[0]),end='$\n')
            print("\nsales per genre:")
            #sales per genre(aggregate all entries sale price with the same genre)(this gets all the entries)
            pergenre = con.execute("SELECT BOOKS.genre, SUM(BOOKS.sold_Price*ENTRY.quantity) FROM BOOKS RIGHT JOIN ENTRY ON BOOKS.ISBN=ENTRY.ISBN GROUP BY BOOKS.genre")
            with con:
                for fo in pergenre:
                    print(fo[0],end='= ')
                    print(fo[1],end='.00$\n')
            print("\nsales per author:")
            perAuth = con.execute("SELECT BOOKS.a_Fname,BOOKS.a_Lname, SUM(BOOKS.sold_Price*ENTRY.quantity) FROM BOOKS RIGHT JOIN ENTRY ON BOOKS.ISBN=ENTRY.ISBN GROUP BY BOOKS.a_Lname")
            with con:
                for au in perAuth:
                    print(au[0],end=' ')
                    print(au[1],end='= ')
                    print(au[2],end='.00$\n')
            #sales per author(aggregate all entries sale price with the same author)
            #add and subtract book options

    






#cleanup when alls done
#con.execute("DROP table *")