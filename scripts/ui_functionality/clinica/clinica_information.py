import os
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

from scripts.model.Clinica import Clinica
from scripts.repositories.ClinicaRepository import ClinicaRepository
from scripts.ui_functionality.clinica.clinica_editar import ClinicaEditWindow


class ClinicaDetailWindow(QtWidgets.QMainWindow):
    """Ventana para mostrar detalles de una clínica"""

    def __init__(self, parent=None, clinica=None):
        super().__init__()
        self.parent = parent
        self.clinica = clinica
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, '../../../ui/clinicas_information.ui')
        uic.loadUi(ui_path, self)

        # Inicializar repositorio
        self.clinicaRepository = ClinicaRepository()

        # Configurar título de la ventana
        self.setWindowTitle(f"Detalles de {clinica.name}")

        # Mostrar información de la clínica
        self.display_clinica_info()

        # Conectar señales de botones
        self.volverButton.clicked.connect(self.on_volver_clicked)
        self.modificarButton.clicked.connect(self.on_modificar_clicked)
        self.borrarButton.clicked.connect(self.on_borrar_clicked)

    def display_clinica_info(self):
        """Mostrar la información de la clínica en la interfaz"""
        self.name.setText(self.clinica.name)
        self.id.setText(f"ID: {self.clinica.id}")
        self.municipio.setText(f"Municipio: {self.clinica.municipio}")
        self.provincia.setText(f"Provincia: {self.clinica.provincia}")

    def on_volver_clicked(self):
        """Volver a la pantalla principal"""
        self.parent.show()
        self.close()

    def on_modificar_clicked(self):
        """Abrir ventana para modificar la clínica"""
        self.edit_window = ClinicaEditWindow(self, self.clinica)
        self.edit_window.show()
        self.hide()

    def on_borrar_clicked(self):
        """Eliminar la clínica actual previa confirmación"""
        reply = QMessageBox.question(self, 'Confirmar eliminación',
                                     f'¿Está seguro de que desea eliminar la clínica {self.clinica.name}?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            try:
                # Intentar eliminar la clínica
                result = self.clinicaRepository.deleteClinica(self.clinica.id)

                if result:
                    QMessageBox.information(self, "Éxito",
                                            "Clínica eliminada correctamente")
                    self.parent.load_clinicas()  # Recargar lista en ventana principal
                    self.parent.show()
                    self.close()
                else:
                    QMessageBox.critical(self, "Error",
                                         "No se pudo eliminar la clínica. Puede que esté siendo utilizada por veterinarios.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al eliminar clínica: {str(e)}")