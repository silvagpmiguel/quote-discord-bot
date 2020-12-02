import sqlite3
from datetime import datetime


class Quote():
    def __init__(self):
        self.conn = sqlite3.connect('db/quotes.db')
        self.createTableIfNotExists()

    def createTableIfNotExists(self):
        c = self.conn.cursor()
        # Create table
        c.execute('''CREATE TABLE IF NOT EXISTS quote
                    (id INT PRIMARY KEY,creation_date datetime, title text, quote text, author text, UNIQUE(quote, author) ON CONFLICT IGNORE)''')
        self.conn.commit()

    def addQuote(self, title, quote, author):
        c = self.conn.cursor()
        format = '%y-%m-%d %H:%M:%S'
        now = datetime.now().strftime(format)
        # Create table
        c.execute(
            f"INSERT INTO quote VALUES ('{now}','{title}','{quote}','{author}')")
        self.conn.commit()

    def getRandomQuote(self):
        c = self.conn.cursor()
        # Create table
        c.execute("SELECT * FROM quote ORDER BY random() LIMIT 1")
        return c.fetchone()

    def getRandomQuoteFromUser(self, author):
        c = self.conn.cursor()
        # Create table
        c.execute(
            f"SELECT * FROM quote where author='{author}' ORDER BY random() LIMIT 1")
        return c.fetchone()

    def closeConnection(self):
        self.conn.close()
