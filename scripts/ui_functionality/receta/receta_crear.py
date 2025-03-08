import os
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

from scripts.model.Receta import Receta
from scripts.repositories.RecetaRepository import RecetaRepository
from scripts.repositories.AnimalRepository import AnimalRepository


class RecetaCreateWindow(QtWidgets.QMainWindow):
    """Ventana para crear una nueva receta médica"""

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, '../../../ui/recetas_crear.ui')
        uic.loadUi(ui_path, self)

        # Inicializar repositorios
        self.recetaRepository = RecetaRepository()
        self.animalRepository = AnimalRepository()

        # Configurar título de la ventana
        self.setWindowTitle("Crear Receta Médica")

        # Poblar el comboBox de pacientes
        self.populate_pacient_combo()

        # Conectar señales de botones
        self.volverButton.clicked.connect(self.on_volver_clicked)
        self.aceptarButton.clicked.connect(self.on_aceptar_clicked)

    def populate_pacient_combo(self):
        """Poblar el comboBox con los nombres de los animales"""
        try:
            # Primero limpiamos el comboBox
            self.pacientInput.clear()

            # Obtenemos la lista de animales desde el repositorio
            animals = self.animalRepository.getAnimalsNameAndId()

            # Añadimos cada animal al comboBox
            for animal_id, animal_name in animals:
                # El texto visible es el nombre, pero el dato es el ID
                self.pacientInput.addItem(animal_name, animal_id)

            # Seleccionamos el primer elemento por defecto
            if self.pacientInput.count() > 0:
                self.pacientInput.setCurrentIndex(0)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar la lista de pacientes: {str(e)}")

    def set_current_pacient(self, pacient_id):
        """Establecer el valor actual en el comboBox basado en el ID del paciente"""
        try:
            # Convertir a entero si es necesario
            if isinstance(pacient_id, str) and pacient_id.isdigit():
                pacient_id = int(pacient_id)

            # Buscar el índice que corresponde al ID del paciente
            index = self.pacientInput.findData(pacient_id)

            # Si encontramos el índice, configuramos el comboBox
            if index >= 0:
                self.pacientInput.setCurrentIndex(index)
        except Exception as e:
            QMessageBox.warning(self, "Advertencia", f"No se pudo seleccionar el paciente actual: {str(e)}")

    def on_volver_clicked(self):
        """Volver a la pantalla principal"""
        self.parent.show()
        self.close()

    def on_aceptar_clicked(self):
        """Crear una nueva receta con los datos del formulario"""
        # Recoger valores del formulario
        treatment_value = self.treatmentInput.text().strip()
        start_date_value = self.startDateInput.date().toString("yyyy-MM-dd")
        finalized_value = self.finalizedCheckBox.isChecked()

        # Obtener el ID del paciente seleccionado del comboBox
        pacient_id = self.pacientInput.currentData()

        # Validar datos
        if not treatment_value or pacient_id is None:
            QMessageBox.warning(self, "Datos incompletos",
                                "Tratamiento y paciente son campos obligatorios")
            return

        try:
            # Crear objeto receta
            receta = Receta(
                id=0,
                treatment=treatment_value,
                start_date=start_date_value,
                finalized=finalized_value,
                pacient=pacient_id  # Ahora usamos el ID del animal
            )

            # Guardar en la base de datos
            result = self.recetaRepository.postReceta(receta)

            if result:
                QMessageBox.information(self, "Éxito",
                                        "Receta médica registrada correctamente")
                self.parent.load_recetas()  # Recargar lista en ventana principal
                self.parent.show()
                self.close()
            else:
                QMessageBox.critical(self, "Error",
                                     "No se pudo registrar la receta. Ha ocurrido un error en la base de datos.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al registrar receta: {str(e)}")