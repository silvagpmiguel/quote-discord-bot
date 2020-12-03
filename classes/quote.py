import psycopg2
from datetime import datetime


class Quote():
    def __init__(self, database, user, password, host, port):
        self.con = psycopg2.connect(
            database=f"{database}", user=f"{user}", password=f"{password}", host=f"{host}", port=f"{port}"
        )
        self.createTableIfNotExists()

    def createTableIfNotExists(self):
        c = self.con.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS quote
            (id SERIAL PRIMARY KEY, creation_date timestamp, title VARCHAR(64) NOT NULL,
            quote VARCHAR(256) NOT NULL, author VARCHAR(32) NOT NULL, 
            unique (quote, author))''')
        self.con.commit()
    def addQuote(self, title, quote, author):
        c = self.con.cursor()
        flag = False
        try: 
            c.execute(
                f"INSERT INTO quote VALUES (default,current_timestamp,'{title}','{quote}','{author}')"
            )

        except Exception:
            flag = True
            self.conn.rollback()
        finally:
            self.con.commit()
            return flag

    def getRandomQuote(self):
        c = self.con.cursor()
        c.execute("SELECT * FROM quote ORDER BY random() LIMIT 1")
        return c.fetchone()

    def getRandomQuoteFromUser(self, author):
        c = self.con.cursor()
        c.execute(
            f"SELECT * FROM quote where author='{author}' ORDER BY random() LIMIT 1")
        return c.fetchone()

    def closeConnection(self):
        self.con.close()
