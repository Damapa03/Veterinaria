import os
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

from scripts.model.Animal import Animal
from scripts.repositories.AnimalRepository import AnimalRepository


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
        self.populate_owner_combo()
        self.set_current_client(self.animal.owner)

    def populate_owner_combo(self):
        """Poblar el comboBox con los nombres de los clientes"""
        try:
            # Primero limpiamos el comboBox
            self.ownerInput.clear()

            # Obtenemos la lista de clientes desde el repositorio
            from scripts.repositories.ClienteRepository import ClienteRepository
            clienteRepository = ClienteRepository()
            clientes = clienteRepository.getClientesNameAndId()

            # Añadimos cada cliente al comboBox
            for cliente_id, cliente_name in clientes:
                # El texto visible es el nombre, pero el dato es el ID
                self.ownerInput.addItem(cliente_name, cliente_id)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar la lista de clientes: {str(e)}")


    def set_current_client(self, client_id):
        """Establecer el valor actual en el comboBox basado en el ID del cliente"""
        try:
            # Convertir a entero si es necesario
            if isinstance(client_id, str) and client_id.isdigit():
                client_id = int(client_id)

            # Buscar el índice que corresponde al ID del cliente
            index = self.ownerInput.findData(client_id)

            # Si encontramos el índice, configuramos el comboBox
            if index >= 0:
                self.ownerInput.setCurrentIndex(index)
        except Exception as e:
            QMessageBox.warning(self, "Advertencia", f"No se pudo seleccionar el cliente actual: {str(e)}")

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

        # Get owner ID from comboBox instead of text
        owner_id = self.ownerInput.currentData()

        # Validar datos
        if not name_value or not species_value or owner_id is None:
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
                owner=owner_id
            )

            # Guardar cambios en la base de datos
            result = self.animalRepository.putAnimal(updated_animal.id, updated_animal)

            if result:
                QMessageBox.information(self, "Éxito",
                                        "Animal actualizado correctamente")

                # Actualizar animal en la ventana padre
                self.parent.animal = updated_animal
                self.parent.display_animal_info()

                # Recargar lista en ventana principal si existe
                if hasattr(self.parent, 'parent') and self.parent.parent:
                    self.parent.parent.load_animals()

                # Volver a la pantalla de detalles
                self.parent.show()
                self.close()
            else:
                QMessageBox.critical(self, "Error",
                                     "No se pudo actualizar el animal")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al actualizar animal: {str(e)}")