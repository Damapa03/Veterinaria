import os
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

from scripts.model.Animal import Animal
from scripts.repositories.AnimalRepository import AnimalRepository
from scripts.repositories.ClienteRepository import ClienteRepository


class AnimalDetailWindow(QtWidgets.QMainWindow):
    """Ventana para mostrar detalles de un animal"""

    def __init__(self, parent=None, animal=None):
        super().__init__()  # Remove parent parameter here
        self.parent_window = parent  # Store parent explicitly
        self.animal = animal
        self.edit_window = None  # Initialize the edit window reference

        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))),
                               'ui/animal_information.ui')
        try:
            uic.loadUi(ui_path, self)
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al cargar UI: {str(e)}")
            return

        # Inicializar repositorio
        self.animalRepository = AnimalRepository()
        self.clienteRepository = ClienteRepository()

        # Configurar título de la ventana
        self.setWindowTitle(f"Detalles de {animal.name}")

        # Mostrar información del animal
        self.display_animal_info()

        # Conectar señales de botones
        self.volverButton.clicked.connect(self.on_volver_clicked)
        self.modificarButton.clicked.connect(self.on_modificar_clicked)
        self.borrarButton.clicked.connect(self.on_borrar_clicked)

    def display_animal_info(self):
        """Mostrar la información del animal en la interfaz"""
        self.name.setText(self.animal.name)
        self.id.setText(f"ID: {self.animal.id}")
        self.species.setText(f"Especie: {self.animal.species}")
        self.description.setText(f"Descripción: {self.animal.description or 'No disponible'}")
        try:
            ownerName = self.clienteRepository.getClienteName(self.animal.owner)["name"]
            self.owner.setText(f"Dueño: {ownerName}")
        except Exception as e:
            self.owner.setText(f"Dueño: {self.animal.owner}")
            print(f"Error getting client name: {str(e)}")

    def on_volver_clicked(self):
        """Volver a la pantalla principal"""
        self.hide()  # Hide instead of close to prevent issues
        if self.parent_window:
            self.parent_window.show()

    def on_modificar_clicked(self):
        """Abrir ventana para modificar el animal"""
        try:
            # Import inside method to avoid circular import issues
            from scripts.ui_functionality.animal.animal_editar import AnimalEditWindow
            self.edit_window = AnimalEditWindow(self, self.animal)
            self.edit_window.show()
            self.hide()
        except Exception as e:
            print(f"Error opening edit window: {str(e)}")
            QMessageBox.critical(self, "Error", f"Error al abrir ventana de edición: {str(e)}")

    def on_borrar_clicked(self):
        """Eliminar el animal actual previa confirmación"""
        reply = QMessageBox.question(self, 'Confirmar eliminación',
                                     f'¿Está seguro de que desea eliminar al animal {self.animal.name}?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            try:
                # Intentar eliminar el animal
                result = self.animalRepository.deleteAnimal(self.animal.id)

                if result:
                    QMessageBox.information(self, "Éxito",
                                            "Animal eliminado correctamente")
                    self.parent_window.load_animals()  # Recargar lista en ventana principal
                    self.hide()  # Hide instead of close
                    self.parent_window.show()
                else:
                    QMessageBox.critical(self, "Error",
                                         "No se pudo eliminar el animal. Puede que esté asociado a tratamientos o recetas.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al eliminar animal: {str(e)}")