import sqlite3

from scripts.DAO import Database
from scripts.model.Receta import Receta

class RecetaRepository:
    def __init__(self):
        self.db = Database()
        
    def getRecetas(self):
        self.db.cursor.execute("SELECT * FROM Recetas")
        return self.db.cursor.fetchall()
    
    def getReceta(self, id: int):
        self.db.cursor.execute("SELECT * FROM Recetas WHERE id = ?", (id,))
        return self.db.cursor.fetchone()

    def getRecetasByPacient(self, pacient_id: int):
        self.db.cursor.execute("SELECT * FROM Recetas WHERE pacient = ?", (pacient_id,))
        return self.db.cursor.fetchall()
        
    def getActiveRecetas(self):
        self.db.cursor.execute("SELECT * FROM Recetas WHERE finalized = 0")
        return self.db.cursor.fetchall()

    def getRecetasFinalized(self):
        self.db.cursor.execute("SELECT * FROM Recetas WHERE finalized = 1")
        return self.db.cursor.fetchall()
    
    def getRecetasByTreatment(self, treatment: str):
        self.db.cursor.execute("SELECT * FROM Recetas WHERE treatment LIKE ?", (f"%{treatment}%",))
        return self.db.cursor.fetchall()

    def postReceta(self, receta: Receta):
        try:
            self.db.cursor.execute(
                "INSERT INTO Recetas (treatment, start_date, finalized, pacient) VALUES (?, ?, ?, ?)", 
                (receta.treatment, receta.start_date, receta.finalized, receta.pacient)
            )
            self.db.conn.commit()
            return self.db.cursor.lastrowid
        except sqlite3.IntegrityError:
            print("Error: Violation de restricción")
            return -1
   
    def putReceta(self, id: int, receta: Receta):
        self.db.cursor.execute(
            "UPDATE Recetas SET treatment = ?, start_date = ?, finalized = ?, pacient = ? WHERE id = ?", 
            (receta.treatment, receta.start_date, receta.finalized, receta.pacient, id)
        )
        self.db.conn.commit()
        return True
        
    def finalizeReceta(self, id: int):
        self.db.cursor.execute("UPDATE Recetas SET finalized = 1 WHERE id = ?", (id,))
        self.db.conn.commit()
        return True
        
    def deleteReceta(self, id: int):
        self.db.cursor.execute("DELETE FROM Recetas WHERE id = ?", (id,))
        self.db.conn.commit()
        return True