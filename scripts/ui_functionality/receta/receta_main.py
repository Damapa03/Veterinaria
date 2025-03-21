import os
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QFrame, QMessageBox

from scripts.DAO import Database
from scripts.model.Receta import Receta
from scripts.repositories.AnimalRepository import AnimalRepository
from scripts.repositories.RecetaRepository import RecetaRepository
from scripts.ui_functionality.receta.receta_informacion import RecetaDetailWindow


class RecetasMainWindow(QtWidgets.QMainWindow):
    """Ventana principal para la gestión de recetas médicas"""

    def __init__(self, parent = None):
        super().__init__(parent)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))),
                               'ui/recetas_main.ui')
        try:
            uic.loadUi(ui_path, self)
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al cargar UI: {str(e)}")
            return

        self.parent_window = self.parent()

        # Inicializar repositorio
        self.recetaRepository = RecetaRepository()
        self.animalRepository = AnimalRepository()

        # Configurar título de la ventana
        self.setWindowTitle("Recetas Médicas")

        # Conectar señales de botones
        self.crearButton.clicked.connect(self.on_crear_clicked)
        self.volverButton.clicked.connect(self.on_volver_clicked)
        if hasattr(self, 'buscarButton'):
            self.buscarButton.clicked.connect(self.on_buscar_clicked)

        # Cargar la lista de recetas
        self.load_recetas()

    def load_recetas(self):
        """Cargar y mostrar la lista de recetas desde la base de datos"""
        # Limpiar elementos existentes del layout
        self.clear_rows_layout()

        # Obtener recetas de la base de datos
        recetas_data = self.recetaRepository.getRecetas()

        # Crear objetos receta
        recetas = []
        for rec_data in recetas_data:
            # Orden de columnas: id, treatment, start_date, finalized, pacient
            receta = Receta(
                id=rec_data[0],
                treatment=rec_data[1],
                start_date=rec_data[2],
                finalized=rec_data[3],
                pacient=rec_data[4]
            )
            recetas.append(receta)

        # Crear fila para cada receta
        for receta in recetas:
            self.add_receta_row(receta)

        # Añadir espacio de estiramiento al final para empujar filas hacia arriba
        self.rows.addStretch()

    def clear_rows_layout(self):
        """Eliminar todos los widgets del layout de filas"""
        while self.rows.count():
            item = self.rows.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def add_receta_row(self, receta: Receta):
        """Añadir una fila para una receta en la lista"""
        # Crear marco para la fila
        row_frame = QFrame()
        row_frame.setFrameShape(QFrame.Shape.StyledPanel)
        row_frame.setLineWidth(1)
        row_frame.setMinimumHeight(50)

        # Crear layout horizontal para la fila
        row_layout = QHBoxLayout(row_frame)

        # Determinar estado para mostrar
        estado = "Finalizada" if receta.finalized else "En curso"

        # Crear etiqueta con información de la receta
        self.animalName = self.animalRepository.getAnimalName(receta.pacient)[0]
        info_text = f"Receta #{receta.id} - {receta.treatment} - Paciente: {self.animalName} - Estado: {estado}"
        info_label = QLabel(info_text)
        info_label.setStyleSheet("font-size: 12px;")

        # Crear botón "Más"
        mas_button = QPushButton("Más")
        mas_button.setFixedWidth(60)

        # Conectar botón para mostrar detalles
        mas_button.clicked.connect(lambda checked, r=receta: self.show_receta_details(r))

        # Añadir widgets al layout de fila
        row_layout.addWidget(info_label)
        row_layout.addStretch()
        row_layout.addWidget(mas_button)

        # Añadir fila al layout vertical principal
        self.rows.addWidget(row_frame)

    def show_receta_details(self, receta: Receta):
        """Mostrar la ventana de detalles para una receta específica"""
        self.detail_window = RecetaDetailWindow(self, receta)
        self.detail_window.show()
        self.hide()

    def on_crear_clicked(self):
        """Abrir la ventana para crear una nueva receta"""
        from scripts.ui_functionality.receta.receta_crear import RecetaCreateWindow
        self.create_window = RecetaCreateWindow(self)
        self.create_window.show()
        self.hide()

    def on_buscar_clicked(self):
        """Buscar recetas por paciente o tratamiento"""
        search_term = self.searchInput.text().strip()
        if not search_term:
            self.load_recetas()  # Si el campo está vacío, cargar todas las recetas
            return

        # Limpiar elementos existentes del layout
        self.clear_rows_layout()
        
        # Buscar por paciente
        by_pacient = self.recetaRepository.getRecetasByPacient(search_term)
        # Buscar por tratamiento
        by_treatment = self.recetaRepository.getRecetasByTreatment(search_term)
        
        # Combinar resultados (eliminando duplicados por ID)
        all_results = {}
        
        for rec_data in by_pacient + by_treatment:
            if rec_data[0] not in all_results:
                receta = Receta(
                    id=rec_data[0],
                    treatment=rec_data[1],
                    start_date=rec_data[2],
                    finalized=rec_data[3],
                    pacient=rec_data[4]
                )
                all_results[rec_data[0]] = receta
        
        # Mostrar resultados
        if all_results:
            for receta in all_results.values():
                self.add_receta_row(receta)
        else:
            # Si no hay resultados, mostrar mensaje
            no_results_label = QLabel("No se encontraron recetas que coincidan con la búsqueda.")
            no_results_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            no_results_label.setStyleSheet("font-size: 12px; color: gray;")
            self.rows.addWidget(no_results_label)
            
        # Añadir espacio de estiramiento al final
        self.rows.addStretch()

    def on_volver_clicked(self):
        """Volver a la pantalla anterior"""
        self.close()
        if self.parent_window:
            self.parent_window.show()

