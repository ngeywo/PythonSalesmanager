import sqlite3

class database:
    def __init__(self,db):
        self.conn= sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS sales ( id INTEGER PRIMARY KEY , product  text,  customer text, pi text,price text)" )
        self.conn.commit()

    def insert(self, product, customer, pi, price):
        self.cur.execute("INSERT INTO sales VALUES(NULL,?,?,?,?)", (product, customer, pi, price))
        self.conn.commit()

    def fetch(self,product=''):
        self.cur.execute("SELECT * FROM  sales ")
        rows= self.cur.fetchall()
        return rows


    def remove(self,id):
        self.cur.execute("DELETE FROM sales WHERE id=?", (id,))
        self.conn.commit()



    def update(self, id, product, customer, pi, price):
        self.cur.execute("UPDATE sales SET product=?,customer=?,pi=?, price=? WHERE id=?",(product,customer,pi,price,id))
        self.conn.commit()


    def __del__(self):
        self.conn.close()



# db=database('store.db')
#
# db.insert("Samsung s10","Mary Ambasa","19277dff37","10399")
# db.insert("Techno k7","calvi joan","19trrff37","1600")
# db.insert("Lenovo ","jacob maeas","1817f37","2399")
# db.insert("nokia","Margret nyawera","19272425","26399")
# db.insert("Itel","John juma","1tttdff37","242599")