import sqlite3

from scripts.DAO import Database
from scripts.model.Animal import Animal

class AnimalRepository:
    def __init__(self):
        self.db = Database()
        
    def getAnimals(self):
        self.db.cursor.execute("SELECT * FROM Animals")
        return self.db.cursor.fetchall()
    
    def getAnimal(self, id: int):
        self.db.cursor.execute("SELECT * FROM Animals WHERE id = ?", (id,))
        return self.db.cursor.fetchone()

    def getAnimalName(self, id: int):
        self.db.cursor.execute("SELECT name FROM Animals WHERE id = ?", (id,))
        return self.db.cursor.fetchone()

    def getAnimalsNameAndId(self):
        self.db.cursor.execute("SELECT id, name FROM Animals")
        result = self.db.cursor.fetchall()
        print(f"Animals fetched: {result}")  # Salida de depuración
        return result
        
    def getAnimalsByOwner(self, owner: str):
        self.db.cursor.execute("SELECT * FROM Animals WHERE owner = ?", (owner,))
        return self.db.cursor.fetchall()
        
    def getAnimalsBySpecies(self, species: str):
        self.db.cursor.execute("SELECT * FROM Animals WHERE species = ?", (species,))
        return self.db.cursor.fetchall()

    def postAnimal(self, animal: Animal):
        try:
            self.db.cursor.execute(
                "INSERT INTO Animals (name, species, description, owner) VALUES (?, ?, ?, ?)", 
                (animal.name, animal.species, animal.description, animal.owner)
            )
            self.db.conn.commit()
            return self.db.cursor.lastrowid
        except sqlite3.IntegrityError:
            print("Error: Violation de restricción")
            return -1
   
    def putAnimal(self, id: int, animal: Animal):
        self.db.cursor.execute(
            "UPDATE Animals SET name = ?, species = ?, description = ?, owner = ? WHERE id = ?", 
            (animal.name, animal.species, animal.description, animal.owner, id)
        )
        self.db.conn.commit()
        return True
        
    def deleteAnimal(self, id: int):
        self.db.cursor.execute("DELETE FROM Animals WHERE id = ?", (id,))
        self.db.conn.commit()
        return True