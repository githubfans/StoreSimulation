from Database import Database
from Functions import genword, genname, gendesc, GetConfig
from time import gmtime, strftime
import hashlib
import sys
import random

def Transaction(num_buyer=1, minbuy_numpro=1, maxbuy_numpro=10, min_stock_can_sell=1):
    if __name__ == "__main__":
        db = Database()
        
        # choose n Users/buyers random
        select_query = "SELECT id, firstname UName from Users WHERE 1 ORDER BY RAND() LIMIT {0}" . format(num_buyer)
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
            num_of_products = random.randint(minbuy_numpro,maxbuy_numpro)
            
            # choose n product random
            # lock this product from other transaction
            qupdate = "UPDATE Products SET in_use='{0}' WHERE 1 AND in_use='' AND stock>={1} ORDER BY RAND() DESC LIMIT {2}" . format(session_code, min_stock_can_sell, num_of_products)
            db.insert(qupdate)
            
            ntrx = 0
            num_item_buy = 0
            sum_num_item_buy = 0
            random_product = ''
            
            try:                
                qrandom = "SELECT p.id idpro, idSeller, title, stock, s.firstname SName FROM Products p JOIN Seller s on p.idSeller=s.id WHERE 1 AND p.in_use='{0}'" . format(session_code)
                random_product = db.query(qrandom)
            except:
                print('error select random_product')
            
            if random_product is not None:
                try:
                    for w in random_product:
                        id_product = w['idpro']
                        #pstock = db.query("select stock from Products where 1 and id={0}" . format(id_product))
                        #for st in pstock:
                        #    pstock_ = st['stock']
                        pstock_ = w['stock']
                        if pstock_ >= 1:
                            if pstock_ is 1:
                                num_item_buy = 1
                            else:    
                                num_item_buy = random.randint(1,pstock_)
                            sum_num_item_buy += num_item_buy
                            diff_after_buy = pstock_ - num_item_buy 
                            if diff_after_buy >= 0:
                                #print('{0} - {1}' . format(id_product, num_item_buy))
                                qinsert = "INSERT INTO SessionOrders SET idProduct={0}, numItems={1}, idUser={2}, dateadd='{3}', sessioncode='{4}'" . format(id_product, num_item_buy, id['id'], currdatetime, session_code)
                                #print(qinsert)
                                qupdate = "UPDATE Products SET stock=stock-{0} WHERE id={1}" . format(num_item_buy, id_product)
                                #print(qupdate)
                                buyer_name = id['UName']
                                try:
                                    db.insert(qinsert)
                                    db.insert(qupdate)
                                    #print('{0} buy {1} ({2} items)' . format(buyer_name, w['title'], num_item_buy))
                                    ntrx += 1
                                except:
                                    print('error insert SessionOrders')       
               
                except:
                
                    print('error random_product')
                
            else:
                print('random_product is NONE')
            
            if ntrx > 0:
                try:
                    nt += 1
                    db.insert("INSERT INTO Transaction SET idUser={0}, idSeller={1}, idSession='{2}', description='{3}', dateadd='{4}'" . format(id['id'], w['idSeller'], session_code, '', currdatetime))
                    print('User :{0}, total items = {1}' . format(buyer_name, sum_num_item_buy))
                    print('{0} Transaction : {1} successfully\n' . format(nt, session_code))
            
                except:
                    # roll back
                    db.insert("DELETE FROM SessionOrders WHERE sessioncode='{0}'" . format(session_code))
                    db.insert("UPDATE Products SET stock=stock+{0} WHERE id={1}" . format(num_item_buy, id_product))
                    print('error transaction.. rollback done..')
            
            #print('session_code = {0}' . format(session_code))
            qrezero = "UPDATE Products SET in_use='' WHERE 1 AND in_use='{0}'" . format(session_code)
            db.insert(qrezero)


try:
    while True:
        gentrx_limit = GetConfig('gentrx_limit')
        if gentrx_limit >= 1 :
            print('gentrx_limit = {0}' . format(gentrx_limit))
            gentrx_buy_numpro_min = GetConfig('gentrx_buy_numpro_min')
            gentrx_buy_numpro_max = GetConfig('gentrx_buy_numpro_max')
            gentrx_stock_requirement = GetConfig('gentrx_stock_requirement')
            print('gentrx_buy_numpro_min = {0} | gentrx_buy_numpro_max = {1} | gentrx_stock_requirement = {2}' . format(gentrx_buy_numpro_min, gentrx_buy_numpro_max, gentrx_stock_requirement))
            Transaction(num_buyer=gentrx_limit, minbuy_numpro=gentrx_buy_numpro_min, maxbuy_numpro=gentrx_buy_numpro_max, min_stock_can_sell=gentrx_stock_requirement)
        else:
            pass
except KeyboardInterrupt:
    pass # do cleanup here


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
    fgfgfdTransaction(limit=10)
    # press 'q' to exit
    if k == ord('q'):
        break
'''
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
