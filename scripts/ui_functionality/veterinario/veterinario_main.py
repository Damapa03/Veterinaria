import os
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QFrame, QVBoxLayout, QMessageBox
from typing import List, Optional

from scripts.DAO import Database
from scripts.model.Veterinario import Veterinario
from scripts.repositories.VeterinarioRepository import VeterinarioRepository

# Main window class
class VeterinariosMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir,'../../../ui/veterinarios_main.ui')
        uic.loadUi(ui_path, self)

        # Store database connection
        self.veterinarioRepository = VeterinarioRepository()
        
        # Set window title
        self.setWindowTitle("Veterinarios")

        # Connect button signals
        self.crearButton.clicked.connect(self.on_crear_clicked)
        self.volverButton.clicked.connect(self.on_volver_clicked)
        
        # Populate the veterinarians list
        self.load_veterinarios()

    def load_veterinarios(self):
        # Clear existing items from the layout
        self.clear_rows_layout()
        
        # Get veterinarians from database
        veterinarios_data = self.veterinarioRepository.getVeterinarios()
        
        # Create veterinario objects
        veterinarios = []
        for vet_data in veterinarios_data:
            # Assuming column order: DNI, name, surname, email, telephone, password, location
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
        
        # Create row for each veterinarian
        for veterinario in veterinarios:
            self.add_veterinario_row(veterinario)
        
        # Add stretching space at the bottom to push rows to the top
        self.rows.addStretch()
    
    def clear_rows_layout(self):
        # Remove all widgets from the layout
        while self.rows.count():
            item = self.rows.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
    
    def add_veterinario_row(self, veterinario: Veterinario):
        # Create frame for the row
        row_frame = QFrame()
        row_frame.setFrameShape(QFrame.Shape.StyledPanel)
        row_frame.setLineWidth(1)
        row_frame.setMinimumHeight(50)
        
        # Create horizontal layout for the row
        row_layout = QHBoxLayout(row_frame)
        
        # Create label with veterinarian info
        info_text = f"{veterinario.name} {veterinario.surname} (DNI: {veterinario.dni})"
        info_label = QLabel(info_text)
        info_label.setStyleSheet("font-size: 12px;")
        
        # Create "Más" button
        mas_button = QPushButton("Más")
        mas_button.setFixedWidth(60)
        
        # Connect button to show details
        mas_button.clicked.connect(lambda checked, v=veterinario: self.show_veterinario_details(v))
        
        # Add widgets to row layout
        row_layout.addWidget(info_label)
        row_layout.addStretch()
        row_layout.addWidget(mas_button)
        
        # Add row to main vertical layout
        self.rows.addWidget(row_frame)
    
    def show_veterinario_details(self, veterinario: Veterinario):
        # This would open a detailed view of the veterinarian
        # For now, just show a message box with details
        details = (f"DNI: {veterinario.dni}\n"
                  f"Nombre: {veterinario.name}\n"
                  f"Apellidos: {veterinario.surname}\n"
                  f"Email: {veterinario.email}\n"
                  f"Teléfono: {veterinario.telephone}\n"
                  f"Ubicación: {veterinario.location if veterinario.location else 'No asignada'}")
        
        QMessageBox.information(self, f"Detalles de {veterinario.name}", details)
    
    def on_crear_clicked(self):
        # This would open a dialog to create a new veterinarian
        QMessageBox.information(self, "Crear Veterinario", "Aquí se abriría el formulario para crear un nuevo veterinario.")
    
    def on_volver_clicked(self):
        # This would go back to previous screen
        self.close()

# Main application
def main():
    app = QtWidgets.QApplication(sys.argv)
    
    # Create database connection
    db = Database("veterinaria_clinic")  # Initialize your database
    
    # Create and show main window
    window = VeterinariosMainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()