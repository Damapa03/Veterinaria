import os

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

from scripts.repositories.ClinicaRepository import ClinicaRepository
from scripts.repositories.VeterinarioRepository import VeterinarioRepository


class VeterinarioDetailWindow(QtWidgets.QMainWindow):
    """Ventana para mostrar los detalles de un veterinario"""
    def __init__(self, parent=None, veterinario=None):
        super().__init__(parent)
        # Cargar archivo UI
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, '../../../ui/veterinarios_information.ui')
        uic.loadUi(ui_path, self)

        # Guardar referencia a la ventana padre
        self.parent_window = parent

        # Guardar objeto veterinario
        self.veterinario = veterinario

        # Inicializar repositorios
        self.veterinarioRepository = VeterinarioRepository()
        self.clinicaRepository = ClinicaRepository()

        # Configurar título de la ventana
        self.setWindowTitle(f"Detalles del Veterinario - {veterinario.name}")

        # Conectar señales de botones
        self.volverButton.clicked.connect(self.on_volver_clicked)
        self.modificarButton.clicked.connect(self.on_modificar_clicked)
        self.borrarButton.clicked.connect(self.on_borrar_clicked)

        # Mostrar información del veterinario
        self.display_veterinario_details()

    def display_veterinario_details(self):
        """Mostrar los detalles del veterinario en la interfaz"""
        # Nombre y apellidos
        self.nameAndSurname.setText(f"{self.veterinario.name} {self.veterinario.surname}")

        # DNI
        self.dni.setText(f"DNI: {self.veterinario.dni}")

        # Información de la clínica
        if self.veterinario.location:
            try:
                clinica_repo = ClinicaRepository()
                clinica_data = clinica_repo.getClinicaName(int(self.veterinario.location))
                clinica_name = clinica_data[0] if clinica_data else "Clínica no encontrada"
                self.clinica.setText(f"Asignado en: {clinica_name}")
            except Exception as e:
                self.clinica.setText(f"Asignado en clínica ID: {self.veterinario.location}")
        else:
            self.clinica.setText("No asignado a ninguna clínica")

        # Email
        self.email.setText(f"Email: {self.veterinario.email}")

        # Teléfono
        self.label_5.setText(f"Teléfono: {self.veterinario.telephone}")

    def on_volver_clicked(self):
        """Volver a la pantalla principal de veterinarios"""
        self.close()
        if self.parent_window:
            self.parent_window.show()

    def on_modificar_clicked(self):
        """Abrir la pantalla de edición para este veterinario"""
        from veterinario_editar import VeterinarioEditWindow
        self.edit_window = VeterinarioEditWindow(self, self.veterinario)
        self.edit_window.show()
        self.hide()  # Ocultar la ventana de detalles mientras se edita

    def on_borrar_clicked(self):
        """Eliminar el veterinario después de confirmación"""
        # Diálogo de confirmación
        confirm = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Está seguro que desea eliminar al veterinario {self.veterinario.name} {self.veterinario.surname}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            try:
                # Eliminar de la base de datos
                self.veterinarioRepository.deleteVeterinario(self.veterinario.dni)

                # Mostrar mensaje de éxito
                QMessageBox.information(
                    self,
                    "Veterinario eliminado",
                    f"El veterinario {self.veterinario.name} {self.veterinario.surname} ha sido eliminado correctamente."
                )

                # Volver a la pantalla principal y actualizar
                if self.parent_window:
                    self.parent_window.load_veterinarios()
                    self.parent_window.show()
                self.close()

            except Exception as e:
                # Mostrar mensaje de error
                QMessageBox.critical(
                    self,
                    "Error",
                    f"No se pudo eliminar al veterinario: {str(e)}"
                )