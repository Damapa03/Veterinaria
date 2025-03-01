import os
import sqlite3


class Database:
    def __init__(self):
        # Get the absolute path to the project directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db_path = os.path.join(base_dir, "database", "veterinary_clinic.db")

        # Make sure the directory exists
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.conn.commit()