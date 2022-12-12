#sql test info, taken directly out of the python file below
#i understand i didnt set a database but this would be the input for that 

CREATE DATABASE my-test.db

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



            CREATE TABLE PUBLISHERS (
                name varchar(30),
                address varchar(30),
                card_Num INTEGER,
                email varchar(30),
                phone_Num INTEGER,
                ID INTEGER RPRIMARY KEY


            CREATE TABLE USERS (
                username varchar(30),
                address varchar(30),
                email varchar(30),
                card_Num INTEGER,
                user_ID INTEGER PRIMARY KEY



            CREATE TABLE ORDERS (
                order_Num INTEGER PRIMARY KEY,
                user_ID INTEGER,
                card_Num INTEGER,
                address varchar(30)

        

            CREATE TABLE ENTRY (
                entry_Num INTEGER PRIMARY KEY,
                order_Num INTEGER,
                ISBN INTEGER,
                quantity INTEGER

    #for testing we will have 20 books(starting at ISBN=1332),5 publishers(starting at id=0),4 users(starting at id=0),genre will be [suspense, action, adventure, horror,sad]
    INSERT INTO BOOKS values('catcher and the rye',1332,'suspense',21,19,20,10,01,420,'Jerome','Salinger')
    INSERT INTO BOOKS values('mobey dick',1333,'action',21,18,21,11,02,4666,'Dun-in','Kruger')
    INSERT INTO BOOKS values('simple',1334,'adventure',23,16,17,16,03,555,'Ben','Jamin')
    INSERT INTO BOOKS values('one and done',1335,'horror',44,15,16,22,04,435,'Ben','Jamin')
    INSERT INTO BOOKS values('stone',1336,'sad',12,13,31,33,01,2456,'Suma','Wrastlin')
    INSERT INTO BOOKS values('beggar',1337,'suspense',11,14,23,45,02,243,'Aasi','Mar')
    INSERT INTO BOOKS values('Chimarvamidium',1338,'action',45,15,16,33,03,12,'Beo','Wulf')
    INSERT INTO BOOKS values('notebook',1339,'adventure',23,15,17,25,04,433,'N/A','N/A')
    INSERT INTO BOOKS values('deathbrand',1340,'horror',43,16,19,12,01,776,'Razz','Elazier')
    INSERT INTO BOOKS values('dwarves',1341,'sad',15,13,14,36,02,346,'El','Lagarto')
    INSERT INTO BOOKS values('king',1342,'suspense',34,12,15,74,03,123,'War','Forged')
    INSERT INTO BOOKS values('olaf and the dragon',1343,'action',33,11,12,14,04,653,'Ben','Jamin')
    INSERT INTO BOOKS values('on oblivion',1344,'adventure',54,17,20,64,01,644,'Ben','Jamin')
    INSERT INTO BOOKS values('remanada',1345,'horror',32,19,21,35,02,675,'Razz','Elazier')
    INSERT INTO BOOKS values('shadowmarks',1346,'sad',12,18,23,57,03,4321,'Denji','Pochita')
    INSERT INTO BOOKS values('sithis',1347,'suspense',51,16,17,86,04,1222,'Choles','Torol')
    INSERT INTO BOOKS values('the art of war magic',1348,'action',21,15,22,45,01,1111,'Potas','Sium')
    INSERT INTO BOOKS values('the black arrow',1349,'adventure',32,13,15,24,02,121,'Ben','Jamin')
    INSERT INTO BOOKS values('scourge',1350,'horror',13,15,17,46,03,321,'Denji','Pochita')
    INSERT INTO BOOKS values('The Song of Pelinal, Book IV',1351,'sad',42,16,19,23,04,567,'Aki','Hayakawa')

    INSERT INTO PUBLISHERS values('remingont.Pc','44 bakers street',112369549836,'remingont@gmail.com',6138859898,0)
    INSERT INTO PUBLISHERS values('guronimo.Pc','43 pencil ave.',471854087227,'guronimo@gmail.com',6134604267,1)
    INSERT INTO PUBLISHERS values('outpost.Pc','11 frog road',372818947195,'outpost@gmail.com',6132076392,2)
    INSERT INTO PUBLISHERS values('books4days.Pc','65 stag street',311470951372,'books4days@gmail.com',6134194170,3)
    INSERT INTO PUBLISHERS values('suplexepedia.Pc','876 rear street',847138088349,'suplexepedia@gmail.com',6136315312,4)

    INSERT INTO USERS values('BenConabree','9 roe ave','BC@gmail.com',966061692207,0)
    INSERT INTO USERS values('JoeShmoo','4 sill ave','JS@gmail.com',162064667645,1)
    INSERT INTO USERS values('IndianaJones','5 piccolo way','IJ@gmail.com',279942305771,2)
    INSERT INTO USERS values('JustinTimberlake','66 avalon street','JT@gmail.com',207002434194,3)
    INSERT INTO USERS values('RomeoJuliet','344 soar ave.','RJ@gmail.com',844070300767,4)
    INSERT INTO USERS values('HomerSimpson','22 jim road','HS@gmail.com',012954054731,5)
    
