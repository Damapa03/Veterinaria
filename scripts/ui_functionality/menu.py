import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6 import uic

from scripts.ui_functionality.receta.receta_main import RecetasMainWindow
from scripts.ui_functionality.Cita.Citasui import CitaMainWindow
from scripts.ui_functionality.animal.animal_main import AnimalsMainWindow
from scripts.ui_functionality.clinica.clinica_main import ClinicasMainWindow
from scripts.ui_functionality.clientes.main import ClientesMainWindow
from scripts.ui_functionality.veterinario.veterinario_main import VeterinariosMainWindow


class MenuMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        script_dir = os.path.dirname(os.path.abspath(__file__))

        project_root = os.path.dirname(os.path.dirname(script_dir))
        ui_path = os.path.join(project_root, 'ui', 'menu.ui')

        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found at path: {ui_path}")

        uic.loadUi(ui_path, self)

        self.setWindowTitle("Veterinaria D3P")

        # Initialize window references to None
        self.veterinarios_window = None
        self.animales_window = None
        self.clinicas_window = None
        self.recetas_window = None
        self.citas_window = None
        self.clientes_window = None

        # Connect buttons to navigation functions
        self.veterinariosNavigate.clicked.connect(self.show_veterinarios)
        self.animalesNavigate.clicked.connect(self.show_animales)
        self.clientesNavigate.clicked.connect(self.show_clientes)
        self.clinicasNavigate.clicked.connect(self.show_clinicas)
        self.recetasNavigate.clicked.connect(self.show_recetas)
        self.citasNavigate.clicked.connect(self.show_citas)

    # Navigation functions with lazy initialization
    def show_veterinarios(self):
        print("Navigating to Veterinarios screen")
        if self.veterinarios_window is None:
            self.veterinarios_window = VeterinariosMainWindow(self)
        self.hide()
        self.veterinarios_window.show()

    def show_animales(self):
        print("Navigating to Animales screen")
        if self.animales_window is None:
            self.animales_window = AnimalsMainWindow(self)
        self.hide()
        self.animales_window.show()

    def show_clientes(self):
        print("Navigating to Clientes screen")
        if self.clientes_window is None:
            self.clientes_window = ClientesMainWindow(self)
        self.hide()
        self.clientes_window.show()

    def show_clinicas(self):
        print("Navigating to Clinicas screen")
        if self.clinicas_window is None:
            self.clinicas_window = ClinicasMainWindow(self)
        self.hide()
        self.clinicas_window.show()

    def show_recetas(self):
        print("Navigating to Recetas screen")
        if self.recetas_window is None:
            self.recetas_window = RecetasMainWindow(self)
        self.hide()
        self.recetas_window.show()

    def show_citas(self):
        print("Navigating to Citas screen")
        if self.citas_window is None:
            self.citas_window = CitaMainWindow(self)
        self.hide()
        self.citas_window.show()

    def closeEvent(self, event):
        """Handle application closure properly"""
        # Clean up all child windows
        windows = [
            self.veterinarios_window,
            self.animales_window,
            self.clinicas_window,
            self.recetas_window,
            self.citas_window,
            self.clientes_window
        ]

        for window in windows:
            if window is not None:
                window.close()

        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuMainWindow()
    window.show()
    sys.exit(app.exec())