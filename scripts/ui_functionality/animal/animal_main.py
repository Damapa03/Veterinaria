import os
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QFrame

from scripts.DAO import Database
from scripts.model.Animal import Animal
from scripts.repositories.AnimalRepository import AnimalRepository
from scripts.repositories.ClienteRepository import ClienteRepository
from scripts.ui_functionality.animal.animal_informacion import AnimalDetailWindow


class AnimalsMainWindow(QtWidgets.QMainWindow):
    """Ventana principal para la gestión de animales"""

    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, '../../../ui/animal_main.ui')
        uic.loadUi(ui_path, self)

        # Inicializar repositorio
        self.animalRepository = AnimalRepository()
        self.clienteRepository = ClienteRepository()

        # Configurar título de la ventana
        self.setWindowTitle("Animales")

        # Conectar señales de botones
        self.crearButton.clicked.connect(self.on_crear_clicked)
        self.volverButton.clicked.connect(self.on_volver_clicked)
        self.searchButton.clicked.connect(self.on_buscar_clicked)
        self.clearFiltersButton.clicked.connect(self.on_clear_filters)

        # Cargar la lista de animales
        self.load_animals()

    def load_animals(self):
        """Cargar y mostrar la lista de animales desde la base de datos"""
        # Limpiar elementos existentes del layout
        self.clear_rows_layout()

        # Obtener animales de la base de datos
        animals_data = self.animalRepository.getAnimals()

        # Crear objetos animal
        animals = []
        for anim_data in animals_data:
            # Orden de columnas: id, name, species, description, owner
            animal = Animal(
                id=anim_data[0],
                name=anim_data[1],
                species=anim_data[2],
                description=anim_data[3],
                owner=anim_data[4]
            )
            animals.append(animal)

        # Crear fila para cada animal
        for animal in animals:
            self.add_animal_row(animal)

        # Añadir espacio de estiramiento al final para empujar filas hacia arriba
        self.rows.addStretch()

    def clear_rows_layout(self):
        """Eliminar todos los widgets del layout de filas"""
        while self.rows.count():
            item = self.rows.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def add_animal_row(self, animal: Animal):
        """Añadir una fila para un animal en la lista"""
        # Crear marco para la fila
        row_frame = QFrame()
        row_frame.setFrameShape(QFrame.Shape.StyledPanel)
        row_frame.setLineWidth(1)
        row_frame.setMinimumHeight(50)

        # Crear layout horizontal para la fila
        row_layout = QHBoxLayout(row_frame)

        # Crear etiqueta con información del animal
        ownerName = self.clienteRepository.getClienteName(animal.owner)["name"]
        info_text = f"{animal.name} - {animal.species} - Dueño: {ownerName}"
        info_label = QLabel(info_text)
        info_label.setStyleSheet("font-size: 12px;")

        # Crear botón "Más"
        mas_button = QPushButton("Más")
        mas_button.setFixedWidth(60)

        # Conectar botón para mostrar detalles
        mas_button.clicked.connect(lambda checked, a=animal: self.show_animal_details(a))

        # Añadir widgets al layout de fila
        row_layout.addWidget(info_label)
        row_layout.addStretch()
        row_layout.addWidget(mas_button)

        # Añadir fila al layout vertical principal
        self.rows.addWidget(row_frame)

    def show_animal_details(self, animal: Animal):
        """Mostrar la ventana de detalles para un animal específico"""
        self.detail_window = AnimalDetailWindow(self, animal)
        self.detail_window.show()
        self.hide()

    def on_crear_clicked(self):
        """Abrir la ventana para crear un nuevo animal"""
        from scripts.ui_functionality.animal.animal_crear import AnimalCreateWindow
        self.create_window = AnimalCreateWindow(self)
        self.create_window.show()
        self.hide()

    def on_buscar_clicked(self):
        """Buscar animales por propietario, especie y nombre"""
        search_name = self.nameFilterInput.text().strip()
        search_species = self.speciesFilterInput.text().strip()
        search_owner = self.ownerFilterInput.text().strip()

        # Limpiar elementos existentes del layout
        self.clear_rows_layout()

        # Obtener animales filtrados de la base de datos
        animals_data = self.animalRepository.getAnimalsFilter(search_name, search_species, search_owner)

        # Crear objetos animal
        animals = []
        for anim_data in animals_data:
            # Los datos vienen en el mismo orden que en la consulta simple
            animal = Animal(
                id=anim_data[0],
                name=anim_data[1],
                species=anim_data[2],
                description=anim_data[3],
                owner=anim_data[4]
            )
            animals.append(animal)

        # Crear fila para cada animal
        for animal in animals:
            self.add_animal_row(animal)

        # Mostrar mensaje si no hay resultados
        if not animals:
            no_results_label = QLabel("No se encontraron animales con los criterios especificados")
            no_results_label.setStyleSheet("padding: 20px;")
            self.rows.addWidget(no_results_label)

        # Añadir espacio de estiramiento al final para empujar filas hacia arriba
        self.rows.addStretch()

    def on_clear_filters(self):
        self.nameFilterInput.setText("")
        self.ownerFilterInput.setText("")
        self.speciesFilterInput.setText("")

    def on_volver_clicked(self):
        """Volver a la pantalla anterior"""
        self.close()


def main():
    """Función principal para iniciar la aplicación"""
    app = QtWidgets.QApplication(sys.argv)

    # Crear conexión a la base de datos
    db = Database()

    # Crear y mostrar ventana principal
    window = AnimalsMainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()