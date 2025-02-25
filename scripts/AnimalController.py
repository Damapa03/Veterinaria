from DAO import Database
import sqlite3
from scripts.model.Animal import Animal

class AnimalController:
    def __init__(self):
        self.db = Database("veterinaria.db")

    def getAnimales(self):
        self.db.cursor.execute("SELECT * FROM animales")
        return self.db.cursor.fetchall()

    def getAnimal(self, id: str):
        self.db.cursor.execute("SELECT * FROM animales WHERE id = ?", (id,))
        return self.db.cursor.fetchone()

    def postAnimal(self, animal: Animal):
        try:
            self.db.cursor.execute("INSERT INTO animales (id, name, species, description, owner) VALUES (?, ?, ?, ?, ?)",
                                   (animal.id, animal.name, animal.species, animal.description, animal.owner))
            self.db.conn.commit()
            return self.db.cursor.lastrowid
        except sqlite3.IntegrityError:
            print("Error: No se pudo insertar el animal.")
            return -1
    
    def putAnimal(self, id: str, animal: Animal):
        self.db.cursor.execute("UPDATE animales SET name = ?, species = ?, description = ?, owner = ? WHERE id = ?",
                               (animal.name, animal.species, animal.description, animal.owner, id))
        self.db.conn.commit()

    def deleteAnimal(self, id: str):
        self.db.cursor.execute("DELETE FROM animales WHERE id = ?", (id,))
        self.db.conn.commit()
