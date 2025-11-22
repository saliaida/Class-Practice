import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute( """
                            CREATE TABLE IF NOT EXISTS Contacts (id INTEGER PRIMARY KEY,
                            name text, family text, address text, phone text)
                            """)
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM Contacts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, family, address, phone):
        self.cur.execute("""
                            INSERT INTO Contacts VALUES( NULL, ?, ?, ?, ?)
                            """, (name, family, address, phone))
        self.con.commit()

    def remove(self, id):
        sql_delete = "DELETE FROM Contacts WHERE id = ?"
        self.cur.execute(sql_delete, (id,))
        self.con.commit()

    def update(self, id, name, family, address, phone):
        self.cur.execute("""
                            UPDATE Contacts SET name = ?, family = ?, address = ? , phone = ? WHERE id = ?
                            """ , (name, family, address, phone, id))
        self.con.commit()

    def search(self, name):
         self.cur.execute('SELECT * FROM Contacts WHERE id = ? or name = ? or family = ? or address = ? or phone= ? ',
                                (name, name, name, name, name))
         recs = self.cur.fetchall()
         return  recs
    #def search(self, id):
            # print("Last ID is: ", self.cur.lastrowid)
            # print(id , self.cur.lastrowid)
            # if id <= lastrow:
            #     self.cur.execute("SELECT  * FROM Contacts WHERE id = ?", (id,) )
            #     row = self.cur.fetchone()
            #     return row
            # else:
            #      return 0
        
            # self.cur.execute("SELECT  * FROM Contacts WHERE id = ?", (id,) )
            # row = self.cur.fetchone()
            # return  row

    # def __del__(self):
    #     self.con.close()







        
