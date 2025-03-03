import os
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

from scripts.model.Animal import Animal
from scripts.repository.AnimalRepository import AnimalRepository


class AnimalEditWindow(QtWidgets.QMainWindow):
    """Ventana para editar un animal existente"""

    def __init__(self, parent=None, animal=None):
        super().__init__()
        self.parent = parent
        self.animal = animal
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, '../../../ui/animal_editar.ui')
        uic.loadUi(ui_path, self)

        # Inicializar repositorio
        self.animalRepository = AnimalRepository()

        # Configurar título de la ventana
        self.setWindowTitle(f"Editar {animal.name}")

        # Cargar datos actuales del animal
        self.load_animal_data()

        # Conectar señales de botones
        self.volverButton.clicked.connect(self.on_volver_clicked)
        self.guardarButton.clicked.connect(self.on_guardar_clicked)

    def load_animal_data(self):
        """Cargar los datos actuales del animal en el formulario"""
        self.idDisplay.setText(str(self.animal.id))
        self.nameInput.setText(self.animal.name)
        self.speciesInput.setText(self.animal.species)
        self.descriptionInput.setPlainText(self.animal.description)
        self.ownerInput.setText(self.animal.owner)

    def on_volver_clicked(self):
        """Volver a la pantalla de detalles"""
        self.parent.show()
        self.close()

    def on_guardar_clicked(self):
        """Guardar los cambios realizados al animal"""
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
            # Actualizar objeto animal con nuevos valores
            updated_animal = Animal(
                id=self.animal.id,
                name=name_value,
                species=species_value,
                description=description_value,
                owner=owner_value
            )

            # Guardar cambios en la base de datos
            result = self.animalRepository.putAnimal(updated_animal.id, updated_animal)

            if result:
                QMessageBox.information(self, "Éxito",
                                        "Animal actualizado correctamente")

                # Actualizar animal en la ventana padre
                self.parent.animal = updated_animal
                self.parent.display_animal_info()

                # Recargar lista en ventana principal
                self.parent.parent.load_animals()

                # Volver a la pantalla de detalles
                self.parent.show()
                self.close()
            else:
                QMessageBox.critical(self, "Error",
                                     "No se pudo actualizar el animal")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al actualizar animal: {str(e)}")