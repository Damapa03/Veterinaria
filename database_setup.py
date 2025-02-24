import sqlite3

def initialize_database():
    conn = sqlite3.connect('veterinary_clinic.db')
    cursor = conn.cursor()
    
    # Read the SQL script
    with open('veterinary_database.sql', 'r') as sql_file:
        sql_script = sql_file.read()
    
    # Execute the script
    cursor.executescript(sql_script)
    
    conn.commit()
    conn.close()
    print("Database initialized successfully")