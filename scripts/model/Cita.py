
from datetime import date, time


class Cita:
    def __init__(self, fecha: date, precio: int, motivo: str, animal: str, profesional: str,id = None):
        self._id = id
        self._fecha = fecha
        self._precio = precio
        self._motivo = motivo
        self._animal = animal
        self._profesional = profesional
        
        def __getitem__(self, key):
            if key == 'id':
                return self._id
            elif key == 'motivo':
                return self._motivo
            elif key == 'animal':
                return self._animal
            elif key == 'profesional':
                return self._profesional
            elif key == 'fecha':
                return self._fecha
            elif key == 'precio':
                return self._precio
            else:
                raise KeyError(f"La clave '{key}' no existe")