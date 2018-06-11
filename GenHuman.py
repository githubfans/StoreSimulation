from Database import Database
from time import gmtime, strftime

if __name__ == "__main__":

    db = Database()
    currdatetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    
    # generate User
    g = 0
    for w in range(random.randint(10, 50)):
        # Data Insert into the table
        g += 1
        name_1 = genname(minwords=1,maxwords=1,minchars=3,maxchars=5)
        name_2 = genname(minwords=1,maxwords=2,minchars=3,maxchars=5)
        email  = '{0}@{1}.com' . format(name_1, genword(minchars=5,maxchars=10, istitle=0))
        query = "INSERT INTO Users SET firstname = '"+str(name_1)+"', lastname = '"+str(name_2)+"', email = '"+str(email)+"', dateadd='"+currdatetime+"'"
        print('{0} User created : {1} {2}' . format(g, name_1, name_2))
        db.insert(query)
    
    # generate Seller
    g = 0
    currdatetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    for w in range(random.randint(1, 10)):
        # Data Insert into the table
        g += 1
        name_1 = genname(minwords=1,maxwords=1,minchars=3,maxchars=5)
        name_2 = genname(minwords=1,maxwords=2,minchars=3,maxchars=5)
        email  = '{0}@{1}.com' . format(name_1, genword(minchars=5,maxchars=10, istitle=0))
        query = "INSERT INTO Seller SET firstname = '"+str(name_1)+"', lastname = '"+str(name_2)+"', email = '"+str(email)+"', dateadd='"+currdatetime+"'"
        print('{0} Seller created : {1} {2}' . format(g, name_1, name_2))
        db.insert(query)
