import sqlite3

#ESTO ES PROVISIONAL PARA CREAR LA BASE DE DATOS NO HACE FALTA QUE LO USEIS
def initialize_database():
    conn = sqlite3.connect('veterinary_clinic.db')
    cursor = conn.cursor()
    
    # Lee el script Sql
    with open('veterinary_database.sql', 'r') as sql_file:
        sql_script = sql_file.read()
    
    # Ejecuta el script
    cursor.executescript(sql_script)
    
    conn.commit()
    conn.close()
    print("Database initialized successfully")