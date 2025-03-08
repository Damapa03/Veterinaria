import os
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QFrame, QVBoxLayout, QMessageBox
from typing import List, Optional

from scripts.DAO import Database
from scripts.model.Clinica import Clinica
from scripts.repositories.ClinicaRepository import ClinicaRepository
from scripts.ui_functionality.clinica.clinica_information import ClinicaDetailWindow


class ClinicasMainWindow(QtWidgets.QMainWindow):
    """Ventana principal para la gestión de clínicas"""

    def __init__(self, parent = None):
        super().__init__(parent)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))),
                               'ui/clinicas_main.ui')
        try:
            uic.loadUi(ui_path, self)
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al cargar UI: {str(e)}")
            return

        self.parent_window = self.parent()

        # Inicializar repositorio
        self.clinicaRepository = ClinicaRepository()

        # Configurar título de la ventana
        self.setWindowTitle("Clínicas")

        # Conectar señales de botones
        self.crearButton.clicked.connect(self.on_crear_clicked)
        self.volverButton.clicked.connect(self.on_volver_clicked)

        # Cargar la lista de clínicas
        self.load_clinicas()

    def load_clinicas(self):
        """Cargar y mostrar la lista de clínicas desde la base de datos"""
        # Limpiar elementos existentes del layout
        self.clear_rows_layout()

        # Obtener clínicas de la base de datos
        clinicas_data = self.clinicaRepository.getClinicas()

        # Crear objetos clínica
        clinicas = []
        for clin_data in clinicas_data:
            # Orden de columnas: id, Municipio, Provincia, name
            clinica = Clinica(
                id=clin_data[0],
                municipio=clin_data[1],
                provincia=clin_data[2],
                name=clin_data[3]
            )
            clinicas.append(clinica)

        # Crear fila para cada clínica
        for clinica in clinicas:
            self.add_clinica_row(clinica)

        # Añadir espacio de estiramiento al final para empujar filas hacia arriba
        self.rows.addStretch()

    def clear_rows_layout(self):
        """Eliminar todos los widgets del layout de filas"""
        while self.rows.count():
            item = self.rows.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def add_clinica_row(self, clinica: Clinica):
        """Añadir una fila para una clínica en la lista"""
        # Crear marco para la fila
        row_frame = QFrame()
        row_frame.setFrameShape(QFrame.Shape.StyledPanel)
        row_frame.setLineWidth(1)
        row_frame.setMinimumHeight(50)

        # Crear layout horizontal para la fila
        row_layout = QHBoxLayout(row_frame)

        # Crear etiqueta con información de la clínica
        info_text = f"{clinica.name} ({clinica.municipio}, {clinica.provincia})"
        info_label = QLabel(info_text)
        info_label.setStyleSheet("font-size: 12px;")

        # Crear botón "Más"
        mas_button = QPushButton("Más")
        mas_button.setFixedWidth(60)

        # Conectar botón para mostrar detalles
        mas_button.clicked.connect(lambda checked, c=clinica: self.show_clinica_details(c))

        # Añadir widgets al layout de fila
        row_layout.addWidget(info_label)
        row_layout.addStretch()
        row_layout.addWidget(mas_button)

        # Añadir fila al layout vertical principal
        self.rows.addWidget(row_frame)

    def show_clinica_details(self, clinica: Clinica):
        """Mostrar la ventana de detalles para una clínica específica"""
        self.detail_window = ClinicaDetailWindow(self, clinica)
        self.detail_window.show()
        self.hide()

    def on_crear_clicked(self):
        """Abrir la ventana para crear una nueva clínica"""
        from scripts.ui_functionality.clinica.clinica_crear import ClinicaCreateWindow
        self.create_window = ClinicaCreateWindow(self)
        self.create_window.show()
        self.hide()

    def on_volver_clicked(self):
        """Volver a la pantalla anterior"""
        self.close()
        if self.parent_window:
            self.parent_window.show()