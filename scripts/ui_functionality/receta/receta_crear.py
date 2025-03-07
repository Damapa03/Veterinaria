import os
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

from scripts.model.Receta import Receta
from scripts.repository.RecetaRepository import RecetaRepository


class RecetaCreateWindow(QtWidgets.QMainWindow):
    """Ventana para crear una nueva receta médica"""

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, '../../../ui/recetas_crear.ui')
        uic.loadUi(ui_path, self)

        # Inicializar repositorio
        self.recetaRepository = RecetaRepository()

        # Configurar título de la ventana
        self.setWindowTitle("Crear Receta Médica")

        # Conectar señales de botones
        self.volverButton.clicked.connect(self.on_volver_clicked)
        self.aceptarButton.clicked.connect(self.on_aceptar_clicked)

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
        pacient_value = self.pacientInput.text().strip()

        # Validar datos
        if not treatment_value or not pacient_value:
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
                pacient=pacient_value
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