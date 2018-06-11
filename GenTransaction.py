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
            num_of_buys = random.randint(1,10)
            for w in range(num_of_buys):

                # choose 1 product random
                random_product = db.query("select p.id, idSeller, title, stock, s.firstname SName from Products p Join Seller s on p.idSeller=s.id where 1 and stock>=1 order by RAND() limit 0,1")

                # get id
                groupID = []
                groupQ = []
                for rp in random_product:
                    id_product = rp['id']

                num_item_buy = random.randint(1,rp['stock'])
                '''
                try:
                    db.insert("INSERT INTO SessionOrders SET idProduct={0}, numItems={1}, idUser={2}, dateadd='{3}', SessCode='{4}'" . format(id_product, num_item_buy, id['id'], currdatetime, session_code))
                    db.insert("UPDATE Products SET stock=stock-{0} WHERE id={1}" . format(num_item_buy, id_product))
                    print('{0} buy {1} ({2} items)' . format(id['UName'], rp['title'], num_item_buy))
                    error = False
                except:
                    print('error insert SessionOrders')
                    error = True
                '''
                
                q_insert="(idProduct={0}, numItems={1}, idUser={2}, dateadd='{3}', SessCode='{4}'), " . format(id_product, num_item_buy, id['id'], currdatetime, session_code)
                parsial = '{0}|{1}' . format(id_product, num_item_buy)
                groupID.append(parsial)                
                groupQ.append(q_insert) 

            group_string = "".join(groupID)
            group_stringQ = "".join(groupQ)
            try:
                db.insert("INSERT INTO SessionOrders {0}" . format(group_stringQ))
                for gpid in group_string:
                    nstock = gpid.strip().split('|')[0]
                    pid_ = gpid.strip().split('|')[1]
                    db.insert("UPDATE Products SET stock=stock-{0} WHERE id={1}" . format(nstock, pid_))
            except:
                print('error insert transaction.')
            if error is False:
                try:
                    nt += 1
                    db.insert("INSERT INTO Transaction SET idUser={0}, idSeller={1}, idSession='{2}', description='{3}', dateadd='{4}'" . format(id['id'], rp['idSeller'], session_code, '', currdatetime))
                    print('{0} Transaction : {1} successfully\n' . format(nt, session_code))
                except:
                    # roll back
                    db.insert("DELETE FROM SessionOrders WHERE SessCode='{0}'" . format(session_code))
                    db.insert("UPDATE Products SET stock=stock+{0} WHERE id={1}" . format(num_item_buy, id_product))
                    print('error transaction')
            else:
                print('error transaction')


Transaction(limit=253)
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
