class Receta:
    """Clase que representa un controlador de recetas médicas"""

    def __init__(self, id=None, treatment=None, start_date=None, finalized=None, pacient=None):
        self.id = id
        self.treatment = treatment
        self.start_date = start_date
        self.finalized = finalized
        self.pacient = pacient

    def __str__(self):
        return f"Receta: {self.id} - Tratamiento: {self.treatment} - Paciente: {self.pacient}"