import os
import sqlite3
import traceback

class Database:
    def __init__(self):
        # Determinar la ruta absoluta de la base de datos.
        script_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(script_dir)
        db_path = os.path.join(base_dir, "database", "veterinary_client.db")
        print(f"Intentando conectar a: {db_path}")
        
        # Verificamos si el archivo de base de datos ya existe.
        file_exists = os.path.isfile(db_path)
        
        # Conectarse a la base de datos.
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

        # Si el archivo no existe, ejecuta la inicialización.
        if not file_exists:
            self.initialize_database()
        
        self.conn.commit()

    def initialize_database(self):
        try:
            # Lee el script SQL desde el archivo.
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            sql_path = os.path.join(base_dir, "database", "veterinary_client.sql")
            with open(sql_path, 'r', encoding='utf-8') as sql_file:
                sql_script = sql_file.read()
                print("Contenido del script SQL:\n", sql_script)

            # Ejecuta todas las sentencias del script SQL.
            self.cursor.executescript(sql_script)
            self.conn.commit()
            print("Base de datos inicializada correctamente.")
        except Exception as e:
            print("Error durante la inicialización de la base de datos:")
            traceback.print_exc()
