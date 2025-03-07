import sqlite3

from scripts.DAO import Database
from scripts.model.Animal import Animal

class AnimalRepository:
    def __init__(self):
        self.db = Database()
        
    def getAnimals(self):
        self.db.cursor.execute("SELECT * FROM Animales")
        return self.db.cursor.fetchall()
    
    def getAnimal(self, id: int):
        self.db.cursor.execute("SELECT * FROM Animales WHERE id = ?", (id,))
        return self.db.cursor.fetchone()

    def getAnimalName(self, id: int):
        self.db.cursor.execute("SELECT name FROM Animales WHERE id = ?", (id,))
        return self.db.cursor.fetchone()

    def getAnimalsNameAndId(self):
        self.db.cursor.execute("SELECT id, name FROM Animales")
        result = self.db.cursor.fetchall()
        return result

    def getAnimalsFilter(self, name: str, species: str, owner: str):
        # Replace empty strings with % for SQL LIKE wildcards
        name_param = name if name else "%"
        species_param = species if species else "%"
        owner_param = owner if owner else "%"

        self.db.cursor.execute("""
            SELECT a.id, a.name, a.species, a.description, a.owner FROM Animales a 
            JOIN Clientes c ON a.owner = c.DNI
            WHERE (? = '%' OR a.name LIKE ?)
            AND (? = '%' OR a.species LIKE ?)
            AND (? = '%' OR c.name LIKE ?)
        """, (name_param, name_param, species_param, species_param, owner_param, owner_param))

        result = self.db.cursor.fetchall()
        return result

    def getAnimalsByOwner(self, owner: str):
        self.db.cursor.execute("SELECT * FROM Animales WHERE owner = ?", (owner,))
        return self.db.cursor.fetchall()
        
    def getAnimalsBySpecies(self, species: str):
        self.db.cursor.execute("SELECT * FROM Animales WHERE species = ?", (species,))
        return self.db.cursor.fetchall()

    def postAnimal(self, animal: Animal):
        try:
            self.db.cursor.execute(
                "INSERT INTO Animales (name, species, description, owner) VALUES (?, ?, ?, ?)",
                (animal.name, animal.species, animal.description, animal.owner)
            )
            self.db.conn.commit()
            return self.db.cursor.lastrowid
        except sqlite3.IntegrityError:
            print("Error: Violation de restricción")
            return -1
   
    def putAnimal(self, id: int, animal: Animal):
        self.db.cursor.execute(
            "UPDATE Animales SET name = ?, species = ?, description = ?, owner = ? WHERE id = ?",
            (animal.name, animal.species, animal.description, animal.owner, id)
        )
        self.db.conn.commit()
        return True
        
    def deleteAnimal(self, id: int):
        self.db.cursor.execute("DELETE FROM Animales WHERE id = ?", (id,))
        self.db.conn.commit()
        return True