from Database import Database
from Functions import genword, genname, gendesc
from time import gmtime, strftime
import sys
import random
import time

def GenProducts(limit=100):
    if __name__ == "__main__":
        db = Database()
        
        # generate Product
        select_query = "SELECT id, firstname from Seller Where 1 order by RAND() LIMIT {0}" . format(limit)
        cursor = db.query(select_query)
        l = 0
        for (id) in cursor:
            l += 1
            print('\n{0}-----' . format(l))
            restock_or_generate = random.randint(1,5)

            # new products
            if restock_or_generate is 1:
                currdatetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                # how many Product
                for w in range(random.randint(1, 10)):
                    title = genname(minwords=1,maxwords=4,minchars=3,maxchars=5, istitle=1)
                    descr = gendesc(minitem=5, maxitem=10, minwords=5, maxwords=10, minchars=3, maxchars=7)
                    nstock = random.randint(5,20)
                    check_title = db.query("SELECT COUNT(title) FROM Products WHERE 1 AND title='{0}'" . format(title))
                    if check_title = 0:
                        query = "INSERT INTO Products SET title = '{0}', idSeller = {1}, stock = {2}, description = '{3}', dateadd='{4}'" . format(title, id['id'], nstock, descr, currdatetime)
                        print('{0}  Product created : {1} ({2} items)' . format(id['firstname'], title, nstock))
                        db.insert(query)
            
            elif restock_or_generate > 1:
                select_query = "SELECT id, title from Products Where 1 and stock<10 and idSeller={0} order by RAND() LIMIT 500" . format(id['id'])
                cursor = db.query(select_query)
                for (Pid) in cursor:
                    try:
                        num_restock = random.randint(1,20)
                        db.query("UPDATE Products SET stock=stock+{0} where 1 and id={1}" . format(num_restock, Pid['id']))
                        print('Restock {0} + {1}' . format(Pid['title'], num_restock))
                    except:
                        print('Restock Fail {0} + {1}' . format(Pid['title'], num_restock))

                        
try:
    while True:
        GenProducts(limit=1)
        time.sleep(1)
except KeyboardInterrupt:
    pass # do cleanup here
