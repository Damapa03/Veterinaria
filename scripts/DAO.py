import os
import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database/veterinary_clinic.db")
        self.cursor = self.conn.cursor()

        with open("database/veterinaria_db.sql", 'r') as sql_file:
            sql_script = sql_file.read()

        self.cursor.executescript(sql_script)

        self.conn.commit()

    def close(self):
        self.conn.close()