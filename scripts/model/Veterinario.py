from typing import Optional

class Veterinario:
    def __init__(self, dni: str, name: str, surname: str, email: str, telephone: str, password: str, location: Optional[int] = None):
        self.dni = dni
        self.name = name
        self.surname = surname
        self.email = email
        self.telephone = telephone
        self.password = password
        self.location = location
        
    def __str__(self):
        return f"{self.name} {self.surname} (DNI: {self.dni})"