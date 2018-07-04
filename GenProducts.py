from Database import Database
from Functions import genword, genname, gendesc, GetConfig
from time import gmtime, strftime
import sys
import random
import time


def GenProducts(numseller=1, restockprobability=5, numproduct_restock=1, min_numnewpro=1, max_numnewpro=2, min_nstock=1, max_nstock=5):
    if __name__ == "__main__":
        db = Database()
        
        # generate Product
        select_query = "SELECT id, firstname from Seller Where 1 order by RAND() LIMIT {0}" . format(numseller)
        cursor = db.query(select_query)
        l = 0
        for (id) in cursor:
            l += 1
            print('\n{0}-----' . format(l))
            restock_or_generate = random.randint(1,restockprobability)

            # new products
            if restock_or_generate is 1:
                currdatetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                # how many Product
                for w in range(random.randint(min_numnewpro, max_numnewpro)):
                    title = genname(minwords=1,maxwords=4,minchars=3,maxchars=5, istitle=1)
                    descr = gendesc(minitem=5, maxitem=10, minwords=5, maxwords=10, minchars=3, maxchars=7)
                    nstock = random.randint(min_nstock,max_nstock)
                    check_title = db.insert("SELECT COUNT(title) FROM Products WHERE 1 AND title='{0}'" . format(title))
                    if check_title < 1:
                        query = "INSERT INTO Products SET title = '{0}', idSeller = {1}, stock = {2}, description = '{3}', dateadd='{4}'" . format(title, id['id'], nstock, descr, currdatetime)
                        print('{0}  Product created : {1} ({2} items)' . format(id['firstname'], title, nstock))
                        db.insert(query)
            
            # restock here.....
            elif restock_or_generate > 1:
                select_product = "SELECT id, title from Products Where 1 and stock<1 and idSeller={0} order by RAND() LIMIT {1}" . format(id['id'], numproduct_restock)
                cursor = db.query(select_product)
                for (Pid) in cursor:
                    try:
                        num_restock = random.randint(min_nstock,max_nstock)
                        db.insert("UPDATE Products SET stock=stock+{0} WHERE 1 AND id={1}" . format(num_restock, Pid['id']))
                        print('Restock {0} + {1}' . format(Pid['title'], num_restock))
                    except:
                        print('Restock Fail {0} + {1}' . format(Pid['title'], num_restock))
                # if stock < 1
                db.insert("update Products set stock=1 where stock < 0")

                        
try:
    while True:
        
        genpro_sleep = GetConfig('genpro_sleep')
        genpro_limit = GetConfig('genpro_limit')
        
        if genpro_limit >= 1 :
        
            # probability = 5 >> 1 for new product and 5 for restock 
            genpro_restockprobability = GetConfig('genpro_restockprobability')
            genpro_numproducttorestock = GetConfig('genpro_numproducttorestock')
            genpro_nstock_min = GetConfig('genpro_nstock_min')
            genpro_nstock_max = GetConfig('genpro_nstock_max')
            genpro_numnewpro_min = GetConfig('genpro_numnewpro_min')
            genpro_numnewpro_max = GetConfig('genpro_numnewpro_max')
            
            GenProducts(numseller=genpro_limit, restockprobability=genpro_restockprobability, numproduct_restock=genpro_numproducttorestock, min_numnewpro=genpro_numnewpro_min, max_numnewpro=genpro_numnewpro_max, min_nstock=genpro_nstock_min, max_nstock=genpro_nstock_max)
            if genpro_sleep >= 1:
                time.sleep(genpro_sleep)
        
        else:
            pass

except KeyboardInterrupt:
    pass # do cleanup here
