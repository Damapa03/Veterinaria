import os
import re
import sqlite3

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

from scripts.model.Veterinario import Veterinario
from scripts.repositories.ClinicaRepository import ClinicaRepository
from scripts.repositories.VeterinarioRepository import VeterinarioRepository


class VeterinarioCreateWindow(QtWidgets.QMainWindow):
    """Ventana para crear un nuevo veterinario en el sistema"""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Cargar archivo UI
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, '../../../ui/veterinarios_crear.ui')
        uic.loadUi(ui_path, self)

        # Guardar referencia a la ventana padre
        self.parent_window = parent

        # Inicializar repositorios
        self.veterinarioRepository = VeterinarioRepository()
        self.clinicaRepository = ClinicaRepository()

        # Configurar título de la ventana
        self.setWindowTitle("Crear Nuevo Veterinario")

        # Conectar señales de botones
        self.volverButton.clicked.connect(self.on_volver_clicked)
        self.aceptarButton.clicked.connect(self.on_aceptar_clicked)

        # Cargar clínicas en el combobox
        self.load_clinicas()

    def load_clinicas(self):
        """Cargar las clínicas en el combo box"""
        try:
            self.clinicaComboBox.clear()

            # Primero añadir opción "Sin asignar"
            self.clinicaComboBox.addItem("Sin asignar", None)

            # Después añadir todas las clínicas de la base de datos
            clinicas = self.clinicaRepository.getClinicasNameAndId()
            for clinica in clinicas:
                # clinica[0] es id, clinica[1] es nombre
                self.clinicaComboBox.addItem(clinica[1], clinica[0])
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudieron cargar las clínicas: {str(e)}")

    def on_volver_clicked(self):
        """Volver a la pantalla principal de veterinarios"""
        self.close()
        if self.parent_window:
            self.parent_window.show()

    def on_aceptar_clicked(self):
        """Procesar el formulario y crear un nuevo veterinario"""
        # Validar datos del formulario
        if not self.validate_form():
            return

        # Obtener valores del formulario
        dni = self.dniInput.text().strip()
        name = self.nameInput.text().strip()
        surname = self.surnameInput.text().strip()
        email = self.emailInput.text().strip()
        telephone = self.telephoneInput.text().strip()
        password = self.passwordInput.text()

        # Obtener ID de clínica seleccionada (puede ser None)
        clinica_id = self.clinicaComboBox.currentData()

        # Crear objeto veterinario
        new_veterinario = Veterinario(
            dni=dni,
            name=name,
            surname=surname,
            email=email,
            telephone=telephone,
            password=password,
            location=clinica_id
        )

        # Intentar guardar en la base de datos
        try:
            result = self.veterinarioRepository.postVeterinario(new_veterinario)

            if result == sqlite3.IntegrityError:
                QMessageBox.warning(
                    self,
                    "Error",
                    f"Ya existe un veterinario con el DNI {dni}."
                )
                return

            # Mostrar mensaje de éxito
            QMessageBox.information(
                self,
                "Veterinario Creado",
                f"El veterinario {name} {surname} ha sido creado correctamente."
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
                f"No se pudo crear el veterinario: {str(e)}"
            )

    def validate_form(self):
        """Validar los datos del formulario"""
        # Comprobar campos vacíos
        if not self.dniInput.text().strip():
            QMessageBox.warning(self, "Validación", "El DNI es obligatorio.")
            self.dniInput.setFocus()
            return False

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

        if not self.passwordInput.text():
            QMessageBox.warning(self, "Validación", "La contraseña es obligatoria.")
            self.passwordInput.setFocus()
            return False

        # Validar formato DNI (DNI español: 8 dígitos seguidos de una letra)
        dni = self.dniInput.text().strip()
        if not re.match(r'^\d{8}[A-Za-z]$', dni):
            QMessageBox.warning(self, "Validación", "El DNI debe tener 8 dígitos seguidos de una letra.")
            self.dniInput.setFocus()
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

        # Validar longitud de contraseña
        if len(self.passwordInput.text()) < 6:
            QMessageBox.warning(self, "Validación", "La contraseña debe tener al menos 6 caracteres.")
            self.passwordInput.setFocus()
            return False

        return True