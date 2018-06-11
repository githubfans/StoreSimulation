from Database import Database
from Functions import genword, genname, gendesc
from time import gmtime, strftime
import sys
import random

if __name__ == "__main__":

    db = Database()
        
    # generate Product
    select_query = "SELECT id, firstname from Seller Where 1 order by RAND() LIMIT 500"
    cursor = db.query(select_query)
    l = 0
    for (id) in cursor:
        l += 1
        restock_or_generate = random.randint(0,1)
        if restock_or_generate is 0:
            currdatetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            for w in range(random.randint(10, 50)):
                title = genname(minwords=1,maxwords=4,minchars=3,maxchars=5, istitle=1)
                descr = gendesc(minitem=5, maxitem=10, minwords=5, maxwords=10, minchars=3, maxchars=7)
                nstock = random.randint(5,100)
                query = "INSERT INTO Products SET title = '{0}', idSeller = {1}, stock = {2}, description = '{3}', dateadd='{4}'" . format(title, id['id'], nstock, descr, currdatetime)
                print('{0} {1}  Product created : {2} ({3} items)' . format(l, id['firstname'], title, nstock))
                db.insert(query)
        else:
            select_query = "SELECT id, title from Products Where 1 and stock<10 and idSeller={0} order by RAND() LIMIT 100" . format(id['id'])
            cursor = db.query(select_query)
            for (Pid) in cursor:
                try:
                    num_restock = random.randint(10,50)
                    db.query("UPDATE Products SET stock=stock+{0} where 1 and id={1}" . format(num_restock, Pid['id']))
                    print('{0} Restock {1} + {2}' . format(l, Pid['title'], num_restock))
                except:
                    print('{0} Restock Fail {1} + {2}' . format(l, Pid['title'], num_restock))
