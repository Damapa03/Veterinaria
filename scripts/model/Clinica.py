class Clinica:
    """Clase que representa una clínica veterinaria"""

    def __init__(self, id=None, name=None, municipio=None, provincia=None):
        self.id = id
        self.name = name
        self.municipio = municipio
        self.provincia = provincia

    def __str__(self):
        return f"Clínica: {self.name} - {self.municipio}, {self.provincia}"