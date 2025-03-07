import os
import sqlite3


class Database:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db_path = os.path.join(base_dir, "database", "veterinary_clinic.db")

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.conn.commit()