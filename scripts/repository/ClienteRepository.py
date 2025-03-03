from model.Cliente import Cliente
from database.SQLiteDatabase import SQLiteDatabase

class ClienteRepository:
    def __init__(self):
        self.sqlite_db = SQLiteDatabase()
        if not self.sqlite_db.is_connected():
            raise ConnectionError("No hay conexión a SQLite")
        self.table = 'clientes'
    
    def getClientes(self):
        """Obtiene todos los clientes de SQLite"""
        try:
            self.sqlite_db.cursor.execute(f"SELECT dni, name, surname, email, telephone FROM {self.table}")
            rows = self.sqlite_db.cursor.fetchall()
            
            # Convertir filas a diccionarios
            clientes = []
            for row in rows:
                cliente = {
                    "dni": row[0],
                    "name": row[1],
                    "surname": row[2],
                    "email": row[3],
                    "telephone": row[4]
                }
                clientes.append(cliente)
            
            return clientes
        except Exception as e:
            print(f"Error al obtener clientes: {e}")
            return []
    
    def getCliente(self, dni):
        """Obtiene un cliente por su DNI"""
        try:
            self.sqlite_db.cursor.execute(
                f"SELECT dni, name, surname, email, telephone FROM {self.table} WHERE dni = ?", 
                (dni,)
            )
            row = self.sqlite_db.cursor.fetchone()
            
            if row:
                cliente = {
                    "dni": row[0],
                    "name": row[1],
                    "surname": row[2],
                    "email": row[3],
                    "telephone": row[4]
                }
                return cliente
            return None
        except Exception as e:
            print(f"Error al obtener cliente {dni}: {e}")
            return None
    
    def postCliente(self, cliente):
        """Añade un nuevo cliente a SQLite"""
        if not isinstance(cliente, Cliente):
            raise TypeError("El parámetro debe ser un objeto Cliente")
        
        try:
            # Verifica primero si ya existe
            if self.getCliente(cliente.dni) is not None:
                print(f"El cliente con DNI {cliente.dni} ya existe")
                return False
            
            # Insertar el nuevo cliente
            self.sqlite_db.cursor.execute(
                f"INSERT INTO {self.table} (dni, name, surname, email, telephone) VALUES (?, ?, ?, ?, ?)",
                (cliente.dni, cliente.name, cliente.surname, cliente.email, cliente.tlfn)
            )
            self.sqlite_db.conn.commit()
            return True
        except Exception as e:
            print(f"Error al añadir cliente: {e}")
            return False
    
    def putCliente(self, dni, cliente):
        """Actualiza un cliente existente en SQLite"""
        if not isinstance(cliente, Cliente):
            raise TypeError("El parámetro debe ser un objeto Cliente")
        
        try:
            # Verifica si el cliente existe
            if self.getCliente(dni) is None:
                print(f"El cliente con DNI {dni} no existe")
                return False
            
            # Si el DNI ha cambiado, elimina el antiguo y crea uno nuevo
            if dni != cliente.dni:
                # Comenzar una transacción para garantizar la integridad
                self.sqlite_db.cursor.execute("BEGIN TRANSACTION")
                
                # Eliminar el cliente con el DNI antiguo
                self.sqlite_db.cursor.execute(f"DELETE FROM {self.table} WHERE dni = ?", (dni,))
                
                # Insertar el cliente con el nuevo DNI
                self.sqlite_db.cursor.execute(
                    f"INSERT INTO {self.table} (dni, name, surname, email, telephone) VALUES (?, ?, ?, ?, ?)",
                    (cliente.dni, cliente.name, cliente.surname, cliente.email, cliente.tlfn)
                )
                
                # Confirmar la transacción
                self.sqlite_db.conn.commit()
            else:
                # Si el DNI es el mismo, simplemente actualiza los otros campos
                self.sqlite_db.cursor.execute(
                    f"UPDATE {self.table} SET name = ?, surname = ?, email = ?, telephone = ? WHERE dni = ?",
                    (cliente.name, cliente.surname, cliente.email, cliente.tlfn, dni)
                )
                self.sqlite_db.conn.commit()
            
            return True
        except Exception as e:
            # En caso de error, revertir cualquier cambio parcial
            self.sqlite_db.conn.rollback()
            print(f"Error al actualizar cliente: {e}")
            return False
    
    def deleteCliente(self, dni):
        """Elimina un cliente de SQLite"""
        try:
            # Verifica si el cliente existe
            if self.getCliente(dni) is None:
                print(f"El cliente con DNI {dni} no existe")
                return False
            
            # Elimina el cliente
            self.sqlite_db.cursor.execute(f"DELETE FROM {self.table} WHERE dni = ?", (dni,))
            self.sqlite_db.conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
            return False