from scripts.DAO import Database
import sqlite3
from scripts.model.Clinica import Clinica

class ClinicaController:
    def __init__(self):
        self.db = Database("veterinaria_clinic.db")
        
    def getClinicas(self):
        self.db.cursor.execute("SELECT * FROM Clinicas")
        return self.db.cursor.fetchall()
    
    def getClinica(self, id: int):
        self.db.cursor.execute("SELECT * FROM Clinicas WHERE id = ?", (id,))
        return self.db.cursor.fetchone()
    
    def postClinica(self, clinica: Clinica):
        try:
            self.db.cursor.execute(
                "INSERT INTO Clinicas (Municipio, Provincia, name) VALUES (?, ?, ?)", 
                (clinica.municipio, clinica.provincia, clinica.name)
            )
            self.db.conn.commit()
            return self.db.cursor.lastrowid
        except sqlite3.IntegrityError:
            print("Error: Constraint violation")
            return -1
   
    def putClinica(self, id: int, clinica: Clinica):
        self.db.cursor.execute(
            "UPDATE Clinicas SET Municipio = ?, Provincia = ?, name = ? WHERE id = ?", 
            (clinica.municipio, clinica.provincia, clinica.name, id)
        )
        self.db.conn.commit()
        
    def deleteClinica(self, id: int):
        self.db.cursor.execute("DELETE FROM Clinicas WHERE id = ?", (id,))
        self.db.conn.commit()