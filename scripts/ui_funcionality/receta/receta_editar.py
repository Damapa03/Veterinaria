import os
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QDate

from scripts.model.Receta import Receta
from scripts.repository.RecetaRepository import RecetaRepository


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
            receta = self.recetaRepository.getRecetaById(self.receta_id)
            
            if receta:
                # Rellenar los campos del formulario con los datos de la receta
                self.treatmentInput.setText(receta.treatment)
                
                # Convertir la fecha de string a QDate si es necesario
                if isinstance(receta.start_date, str):
                    date_parts = receta.start_date.split('-')
                    if len(date_parts) == 3:
                        qdate = QDate(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
                        self.startDateInput.setDate(qdate)
                
                self.finalizedCheckBox.setChecked(receta.finalized)
                self.pacientInput.setText(receta.pacient)
            else:
                QMessageBox.critical(self, "Error", "No se pudo encontrar la receta solicitada")
                self.on_volver_clicked()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar datos de la receta: {str(e)}")
            self.on_volver_clicked()

    def on_volver_clicked(self):
        """Volver a la pantalla principal"""
        self.parent.show()
        self.close()

    def on_guardar_clicked(self):
        """Actualizar la receta con los datos modificados del formulario"""
        # Recoger valores del formulario
        treatment_value = self.treatmentInput.text().strip()
        start_date_value = self.startDateInput.date().toString("yyyy-MM-dd")
        finalized_value = self.finalizedCheckBox.isChecked()
        pacient_value = self.pacientInput.text().strip()

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
            result = self.recetaRepository.updateReceta(receta)

            if result:
                QMessageBox.information(self, "Éxito",
                                        "Receta médica actualizada correctamente")
                self.parent.load_recetas()  # Recargar lista en ventana principal
                self.parent.show()
                self.close()
            else:
                QMessageBox.critical(self, "Error",
                                     "No se pudo actualizar la receta. Ha ocurrido un error en la base de datos.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al actualizar receta: {str(e)}")