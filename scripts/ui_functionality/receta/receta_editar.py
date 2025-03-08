import os
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QDate

from scripts.model.Receta import Receta
from scripts.repositories.RecetaRepository import RecetaRepository


class RecetaEditWindow(QtWidgets.QMainWindow):
    """Ventana para editar una receta médica existente"""

    def __init__(self, parent=None, receta_id=None):
        super().__init__()
        self.parent = parent
        self.receta_id = receta_id
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, '../../../ui/recetas_editar.ui')
        uic.loadUi(ui_path, self)

        # Inicializar repositorio
        self.recetaRepository = RecetaRepository()

        # Configurar título de la ventana
        self.setWindowTitle("Editar Receta Médica")

        # Conectar señales de botones
        self.volverButton.clicked.connect(self.on_volver_clicked)
        self.guardarButton.clicked.connect(self.on_guardar_clicked)

        # Cargar datos de la receta
        self.load_receta_data()

    def load_receta_data(self):
        """Cargar datos de la receta en los campos del formulario"""
        try:
            # Obtener receta desde el repositorio
            receta_data = self.recetaRepository.getReceta(self.receta_id)

            receta = Receta(
                id=receta_data[0],
                treatment=receta_data[1],
                start_date=receta_data[2],
                finalized=receta_data[3],
                pacient=receta_data[4]
            )

            if receta:
                # Rellenar los campos del formulario con los datos de la receta
                self.treatmentInput.setText(receta.treatment)

                # Convertir la fecha de string a QDate si es necesario
                if isinstance(receta.start_date, str):
                    date_parts = receta.start_date.split('-')
                    if len(date_parts) == 3:
                        qdate = QDate(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
                        self.startDateInput.setDate(qdate)

                # Convertir finalized a booleano si es string
                finalized_value = receta.finalized
                if isinstance(finalized_value, str):
                    finalized_value = finalized_value.lower() in ('true', 't', '1', 'yes')
                self.finalizedInput.setChecked(finalized_value)

                # Poblar el comboBox de pacientes
                self.populate_pacient_combo()

                # Configurar el valor actual basado en el paciente de la receta
                self.set_current_pacient(receta.pacient)
            else:
                QMessageBox.critical(self, "Error", "No se pudo encontrar la receta solicitada")
                self.on_volver_clicked()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar datos de la receta: {str(e)}")
            self.on_volver_clicked()

    def populate_pacient_combo(self):
        """Poblar el comboBox con los nombres de los animales"""
        try:
            # Primero limpiamos el comboBox
            self.pacientInput.clear()

            # Obtenemos la lista de animales desde el repositorio
            # Asumiendo que tienes una instancia de AnimalRepository
            from scripts.repositories.AnimalRepository import AnimalRepository
            animalRepository = AnimalRepository()
            animals = animalRepository.getAnimalsNameAndId()

            # Añadimos cada animal al comboBox
            for animal_id, animal_name in animals:
                # El texto visible es el nombre, pero el dato es el ID
                self.pacientInput.addItem(animal_name, animal_id)
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

    def on_guardar_clicked(self):
        """Actualizar la receta con los datos modificados del formulario"""
        # Recoger valores del formulario
        treatment_value = self.treatmentInput.text().strip()
        start_date_value = self.startDateInput.date().toString("yyyy-MM-dd")
        finalized_value = self.finalizedInput.isChecked()
        pacient_value = self.pacientInput.currentData()

        # Validar datos
        if not treatment_value or not pacient_value:
            QMessageBox.warning(self, "Datos incompletos",
                                "Tratamiento y paciente son campos obligatorios")
            return

        try:
            # Crear objeto receta actualizado
            receta = Receta(
                id=self.receta_id,
                treatment=treatment_value,
                start_date=start_date_value,
                finalized=finalized_value,
                pacient=pacient_value
            )

            # Actualizar en la base de datos
            result = self.recetaRepository.putReceta(receta.id,receta)

            if result:
                QMessageBox.information(self, "Éxito",
                                        "Receta médica actualizada correctamente")
                self.parent.parent.load_recetas()  # Recargar lista en ventana principal
                self.parent.parent.show()
                self.parent.close()
                self.close()
            else:
                QMessageBox.critical(self, "Error",
                                     "No se pudo actualizar la receta. Ha ocurrido un error en la base de datos.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al actualizar receta: {str(e)}")