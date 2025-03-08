from scripts.DAO import Database
import sqlite3
from scripts.model.Veterinario import Veterinario

class VeterinarioRepository:
    def __init__(self):
        self.db = Database()
        
    def getVeterinarios(self):
        self.db.cursor.execute("SELECT * FROM Veterinario")
        return self.db.cursor.fetchall()
    
    def getVeterinario(self, dni: str):
        self.db.cursor.execute("SELECT * FROM Veterinario WHERE dni = ?", (dni,))
        return self.db.cursor.fetchone()
    
    def postVeterinario(self, veterinario: Veterinario):
        try:
            self.db.cursor.execute(
                "INSERT INTO Veterinario (DNI, name, surname, email, telephone, password, location) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                (veterinario.dni, veterinario.name, veterinario.surname, veterinario.email, veterinario.telephone, veterinario.password, veterinario.location)
            )
            self.db.conn.commit()
            return self.db.cursor.lastrowid
        except sqlite3.IntegrityError:
            return sqlite3.IntegrityError
   
    def putVeterinario(self, dni: str, veterinario: Veterinario):
        try:
            self.db.cursor.execute(
                "UPDATE Veterinario SET name = ?, surname = ?, email = ?, telephone = ?, password = ?, location = ? WHERE DNI = ?",
                (veterinario.name, veterinario.surname, veterinario.email, veterinario.telephone, veterinario.password, veterinario.location, dni)
            )
            self.db.conn.commit()
        except sqlite3.IntegrityError:
            return sqlite3.IntegrityError
        
    def deleteVeterinario(self, dni: str):
        self.db.cursor.execute("DELETE FROM Veterinario WHERE DNI = ?", (dni,))
        self.db.conn.commit()
