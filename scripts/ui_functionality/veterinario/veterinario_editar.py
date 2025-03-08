import os
import sqlite3
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
import re

from scripts.model.Veterinario import Veterinario
from scripts.repositories.VeterinarioRepository import VeterinarioRepository
from scripts.repositories.ClinicaRepository import ClinicaRepository


class VeterinarioEditWindow(QtWidgets.QMainWindow):
    """Ventana para editar un veterinario existente en el sistema"""
    def __init__(self, parent=None, veterinario=None):
        super().__init__(parent)
        # Cargar archivo UI
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))),
                               'ui/veterinarios_editar.ui')
        try:
            uic.loadUi(ui_path, self)
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al cargar UI: {str(e)}")
            return



        # Guardar referencia a la ventana padre y objeto veterinario
        self.parent_window = parent
        self.veterinario = veterinario

        # Inicializar repositorios
        self.veterinarioRepository = VeterinarioRepository()
        self.clinicaRepository = ClinicaRepository()

        # Configurar título de la ventana
        self.setWindowTitle(f"Modificar Veterinario - {veterinario.name}")

        # Conectar señales de botones
        self.volverButton.clicked.connect(self.on_volver_clicked)
        self.guardarButton.clicked.connect(self.on_guardar_clicked)

        # Cargar clínicas en el combobox
        self.load_clinicas()

        # Rellenar formulario con datos del veterinario
        self.populate_form()

    def load_clinicas(self):
        """Cargar las clínicas en el combo box"""
        try:
            # Después añadir todas las clínicas de la base de datos
            clinicas = self.clinicaRepository.getClinicasNameAndId()
            for clinica in clinicas:
                # clinica[0] es id, clinica[1] es nombre
                self.clinicaComboBox.addItem(clinica[1], clinica[0])
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudieron cargar las clínicas: {str(e)}")

    def populate_form(self):
        """Rellenar el formulario con los datos actuales del veterinario"""
        # Mostrar DNI (no editable)
        self.dniDisplay.setText(self.veterinario.dni)

        # Rellenar otros campos
        self.nameInput.setText(self.veterinario.name)
        self.surnameInput.setText(self.veterinario.surname)
        self.emailInput.setText(self.veterinario.email)
        self.telephoneInput.setText(self.veterinario.telephone)

        # Campo de contraseña se deja en blanco (solo se actualizará si el usuario introduce algo)

        # Seleccionar clínica actual en el combobox
        if self.veterinario.location:
            for i in range(self.clinicaComboBox.count()):
                if self.clinicaComboBox.itemData(i) == self.veterinario.location:
                    self.clinicaComboBox.setCurrentIndex(i)
                    break
        else:
            # Establecer opción "Sin asignar"
            self.clinicaComboBox.setCurrentIndex(0)

    def on_volver_clicked(self):
        """Volver a la pantalla anterior"""
        self.close()
        if self.parent_window:
            self.parent_window.show()

    def on_guardar_clicked(self):
        """Procesar el formulario y actualizar el veterinario"""
        # Validar datos del formulario
        if not self.validate_form():
            return

        # Obtener valores del formulario
        name = self.nameInput.text().strip()
        surname = self.surnameInput.text().strip()
        email = self.emailInput.text().strip()
        telephone = self.telephoneInput.text().strip()
        password = self.passwordInput.text()

        # Si la contraseña está vacía, usar la contraseña existente
        if not password:
            password = self.veterinario.password

        # Obtener ID de clínica seleccionada (puede ser None)
        clinica_id = self.clinicaComboBox.currentData()

        # Crear objeto veterinario actualizado
        updated_veterinario = Veterinario(
            dni=self.veterinario.dni,  # El DNI no cambia
            name=name,
            surname=surname,
            email=email,
            telephone=telephone,
            password=password,
            location=clinica_id
        )

        # Intentar actualizar en la base de datos
        try:
            result = self.veterinarioRepository.putVeterinario(
                self.veterinario.dni, updated_veterinario
            )

            if result == sqlite3.IntegrityError:
                QMessageBox.warning(
                    self,
                    "Error",
                    "No se pudo actualizar el veterinario debido a un conflicto de datos."
                )
                return

            # Mostrar mensaje de éxito
            QMessageBox.information(
                self,
                "Veterinario Actualizado",
                f"Los datos del veterinario {name} {surname} han sido actualizados correctamente."
            )

            # Actualizar el objeto veterinario almacenado (para ventanas padre)
            self.veterinario = updated_veterinario

            # Volver a la ventana padre y actualizar si es necesario
            if self.parent_window:
                # Si el padre es la ventana de detalles, actualizar su visualización
                if hasattr(self.parent_window, 'display_veterinario_details'):
                    self.parent_window.veterinario = updated_veterinario
                    self.parent_window.display_veterinario_details()

                # Si el padre es la ventana principal, actualizar la lista
                if hasattr(self.parent_window, 'load_veterinarios'):
                    self.parent_window.load_veterinarios()

                self.parent_window.show()
            self.close()

        except Exception as e:
            # Mostrar mensaje de error
            QMessageBox.critical(
                self,
                "Error",
                f"No se pudo actualizar el veterinario: {str(e)}"
            )

    def validate_form(self):
        """Validar los datos del formulario"""
        # Comprobar campos vacíos
        if not self.nameInput.text().strip():
            QMessageBox.warning(self, "Validación", "El nombre es obligatorio.")
            self.nameInput.setFocus()
            return False

        if not self.surnameInput.text().strip():
            QMessageBox.warning(self, "Validación", "Los apellidos son obligatorios.")
            self.surnameInput.setFocus()
            return False

        if not self.emailInput.text().strip():
            QMessageBox.warning(self, "Validación", "El email es obligatorio.")
            self.emailInput.setFocus()
            return False

        if not self.telephoneInput.text().strip():
            QMessageBox.warning(self, "Validación", "El teléfono es obligatorio.")
            self.telephoneInput.setFocus()
            return False

        # Validar formato email
        email = self.emailInput.text().strip()
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            QMessageBox.warning(self, "Validación", "El formato del email no es válido.")
            self.emailInput.setFocus()
            return False

        # Validar formato teléfono (formato español: 9 dígitos)
        telephone = self.telephoneInput.text().strip()
        if not re.match(r'^\d{9}$', telephone):
            QMessageBox.warning(self, "Validación", "El teléfono debe tener 9 dígitos.")
            self.telephoneInput.setFocus()
            return False

        # Si la contraseña no está vacía, validar longitud
        password = self.passwordInput.text()
        if password and len(password) < 6:
            QMessageBox.warning(self, "Validación", "La contraseña debe tener al menos 6 caracteres.")
            self.passwordInput.setFocus()
            return False

        return True