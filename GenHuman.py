from Database import Database
from Functions import genword, genname, gendesc, GetConfig
from time import gmtime, strftime
import sys
import random


def GenHuman(limit_user=100, limit_seller=100):
    if __name__ == "__main__":

        db = Database()
        currdatetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        # generate User
        g = 0
        for w in range(random.randint(10, limit_user)):
            # Data Insert into the table
            g += 1
            name_1 = genname(minwords=1,maxwords=1,minchars=3,maxchars=5)
            name_2 = genname(minwords=1,maxwords=2,minchars=3,maxchars=5)
            email  = '{0}@{1}.com' . format(name_1, genword(minchars=5,maxchars=10, istitle=0))
            check_email = db.insert("SELECT COUNT(*) FROM Users WHERE 1 AND email='{0}'" . format(email))
            if check_email is None:
                query = "INSERT INTO Users SET firstname = '"+str(name_1)+"', lastname = '"+str(name_2)+"', email = '"+str(email)+"', dateadd='"+currdatetime+"'"
                print('{0} User created : {1} {2}' . format(g, name_1, name_2))
                db.insert(query)

        # generate Seller
        g = 0
        currdatetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        for w in range(random.randint(1, limit_seller)):
            # Data Insert into the table
            g += 1
            name_1 = genname(minwords=1,maxwords=1,minchars=3,maxchars=5)
            name_2 = genname(minwords=1,maxwords=2,minchars=3,maxchars=5)
            email  = '{0}@{1}.com' . format(name_1, genword(minchars=5,maxchars=10, istitle=0))
            check_email = db.insert("SELECT COUNT(email) FROM Seller WHERE 1 AND email='{0}'" . format(email))
            if check_email is None:
                query = "INSERT INTO Seller SET firstname = '"+str(name_1)+"', lastname = '"+str(name_2)+"', email = '"+str(email)+"', dateadd='"+currdatetime+"'"
                print('{0} Seller created : {1} {2}' . format(g, name_1, name_2))
                db.insert(query)

            
try:
    while True:
        GenHuman(limit_user=50, limit_seller=10)
except KeyboardInterrupt:
    pass # do cleanup here
