from DAO import Database
import sqlite3
from scripts.model.Cliente import Cliente

class ClienteController:
    def __init__(self):
        self.db = Database("veterinaria.db")

    def getClientes(self):
        self.db.cursor.execute("SELECT * FROM clientes")
        return self.db.cursor.fetchall()

    def getCliente(self, dni: str):
        self.db.cursor.execute("SELECT * FROM clientes WHERE dni = ?", (dni,))
        return self.db.cursor.fetchone()

    def postCliente(self, cliente: Cliente):
        try:
            self.db.cursor.execute("INSERT INTO clientes (dni, name, surname, email, tlfn) VALUES (?, ?, ?, ?, ?)", 
                                  (cliente.dni, cliente.name, cliente.surname, cliente.email, cliente.tlfn))
            self.db.conn.commit()
            return self.db.cursor.lastrowid
        except sqlite3.IntegrityError:
            print("Error: El cliente ya existe o hay un problema con los datos")
            return -1
    
    def putCliente(self, dni: str, cliente: Cliente):
        self.db.cursor.execute("UPDATE clientes SET name = ?, surname = ?, email = ?, tlfn = ? WHERE dni = ?", 
                              (cliente.name, cliente.surname, cliente.email, cliente.tlfn, dni))
        self.db.conn.commit()
        return self.db.cursor.rowcount > 0

    def deleteCliente(self, dni: str):
        self.db.cursor.execute("DELETE FROM clientes WHERE dni = ?", (dni,))
        self.db.conn.commit()
        return self.db.cursor.rowcount > 0
