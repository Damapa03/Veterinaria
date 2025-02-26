from typing import Optional

class Clinica:
    def __init__(self, id: Optional[int] = None, municipio: str = "", provincia: str = "", name: str = ""):
        self.id = id
        self.municipio = municipio
        self.provincia = provincia
        self.name = name
        
    def __str__(self):
        return f"{self.name} - {self.municipio}, {self.provincia}"