from Database import Database
from Functions import genword, genname, gendesc
from time import gmtime, strftime
import hashlib
import sys
import random

def Transaction(limit=100):
    if __name__ == "__main__":
        db = Database()

        # choose n Users/buyers random
        select_query = "SELECT id, firstname UName from Users Where 1 order by RAND() LIMIT {0}" . format(limit)
        cursor = db.query(select_query)
        nt = 0
        for (id) in cursor:
            currdatetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

            # md5 for session code = receipt code
            sessioncode = '{0}|{1}' . format(id['id'], strftime("%Y-%m-%d %H:%M:%S", gmtime()))
            m = hashlib.md5()
            m.update(sessioncode)
            session_code = m.hexdigest()

            # Users's buy 
            num_of_products = random.randint(1,20)
            # choose n product random
            random_product = db.query("select p.id idpro, idSeller, title, stock, s.firstname SName from Products p Join Seller s on p.idSeller=s.id where 1 and stock>=1 order by RAND() limit 0,{0}" . format(num_of_products))
            for w in random_product:
                id_product = w['idpro']
                pstock = db.query("select stock from Products where 1 and id={0}" . format(id_product))
                for st in pstock:
                    pstock_ = st['stock']
                if pstock_ >= 1:
                    num_item_buy = random.randint(1,pstock_)
                    #print('{0} - {1}' . format(id_product, num_item_buy))
                    qinsert = "INSERT INTO SessionOrders SET idProduct={0}, numItems={1}, idUser={2}, dateadd='{3}', SessCode='{4}'" . format(id_product, num_item_buy, id['id'], currdatetime, session_code)
                    #print(qinsert)
                    qupdate = "UPDATE Products SET stock=stock-{0} WHERE id={1}" . format(num_item_buy, id_product)
                    #print(qupdate)
                    try:
                        db.insert(qinsert)
                        db.insert(qupdate)
                        print('{0} buy {1} ({2} items)' . format(id['UName'], w['title'], num_item_buy))
                        error = False
                    except:
                        print('error insert SessionOrders')
                        error = True
                else:
                    error = True
                    print('Stock = 0 _____________________________')
            
            if error is False:
                try:
                    nt += 1
                    db.insert("INSERT INTO Transaction SET idUser={0}, idSeller={1}, idSession='{2}', description='{3}', dateadd='{4}'" . format(id['id'], w['idSeller'], session_code, '', currdatetime))
                    print('{0} Transaction : {1} successfully\n' . format(nt, session_code))
                except:
                    # roll back
                    db.insert("DELETE FROM SessionOrders WHERE SessCode='{0}'" . format(session_code))
                    db.insert("UPDATE Products SET stock=stock+{0} WHERE id={1}" . format(num_item_buy, id_product))
                    print('error transaction')
            else:
                print('error transaction')
            
'''
import time
timeout = time.time() + 60*5   # 5 minutes from now
while True:
    test = 0
    Transaction(limit=10)
    if test == 5 or time.time() > timeout:
        break
    test = test - 1
'''
'''
import cv2
while True:
    k = cv2.waitKey(1) & 0xFF
    Transaction(limit=10)
    # press 'q' to exit
    if k == ord('q'):
        break
'''
try:
    while True:
        Transaction(limit=1)
except KeyboardInterrupt:
    pass # do cleanup here
'''
import thread
import time

# Create two threads as follows
try:
    thread.start_new_thread( Transaction, ( 200, ) )
    thread.start_new_thread( Transaction, ( 200, ) )
except:
    print "Error: unable to start thread"

while 1:
    pass
'''
