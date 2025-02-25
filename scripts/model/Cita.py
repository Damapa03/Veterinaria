
from datetime import date, time


class Cita:
    def __init__(self, id: str, fecha: date, hora: time, precio: int, motivo: str, animal: str, profesional: str):
        self.id = id
        self.fecha = fecha
        self.hora = hora
        self.precio = precio
        self.motivo = motivo
        self.animal = animal
        self.profesional = profesional