import sqlite3

class Database:

    def __init__(self):
        self.conn = sqlite3.connect("bank.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(name TEXT, balance INTEGER)""")
        self.conn.commit()

    def insert_account(self,name,balance):
        self.cursor.execute("""INSERT INTO accounts VALUES(?,?)""",(name,balance))
        self.conn.commit()

    def update_balance(self, name, balance):
        self.cursor.execute(
        "UPDATE accounts SET balance = ? WHERE name = ?",
        (balance, name)
                        )
        self.conn.commit()

    
    def get_balance(self,name):
        self.cursor.execute("""SELECT balance FROM accounts WHERE name = ?""", (name))
        result = self.cursor.fetchone()
        return result[0] if result else 0