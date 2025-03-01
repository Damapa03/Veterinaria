import sys
from PyQt6 import uic
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QLabel, QScrollArea, 
                             QPushButton, QSpinBox, QFrame, QSizePolicy)
from PyQt6.QtCore import Qt, QSize

from scripts.repositories import CitaRepository as repository
# Importar la clase Cita desde su módulo
from scripts.model.Cita import Cita


class CardWidget(QFrame):
    def __init__(self, cita:Cita, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.Shape.Box)
        self.setFrameShadow(QFrame.Shadow.Raised)
        self.setLineWidth(2)
        self.setStyleSheet("""
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 10px;
            margin: 5px;
            border: 1px solid #dee2e6;
        """)
        
        # Configurar tamaño para todas las tarjetas
        self.setFixedSize(300, 400)
        
        layout = QVBoxLayout()
        layout.setSpacing(5)
        
        # Título con fecha de la cita
        fecha_str = "Sin fecha"
        if hasattr(cita, 'date') and cita.fecha:
            if hasattr(cita.fecha, 'strftime'):  # Es un objeto date o datetime
                fecha_str = cita.fecha.strftime('%d/%m/%Y')
            else:
                fecha_str = str(cita.fecha)
        
        title = QLabel(f"Cita: {fecha_str}")
        title.setStyleSheet("""
            font-weight: bold; 
            font-size: 16px;
            color: #0d6efd;
            background-color: #e7f1ff;
            padding: 5px;
            border-radius: 5px;
        """)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Crear etiquetas para cada dato con iconos o prefijos distintivos
        info_layout = QVBoxLayout()
        info_layout.setSpacing(4)
        
        # Contenedor para información
        info_widget = QWidget()
        info_widget.setStyleSheet("""
            background-color: white;
            border-radius: 5px;
            padding: 5px;
        """)
        
        # Mascota
        animal_str = "Desconocido"
        if hasattr(cita, 'animal') and cita.animal:
            animal_str = cita.animal
        animal_label = QLabel(f"🐾 {animal_str}")
        animal_label.setStyleSheet("font-size: 13px;")
        
        # Profesional
        prof_str = "Sin asignar"
        if hasattr(cita, 'profesional') and cita.profesional:
            prof_str = cita.profesional
        prof_label = QLabel(f"👨‍⚕️ {prof_str}")
        prof_label.setStyleSheet("font-size: 13px;")
        
        # Motivo
        motivo_str: str = "No especificado"
        if hasattr(cita, 'motivo') and cita.motivo:
            motivo_str = cita.motivo
            # if len(motivo_str) > 25:  # Truncar si es muy largo
            #     motivo_str = motivo_str[:22] + "..."
        motivo_label = QLabel(f"📋 {motivo_str}")
        motivo_label.setStyleSheet("font-size: 13px;")
        motivo_label.setWordWrap(True)
        
        # Precio
        precio_str = "$0"
        if hasattr(cita, 'precio') and cita.precio:
            precio_str = f"${cita.precio}"
        precio_label = QLabel(f"💰 {precio_str}")
        precio_label.setStyleSheet("font-size: 13px; font-weight: bold;")
        
        # Añadir etiquetas al layout de información
        info_layout.addWidget(animal_label)
        info_layout.addWidget(prof_label)
        info_layout.addWidget(motivo_label)
        info_layout.addWidget(precio_label)
        
        info_widget.setLayout(info_layout)
        
        # Botón con estilo mejorado
        button = QPushButton("Ver Detalles")
        button.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 6px;
            font-weight: bold;
        """)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.clicked.connect(lambda: self.card_clicked(cita))
        
        # Agregar widgets al layout principal
        layout.addWidget(title)
        layout.addWidget(info_widget)
        layout.addWidget(button)
        
        self.setLayout(layout)
        
    def card_clicked(self, cita:Cita):
        # Mostrar información detallada de la cita
        fecha_str = str(cita.fecha) if hasattr(cita, 'fecha') and cita.fecha else "Sin fecha"
        animal_str = cita.animal if hasattr(cita, 'animal') and cita.animal else "Desconocido"
        prof_str = cita.profesional if hasattr(cita, 'profesional') and cita.profesional else "Sin asignar"
        
        print(f"Cita seleccionada. Fecha: {fecha_str}, Animal: {animal_str}, Profesional: {prof_str}")
        # Aquí podrías abrir una ventana de detalle en el futuro


class ScrollableGridWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/cita.ui", self)
        
        self.setWindowTitle("Citas Veterinarias")

        cita_repo = repository.CitaRepository()
        
        # Obtener datos de la consulta SQL
        self.data_list = cita_repo.getCitas()
        
        # Convertir los resultados SQL a objetos Cita
        self.citas_list = self.convert_to_cita_objects(self.data_list)
        
        # Widget principal
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        
        # Controles
        controls_layout = QHBoxLayout()
        
        # Spinbox para controlar columnas
        columns_label = QLabel("Columnas:")
        self.columns_spinbox = QSpinBox()
        self.columns_spinbox.setRange(1, 10)
        self.columns_spinbox.setValue(4)
        
        # Botón para añadir tarjetas
        add_card_button = QPushButton("Añadir Cita")
        add_card_button.clicked.connect(self.add_card)
        
        # Botón para actualizar
        update_button = QPushButton("Actualizar Grid")
        update_button.clicked.connect(self.update_grid)
        
        # Botón para refrescar datos desde la BD
        refresh_button = QPushButton("Refrescar Datos")
        refresh_button.clicked.connect(self.refresh_data)
        
        # Añadir controles al layout
        controls_layout.addWidget(columns_label)
        controls_layout.addWidget(self.columns_spinbox)
        controls_layout.addWidget(add_card_button)
        controls_layout.addWidget(update_button)
        controls_layout.addWidget(refresh_button)
        controls_layout.addStretch()
        
        # Área scrolleable
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        
        # Habilitar scroll horizontal y vertical
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        
        # Widget de contenido que contendrá el grid
        self.content_widget = QWidget()
        self.grid_layout = QGridLayout(self.content_widget)
        self.grid_layout.setSpacing(10)
        
        # Configurar el widget de contenido como el widget del área scrolleable
        self.scroll_area.setWidget(self.content_widget)
        
        # Añadir los layouts al layout principal
        main_layout.addLayout(controls_layout)
        main_layout.addWidget(self.scroll_area)
        
        # Establecer el widget principal como el widget central
        self.setCentralWidget(main_widget)
        
        # Inicializar el grid con los valores predeterminados
        self.update_grid()
    
    def convert_to_cita_objects(self, data_list):
        """Convierte los resultados SQL a objetos Cita"""
        citas = []
        
        for data in data_list:
            # Si ya es un objeto Cita
            if isinstance(data, Cita):
                citas.append(data)
                continue
                
            # Si es un diccionario (resultado de consulta SQL)
            if isinstance(data, dict):
                # Mapeo de nombres de columnas a atributos de Cita
                fecha = data.get('fecha', None)
                precio = data.get('precio', 0)
                motivo = data.get('motivo', '')
                animal = data.get('animal', data.get('mascota', data.get('nombre_animal', '')))
                profesional = data.get('profesional', data.get('doctor', data.get('veterinario', '')))
                
                cita = Cita(fecha, precio, motivo, animal, profesional)
                citas.append(cita)
                
            # Si es una tupla u otro objeto
            elif hasattr(data, '__getitem__') or hasattr(data, '__dict__'):
                try:
                    # Intentar extraer los atributos necesarios
                    if hasattr(data, '__getitem__'):
                        # Asumimos un orden específico o usamos índices conocidos
                        # Este orden debe ajustarse según la consulta SQL real
                        fecha = data[0] if len(data) > 0 else None
                        precio = data[1] if len(data) > 1 else 0
                        motivo = data[2] if len(data) > 2 else ''
                        animal = data[3] if len(data) > 3 else ''
                        profesional = data[4] if len(data) > 4 else ''
                    else:
                        # Para objetos con atributos
                        fecha = getattr(data, 'fecha', None)
                        precio = getattr(data, 'precio', 0)
                        motivo = getattr(data, 'motivo', '')
                        animal = getattr(data, 'animal', 
                                getattr(data, 'mascota', 
                                getattr(data, 'nombre_animal', '')))
                        profesional = getattr(data, 'profesional', 
                                    getattr(data, 'doctor', 
                                    getattr(data, 'veterinario', '')))
                    
                    cita = Cita(fecha, precio, motivo, animal, profesional)
                    citas.append(cita)
                except Exception as e:
                    print(f"Error al convertir dato a Cita: {e}")
                    # Crear una cita con datos por defecto
                    cita = Cita(None, 0, "Error al cargar", "Desconocido", "Desconocido")
                    citas.append(cita)
            
        return citas
    
    def update_grid(self):
        # Limpiar los elementos existentes en el grid
        while self.grid_layout.count():
            item = self.grid_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        num_columns = self.columns_spinbox.value()
        
        # Verificar si hay datos para mostrar
        if not self.citas_list:
            no_data_label = QLabel("No hay citas disponibles")
            no_data_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            no_data_label.setStyleSheet("font-size: 16px; color: gray;")
            self.grid_layout.addWidget(no_data_label, 0, 0, 1, num_columns)
            return
        
        # Añadir tarjetas al grid
        for i, cita in enumerate(self.citas_list):
            row = i // num_columns
            col = i % num_columns
            card = CardWidget(cita)
            self.grid_layout.addWidget(card, row, col)
        
        # Asegurar que el contenido tenga el tamaño adecuado para permitir scroll horizontal
        min_width = (200 + 20) * num_columns  # ancho de tarjeta + margen
        self.content_widget.setMinimumWidth(min_width)
    
    def add_card(self):
        # Esta función debería abrir un diálogo para añadir una nueva cita
        # Por ahora, solo mostramos un mensaje
        print("Función para añadir nueva cita - Implementar diálogo o navegación a formulario")
    
    def refresh_data(self):
        # Recargar datos desde el repositorio
        cita_repo = repository.CitaRepository()
        self.data_list = cita_repo.getCitas()
        
        # Convertir los resultados a objetos Cita
        self.citas_list = self.convert_to_cita_objects(self.data_list)
        
        # Actualizar el grid con los nuevos datos
        self.update_grid()
    
    # Método para cargar datos desde una fuente externa
    def load_data(self, new_data_list):
        self.data_list = new_data_list
        self.citas_list = self.convert_to_cita_objects(new_data_list)
        self.update_grid()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScrollableGridWindow()
    window.show()
    sys.exit(app.exec())