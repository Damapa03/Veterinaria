from DAO import Database
import sqlite3
from model.Cliente import Cliente

class ClienteRepository:
    def __init__(self):
        self.db = Database()
        
    def getClientes(self):
        self.db.cursor.execute("SELECT * FROM Clientes")
        rows = self.db.cursor.fetchall()
        col_names = [desc[0] for desc in self.db.cursor.description]
        return [dict(zip(col_names, row)) for row in rows]
    
    def getCliente(self, dni: str):
        self.db.cursor.execute("SELECT * FROM Clientes WHERE DNI = ?", (dni,))
        row = self.db.cursor.fetchone()
        if row:
            col_names = [desc[0] for desc in self.db.cursor.description]
            return dict(zip(col_names, row))
        return None
    
    def postCliente(self, cliente: Cliente):
        try:
            self.db.cursor.execute(
                "INSERT INTO Clientes (DNI, name, surname, email, telephone) VALUES (?, ?, ?, ?, ?)", 
                (cliente.dni, cliente.name, cliente.surname, cliente.email, cliente.tlfn)
            )
            self.db.conn.commit()
            print(f"Cliente insertado: {cliente.dni}")  # Para debug
            return None  # Indica éxito
        except sqlite3.IntegrityError as e:
            print(f"Error de integridad: {e}")  # Para debug
            return str(e)
        except Exception as e:
            print(f"Error inesperado: {e}")  # Para debug
            self.db.conn.rollback()  # Asegúrate de hacer rollback en caso de error
            return str(e)
   
    def putCliente(self, original_dni: str, cliente: Cliente):
        try:
            self.db.cursor.execute(
                "UPDATE Clientes SET DNI = ?, name = ?, surname = ?, email = ?, telephone = ? WHERE DNI = ?",
                (cliente.dni, cliente.name, cliente.surname, cliente.email, cliente.tlfn, original_dni)
            )
            self.db.conn.commit()
            if original_dni != cliente.dni:
                self.db.cursor.execute(
                    "UPDATE Animales SET owner = ? WHERE owner = ?", (cliente.dni, original_dni)
                )
                self.db.conn.commit()
            return None
        except sqlite3.IntegrityError as e:
            return str(e)
        
    def deleteCliente(self, dni: str):
        self.db.cursor.execute("DELETE FROM Clientes WHERE DNI = ?", (dni,))
        self.db.conn.commit()
