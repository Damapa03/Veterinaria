import os
import sys

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QFrame

from scripts.DAO import Database
from scripts.model.Veterinario import Veterinario
from scripts.repositories.VeterinarioRepository import VeterinarioRepository
from scripts.ui_functionality.veterinario.veterinario_information import VeterinarioDetailWindow


class VeterinariosMainWindow(QtWidgets.QMainWindow):
    """Ventana principal para la gestión de veterinarios"""

    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, '../../../ui/veterinarios_main.ui')
        uic.loadUi(ui_path, self)

        # Inicializar repositorio
        self.veterinarioRepository = VeterinarioRepository()

        # Configurar título de la ventana
        self.setWindowTitle("Veterinarios")

        # Conectar señales de botones
        self.crearButton.clicked.connect(self.on_crear_clicked)
        self.volverButton.clicked.connect(self.on_volver_clicked)

        # Cargar la lista de veterinarios
        self.load_veterinarios()

    def load_veterinarios(self):
        """Cargar y mostrar la lista de veterinarios desde la base de datos"""
        # Limpiar elementos existentes del layout
        self.clear_rows_layout()

        # Obtener veterinarios de la base de datos
        veterinarios_data = self.veterinarioRepository.getVeterinarios()

        # Crear objetos veterinario
        veterinarios = []
        for vet_data in veterinarios_data:
            # Orden de columnas: DNI, name, surname, email, telephone, password, location
            veterinario = Veterinario(
                dni=vet_data[0],
                name=vet_data[1],
                surname=vet_data[2],
                email=vet_data[3],
                telephone=vet_data[4],
                password=vet_data[5],
                location=vet_data[6] if len(vet_data) > 6 else None
            )
            veterinarios.append(veterinario)

        # Crear fila para cada veterinario
        for veterinario in veterinarios:
            self.add_veterinario_row(veterinario)

        # Añadir espacio de estiramiento al final para empujar filas hacia arriba
        self.rows.addStretch()

    def clear_rows_layout(self):
        """Eliminar todos los widgets del layout de filas"""
        while self.rows.count():
            item = self.rows.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def add_veterinario_row(self, veterinario: Veterinario):
        """Añadir una fila para un veterinario en la lista"""
        # Crear marco para la fila
        row_frame = QFrame()
        row_frame.setFrameShape(QFrame.Shape.StyledPanel)
        row_frame.setLineWidth(1)
        row_frame.setMinimumHeight(50)

        # Crear layout horizontal para la fila
        row_layout = QHBoxLayout(row_frame)

        # Crear etiqueta con información del veterinario
        info_text = f"{veterinario.name} {veterinario.surname} (DNI: {veterinario.dni})"
        info_label = QLabel(info_text)
        info_label.setStyleSheet("font-size: 12px;")

        # Crear botón "Más"
        mas_button = QPushButton("Más")
        mas_button.setFixedWidth(60)

        # Conectar botón para mostrar detalles
        mas_button.clicked.connect(lambda checked, v=veterinario: self.show_veterinario_details(v))

        # Añadir widgets al layout de fila
        row_layout.addWidget(info_label)
        row_layout.addStretch()
        row_layout.addWidget(mas_button)

        # Añadir fila al layout vertical principal
        self.rows.addWidget(row_frame)

    def show_veterinario_details(self, veterinario: Veterinario):
        """Mostrar la ventana de detalles para un veterinario específico"""
        self.detail_window = VeterinarioDetailWindow(self, veterinario)
        self.detail_window.show()
        self.hide()

    def on_crear_clicked(self):
        """Abrir la ventana para crear un nuevo veterinario"""
        from veterinario_create import VeterinarioCreateWindow
        self.create_window = VeterinarioCreateWindow(self)
        self.create_window.show()
        self.hide()

    def on_volver_clicked(self):
        """Volver a la pantalla anterior"""
        self.close()


def main():
    """Función principal para iniciar la aplicación"""
    app = QtWidgets.QApplication(sys.argv)

    # Crear conexión a la base de datos
    db = Database()

    # Crear y mostrar ventana principal
    window = VeterinariosMainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()