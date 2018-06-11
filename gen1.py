import MySQLdb


class Database:

    host = 'localhost'
    user = 'aji'
    password = '1234567!'
    db = 'wikigen'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()



    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()


import sys
import random


def genword(minchars=3,maxchars=5,istitle=0):
	vocal=('a','e','i','o','u')
	conso=('w','r','t','y','i','p','s','d','f','g','h','j','k','l','z','c','b','n','m')
	group = []
	numchar = random.randint(minchars,maxchars)
	for i in range(numchar):
		rnd = random.randint(0,1)
		if rnd is 0:
			full_name=random.choice(vocal)+random.choice(conso)
		if rnd is 1:
			full_name=random.choice(conso)+random.choice(vocal)
		group.append(full_name)
	#assuming he wants at least some kind of seperator between the names.
	group_string = "".join(group)
	if istitle is 1:
		return group_string.title()
	else:
		return group_string


def genname(minwords=2,maxwords=3,minchars=3,maxchars=5,istitle=1):
	import random
	numword = random.randint(minwords,maxwords)
	group = []
	for i in range(numword):
		dword = genword(minchars,maxchars,istitle)
		group.append(dword)
	return " ".join(group)


def gendesc(minitem=3, maxitem=100, minwords=5, maxwords=10, minchars=3, maxchars=7, istitle=0):
	import random
	numitem = random.randint(minitem,maxitem)
	group = []
	for i in range(numitem):
		ditem = genname(minwords,maxwords,minchars,maxchars, istitle)
		group.append(ditem)
	return ". ".join(group)+"."


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
                g + = 1
		name_1 = genname(minwords=1,maxwords=1,minchars=3,maxchars=5)
                name_2 = genname(minwords=1,maxwords=2,minchars=3,maxchars=5)
                email  = '{0}@{1}.com' . format(name_1, genword(minchars=5,maxchars=10, istitle=0))
                query = "INSERT INTO Seller SET firstname = '"+str(name_1)+"', lastname = '"+str(name_2)+"', email = '"+str(email)+"', dateadd='"+currdatetime+"'"
                print('{0} Seller created : {1} {2}' . format(g, name_1, name_2))
		db.insert(query)
	
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
	
	
	import hashlib
        
	# choose 1000 Users/buyers random
	select_query = "SELECT id, firstname UName from Users Where 1 order by RAND() LIMIT 1000"
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
			for rp in random_product:
				id_product = rp['id']
				
			num_item_buy = random.randint(1,rp['stock'])
			try:
				db.insert("INSERT INTO SessionOrders SET idProduct={0}, numItems={1}, idUser={2}, dateadd='{3}', SessCode='{4}'" . format(id_product, num_item_buy, id['id'], currdatetime, session_code))
				db.insert("UPDATE Products SET stock=stock-{0} WHERE id={1}" . format(num_item_buy, id_product))
				print('{0} buy {1} ({2} items)' . format(id['UName'], rp['title'], num_item_buy))
				error = False
			except:
				print('error insert SessionOrders')
				error = True
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
