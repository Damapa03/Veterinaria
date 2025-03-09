import os
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

from scripts.model.Clinica import Clinica
from scripts.repositories.ClinicaRepository import ClinicaRepository


class ClinicaDetailWindow(QtWidgets.QMainWindow):
    """Ventana para mostrar detalles de una clínica"""

    def __init__(self, parent=None, clinica=None):
        super().__init__(parent)
        self.parent_window = parent
        self.clinica = clinica

        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))),
                               'ui/clinicas_information.ui')
        try:
            uic.loadUi(ui_path, self)
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al cargar UI: {str(e)}")
            return

        # Inicializar repositorio
        self.clinicaRepository = ClinicaRepository()

        # Configurar título de la ventana
        self.setWindowTitle(f"Clínica: {clinica.name if clinica else 'Desconocida'}")

        # Cargar datos de la clínica
        self.load_clinica_data()

        # Conectar señales de botones
        self.volverButton.clicked.connect(self.on_volver_clicked)
        self.modificarButton.clicked.connect(self.on_editar_clicked)
        self.borrarButton.clicked.connect(self.on_eliminar_clicked)

    def load_clinica_data(self):
        """Cargar y mostrar los datos de la clínica"""
        if not self.clinica:
            return


        self.nameLabel.setText(self.clinica.name)
        self.municipioLabel.setText(self.clinica.municipio)
        self.provinciaLabel.setText(self.clinica.provincia)

    def on_volver_clicked(self):
        """Volver a la pantalla principal"""
        if self.parent_window:
            self.parent_window.show()
        self.close()

    def on_editar_clicked(self):
        """Abrir la ventana de edición de la clínica"""
        from scripts.ui_functionality.clinica.clinica_editar import ClinicaEditWindow
        self.edit_window = ClinicaEditWindow(self, self.clinica)
        self.edit_window.show()
        self.hide()

    def on_eliminar_clicked(self):
        """Eliminar la clínica actual"""
        confirm = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Está seguro de que desea eliminar la clínica '{self.clinica.name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            try:
                result = self.clinicaRepository.deleteClinica(self.clinica.id)
                if result:
                    QMessageBox.information(
                        self,
                        "Éxito",
                        f"La clínica '{self.clinica.name}' ha sido eliminada correctamente."
                    )
                    if self.parent_window:
                        self.parent_window.load_clinicas()  # Recargar lista en ventana principal
                        self.parent_window.show()
                    self.close()
                else:
                    QMessageBox.warning(
                        self,
                        "Error",
                        "No se pudo eliminar la clínica. Verifique si existen registros dependientes."
                    )
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al eliminar clínica: {str(e)}")

    def closeEvent(self, event):
        """Manejador para el evento de cierre de ventana"""
        if self.parent_window and not self.parent_window.isVisible():
            self.parent_window.show()
        event.accept()