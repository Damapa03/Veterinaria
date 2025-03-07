import os
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

from scripts.model.Animal import Animal
from scripts.repository.AnimalRepository import AnimalRepository


class AnimalCreateWindow(QtWidgets.QMainWindow):
    """Ventana para crear un nuevo animal"""

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, '../../../ui/animal_crear.ui')
        uic.loadUi(ui_path, self)

        # Inicializar repositorio
        self.animalRepository = AnimalRepository()

        # Configurar título de la ventana
        self.setWindowTitle("Crear Animal")

        # Conectar señales de botones
        self.volverButton.clicked.connect(self.on_volver_clicked)
        self.aceptarButton.clicked.connect(self.on_aceptar_clicked)

    def on_volver_clicked(self):
        """Volver a la pantalla principal"""
        self.parent.show()
        self.close()

    def on_aceptar_clicked(self):
        """Crear un nuevo animal con los datos del formulario"""
        # Recoger valores del formulario
        name_value = self.nameInput.text().strip()
        species_value = self.speciesInput.text().strip()
        description_value = self.descriptionInput.toPlainText().strip()
        owner_value = self.ownerInput.text().strip()

        # Validar datos
        if not name_value or not species_value or not owner_value:
            QMessageBox.warning(self, "Datos incompletos",
                                "Nombre, especie y dueño son campos obligatorios")
            return

        try:
            # Crear objeto animal
            animal = Animal(
                id=0,
                name=name_value,
                species=species_value,
                description=description_value,
                owner=owner_value
            )

            # Guardar en la base de datos
            result = self.animalRepository.postAnimal(animal)

            if result:
                QMessageBox.information(self, "Éxito",
                                        "Animal registrado correctamente")
                self.parent.load_animals()  # Recargar lista en ventana principal
                self.parent.show()
                self.close()
            else:
                QMessageBox.critical(self, "Error",
                                     "No se pudo registrar el animal. Ha ocurrido un error en la base de datos.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al registrar animal: {str(e)}")