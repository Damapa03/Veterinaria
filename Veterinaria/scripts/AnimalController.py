
from DAO import Database
import sqlite3
from scripts.model.Cita import Cita

class CitaController:
    def __init__(self):
        self.db = Database("veterinaria.db")

    def getCitas(self):
        self.db.cursor.execute("SELECT * FROM citas")
        return self.db.cursor.fetchall()

    def getCita(self,id: str):
        self.db.cursor.execute("SELECT * FROM citas WHERE id = ?", (id))
        return self.db.cursor.fetchone()

    def postCitas(self,cita: Cita):
        try:
            self.db.cursor.execute("INSERT INTO citas (id,fecha,hora,precio,motivo,animal,profesional)", (cita.id,cita.fecha,cita.hora,cita.precio,cita.motivo,cita.animal,cita.profesional))
            self.db.conn.commit()
            return self.db.cursor.lastrowid
        except sqlite3.IntegrityError:
            print("Error")
            return -1
    
    def putCita(self,id: str, cita: Cita):
        self.db.cursor.execute("UPDATE citas SET fecha = ?,hora = ?,precio = ?,motivo = ?,animal = ?,profesional = ? WHERE id = ?", (cita.fecha,cita.hora,cita.precio,cita.motivo,cita.animal,cita.profesional, id))
        self.db.conn.commit()

    def deleteCita(self,id: str):
        self.db.cursor.execute("DELETE FROM citas WHERE id = ?", (id))
        self.db.conn.commit