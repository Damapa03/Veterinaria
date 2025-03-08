import os
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

from scripts.model.Clinica import Clinica
from scripts.repositories.ClinicaRepository import ClinicaRepository


class ClinicaCreateWindow(QtWidgets.QMainWindow):
    """Ventana para crear una nueva clínica"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))),
                               'ui/clinicas_crear.ui')
        try:
            uic.loadUi(ui_path, self)
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al cargar UI: {str(e)}")
            return

        # Inicializar repositorio
        self.clinicaRepository = ClinicaRepository()

        # Configurar título de la ventana
        self.setWindowTitle("Crear Clínica")

        # Conectar señales de botones
        self.volverButton.clicked.connect(self.on_volver_clicked)
        self.aceptarButton.clicked.connect(self.on_aceptar_clicked)

    def on_volver_clicked(self):
        """Volver a la pantalla principal"""
        if self.parent_window:
            self.parent_window.show()
        self.close()

    def on_aceptar_clicked(self):
        """Crear una nueva clínica con los datos del formulario"""
        # Recoger valores del formulario
        name_value = self.nameInput.text().strip()
        municipio_value = self.municipioInput.text().strip()
        provincia_value = self.provinciaInput.text().strip()

        # Validar datos
        if not name_value or not municipio_value or not provincia_value:
            QMessageBox.warning(self, "Datos incompletos",
                                "Todos los campos son obligatorios")
            return

        try:
            # Crear objeto clínica
            clinica = Clinica(
                id=0,
                name=name_value,
                municipio=municipio_value,
                provincia=provincia_value
            )

            # Guardar en la base de datos
            result = self.clinicaRepository.postClinica(clinica)

            if result:
                QMessageBox.information(self, "Éxito",
                                        "Clínica creada correctamente")
                if self.parent_window:
                    self.parent_window.load_clinicas()  # Recargar lista en ventana principal
                    self.parent_window.show()
                self.close()
            else:
                QMessageBox.critical(self, "Error",
                                     "No se pudo crear la clínica. Posiblemente ya existe un ID igual.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al crear clínica: {str(e)}")