import os
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

from scripts.model.Clinica import Clinica
from scripts.repositories.ClinicaRepository import ClinicaRepository


class ClinicaEditWindow(QtWidgets.QMainWindow):
    """Ventana para editar una clínica existente"""

    def __init__(self, parent=None, clinica=None):
        super().__init__()
        self.parent = parent
        self.clinica = clinica
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))),
                               'ui/clinicas_editar.ui')
        try:
            uic.loadUi(ui_path, self)
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al cargar UI: {str(e)}")
            return

        # Inicializar repositorio
        self.clinicaRepository = ClinicaRepository()

        # Configurar título de la ventana
        self.setWindowTitle(f"Editar {clinica.name}")

        # Cargar datos actuales de la clínica
        self.load_clinica_data()

        # Conectar señales de botones
        self.volverButton.clicked.connect(self.on_volver_clicked)
        self.guardarButton.clicked.connect(self.on_guardar_clicked)

    def load_clinica_data(self):
        """Cargar los datos actuales de la clínica en el formulario"""
        self.idDisplay.setText(str(self.clinica.id))
        self.nameInput.setText(self.clinica.name)
        self.municipioInput.setText(self.clinica.municipio)
        self.provinciaInput.setText(self.clinica.provincia)

    def on_volver_clicked(self):
        """Volver a la pantalla de detalles"""
        self.parent.show()
        self.close()

    def on_guardar_clicked(self):
        """Guardar los cambios realizados a la clínica"""
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
            # Actualizar objeto clínica con nuevos valores
            updated_clinica = Clinica(
                id=self.clinica.id,
                name=name_value,
                municipio=municipio_value,
                provincia=provincia_value
            )

            # Guardar cambios en la base de datos
            result = self.clinicaRepository.putClinica(updated_clinica.id,updated_clinica)

            if result:
                QMessageBox.information(self, "Éxito",
                                        "Clínica actualizada correctamente")

                # Actualizar clínica en la ventana padre
                self.parent.clinica = updated_clinica
                self.parent.display_clinica_info()

                # Recargar lista en ventana principal
                self.parent.parent.load_clinicas()

                # Volver a la pantalla de detalles
                self.parent.show()
                self.close()
            else:
                QMessageBox.critical(self, "Error",
                                     "No se pudo actualizar la clínica")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al actualizar clínica: {str(e)}")