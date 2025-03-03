class Animal:
    """Clase que representa un animal en una clínica veterinaria"""

    def __init__(self, id=None, name=None, species=None, description=None, owner=None):
        self.id = id
        self.name = name
        self.species = species
        self.description = description
        self.owner = owner

    def __str__(self):
        return f"Animal: {self.name} - {self.species} - Dueño: {self.owner}"