import os
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

from scripts.model.Animal import Animal
from scripts.repositories.AnimalRepository import AnimalRepository


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
        self.populate_owner_combo()

        # Configurar título de la ventana
        self.setWindowTitle("Crear Animal")

        # Conectar señales de botones
        self.volverButton.clicked.connect(self.on_volver_clicked)
        self.aceptarButton.clicked.connect(self.on_aceptar_clicked)

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
        owner_value = self.ownerInput.currentData()

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