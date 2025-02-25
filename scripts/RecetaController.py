from DAO import Database
import sqlite3
from scripts.model.Receta import Receta

class RecetaController:
    def __init__(self):
        self.db = Database("veterinaria.db")

    def getRecetas(self):
        self.db.cursor.execute("SELECT * FROM recetas")
        return self.db.cursor.fetchall()

    def getReceta(self, id: str):
        self.db.cursor.execute("SELECT * FROM recetas WHERE id = ?", (id,))
        return self.db.cursor.fetchone()

    def postReceta(self, receta: Receta):
        try:
            if receta.finalized <= receta.start_date:
                raise ValueError("La fecha de finalización debe ser posterior a la de inicio.")
            
            self.db.cursor.execute("INSERT INTO recetas (id, treatment, start_date, finalized, pacient) VALUES (?, ?, ?, ?, ?)",
                                   (receta.id, receta.treatment, receta.start_date, receta.finalized, receta.pacient))
            self.db.conn.commit()
            return self.db.cursor.lastrowid
        except sqlite3.IntegrityError:
            print("Error: No se pudo insertar la receta.")
            return -1
    
    def putReceta(self, id: str, receta: Receta):
        if receta.finalized <= receta.start_date:
            raise ValueError("La fecha de finalización debe ser posterior a la de inicio.")

        self.db.cursor.execute("UPDATE recetas SET treatment = ?, start_date = ?, finalized = ?, pacient = ? WHERE id = ?",
                               (receta.treatment, receta.start_date, receta.finalized, receta.pacient, id))
        self.db.conn.commit()

    def deleteReceta(self, id: str):
        self.db.cursor.execute("DELETE FROM recetas WHERE id = ?", (id,))
        self.db.conn.commit()

