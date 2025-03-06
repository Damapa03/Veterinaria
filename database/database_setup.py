import sqlite3
import os

def initialize_database():
    # Conecta a la base de datos (se renombra a veterinary_client.db para encajar con Clientes)
    conn = sqlite3.connect('veterinary_client.db')
    cursor = conn.cursor()

    # Verifica si existe la tabla "Clientes"
    cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Clientes'")
    table_exists = cursor.fetchone()[0] > 0

    if table_exists:
        # Si la tabla existe, verifica si ya tiene datos
        cursor.execute("SELECT count(*) FROM Clientes")
        has_data = cursor.fetchone()[0] > 0
        if has_data:
            print("Database already initialized. Skipping.")
            conn.close()
            return

    # Si la tabla no existe o no tiene datos, procede a inicializar la base de datos
    with open('veterinaria_db.sql', 'r', encoding='utf-8') as sql_file:
        sql_script = sql_file.read()
        print("Contenido del script SQL:\n", sql_script)
        
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    print("Database initialized successfully")


if __name__ == "__main__":
    initialize_database()
