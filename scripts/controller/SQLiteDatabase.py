import sqlite3
import os

class SQLiteDatabase:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SQLiteDatabase, cls).__new__(cls)
            # Inicializa la conexión a SQLite
            try:
                # Asegurarse que existe el directorio de datos
                data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
                if not os.path.exists(data_dir):
                    os.makedirs(data_dir)
                
                # Crear la conexión a la base de datos
                db_path = os.path.join(data_dir, 'clientes.db')
                cls._instance.conn = sqlite3.connect(db_path)
                cls._instance.cursor = cls._instance.conn.cursor()
                
                # Crear la tabla si no existe
                cls._instance.cursor.execute('''
                CREATE TABLE IF NOT EXISTS clientes (
                    dni TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    surname TEXT,
                    email TEXT,
                    telephone TEXT
                )
                ''')
                cls._instance.conn.commit()
                print("Conexión a SQLite establecida correctamente")
            except Exception as e:
                print(f"Error al conectar con SQLite: {e}")
                cls._instance.conn = None
                cls._instance.cursor = None
        return cls._instance
    
    def is_connected(self):
        """Verifica si la conexión a SQLite está activa"""
        return self.conn is not None and self.cursor is not None
    
    def close(self):
        """Cierra la conexión a la base de datos"""
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None