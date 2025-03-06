import os
import sqlite3
import traceback

class Database:
    def __init__(self):
        # Obtiene la ruta absoluta del directorio base y construye la ruta de la base de datos
        script_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(script_dir)
        self.db_path = os.path.join(base_dir, "database", "veterinary_client.db")
        print(f"Intentando conectar a: {self.db_path}")
        
        # Verifica si el archivo de la base de datos ya existe
        db_exists = os.path.isfile(self.db_path)
        
        # Conecta a la base de datos
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row  # Para acceder a las filas como diccionarios
        self.cursor = self.conn.cursor()
        
        # Solo inicializa si el archivo no existe
        if not db_exists:
            self.initialize_database()
        
        self.conn.commit()

    def initialize_database(self):
        try:
            # Obtiene la ruta del archivo SQL (asegúrate que la ruta y el nombre sean correctos)
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            sql_path = os.path.join(base_dir, "database", "veterinary_client.sql")
            with open(sql_path, 'r', encoding='utf-8') as sql_file:
                sql_script = sql_file.read()
                print("Contenido del script SQL:\n", sql_script)
            
            # Ejecuta el script completo para crear las tablas e insertar los datos de ejemplo
            self.cursor.executescript(sql_script)
            self.conn.commit()
            print("Base de datos inicializada correctamente.")
        except Exception as e:
            print("Error durante la inicialización de la base de datos:")
            traceback.print_exc()
