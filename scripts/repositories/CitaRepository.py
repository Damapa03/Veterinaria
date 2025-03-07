from ..DAO import Database
import sqlite3
from scripts.model.Cita import Cita

class CitaRepository:
    def __init__(self):
        self.db = Database()

    def getCitas(self):
        self.db.cursor.execute("SELECT c.id, c.date, c.price, c.reason, a.name, v.name  FROM Cita c, Animales a, Veterinario v WHERE v.DNI = c.professional AND a.id = c.animal")
        return self.db.cursor.fetchall()

    def getCita(self,id: str):
        self.db.cursor.execute("SELECT * FROM Cita WHERE id = ?", (id))
        return self.db.cursor.fetchone()

    def postCita(self,cita: Cita):
        try:
            self.db.cursor.execute("INSERT INTO Cita (id,date,price,reason,animal,professional) VALUES (?,?,?,?,?,?)", (cita._id,cita._fecha,cita._precio,cita._motivo,cita._animal,cita._profesional))
            self.db.conn.commit()
            return self.db.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Error {e}" )
            return -1
    
    def putCita(self, id: str, cita: Cita):
        try:
            self.db.cursor.execute("UPDATE Cita SET date = ?, price = ?, reason = ?, animal = ?, professional = ? WHERE id = ?", 
                                (cita._fecha, cita._precio, cita._motivo, cita._animal, cita._profesional, id,))
            self.db.conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")

    def deleteCita(self, id: str):   
        try:
            self.db.cursor.execute("DELETE FROM Cita WHERE id = ?", (id,))  # Nota la coma aquí
            self.db.conn.commit()  # Nota: faltaba los paréntesis ()
        except sqlite3.IntegrityError as e:
            print(f"Error {e}") 

    def getVetarinarioNombreDNI(self): 
       self.db.cursor.execute("SELECT DNI, name FROM Veterinario")
       return self.db.cursor.fetchall()        
    
    def getAnimal(self):
        self.db.cursor.execute("SELECT id, name FROM Animales")
        return self.db.cursor.fetchall()