from Database import Database
from time import gmtime, strftime

if __name__ == "__main__":

    db = Database()
        
    # generate Product
    select_query = "SELECT id, firstname from Seller Where 1 order by RAND() LIMIT 500"
        cursor = db.query(select_query)
        for (id) in cursor:
        currdatetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            g = 0
        for w in range(random.randint(10, 50)):
                    g += 1
            title = genname(minwords=1,maxwords=4,minchars=3,maxchars=5, istitle=1)
                    descr = gendesc(minitem=5, maxitem=10, minwords=5, maxwords=10, minchars=3, maxchars=7)
            nstock = random.randint(5,100)
                    query = "INSERT INTO Products SET title = '{0}', idSeller = {1}, stock = {2}, description = '{3}', dateadd='{4}'" . format(title, id['id'], nstock, descr, currdatetime)
                    print('{0} {1}  Product created : {2} ({3} items)' . format(g, id['firstname'], title, nstock))
            db.insert(query)
