import sqlite3
import os


def initialize_database():
    conn = sqlite3.connect('veterinary_clinic.db')
    cursor = conn.cursor()

    # Check if database already has data
    cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Clinicas'")
    table_exists = cursor.fetchone()[0] > 0

    if table_exists:
        # Check if data exists
        cursor.execute("SELECT count(*) FROM Clinicas")
        has_data = cursor.fetchone()[0] > 0

        if has_data:
            print("Database already initialized. Skipping.")
            conn.close()
            return

    # Continue with database initialization
    with open('veterinaria_db.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    print("Database initialized successfully")


# Actually call the function
if __name__ == "__main__":
    initialize_database()