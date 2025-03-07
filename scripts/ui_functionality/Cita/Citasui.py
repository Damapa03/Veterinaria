from datetime import date
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QLabel, QScrollArea, 
                             QPushButton, QSpinBox, QFrame, QSizePolicy)
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QFont

from scripts.model.Cita import Cita
from scripts.repositories.CitaRepository import CitaRepository as repository
# Importar la clase Cita desde su módulo

class TarjetaCita(QFrame):
    def __init__(self, parent = None, cita = None, on_eliminar = None, on_editar = None):
        super().__init__(parent)
        self.cita = cita
        self.on_eliminar = on_eliminar
        self.on_editar = on_editar
        self.initUI()       
    
    def initUI(self):
        
        layout = QVBoxLayout(self)
        
        # Titulo 
        titulo = QLabel(self.cita["motivo"])
        titulo.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titulo)
        
        # Detalles
        detalles = QVBoxLayout()
        detalles.addWidget(QLabel(f"Animal: {self.cita['animal']}"))
        detalles.addWidget(QLabel(f"Profesional: {self.cita['profesional']}"))
        detalles.addWidget(QLabel(f"Fecha: {self.cita['fecha']}"))
        detalles.addWidget(QLabel(f"Precio: {self.cita['precio']} €"))
        layout.addLayout(detalles)
        
        #Botones
        btn_layout = QHBoxLayout()
        
        btn_eliminar = QPushButton("Eliminar")
        btn_eliminar.setStyleSheet("""
        QPushButton {
            background-color: #ff5e5e;
            color: black;
            border: 2px solid #8B0000;
            border-radius: 10px;
            padding: 5px;
        }

        QPushButton:hover {
            background-color: #df5252;
        }

        QPushButton:pressed {
            background-color: #cc0000;
        }
        """)
        btn_eliminar.clicked.connect(lambda: self.on_eliminar(self.cita["id"]))
        
        btn_editar = QPushButton("Editar")
        btn_editar.setStyleSheet("""
        QPushButton {
            background-color: lightgray;
            color: black;
            border: 2px solid gray;
            border-radius: 10px;
            padding: 5px;
        }

        QPushButton:hover {
            background-color: silver;
        }

        QPushButton:pressed {
            background-color: darkgray;
        }

        """)
        btn_editar.clicked.connect(lambda: self.on_editar(self.cita))
        
        btn_layout.addWidget(btn_eliminar)
        btn_layout.addWidget(btn_editar)
        layout.addLayout(btn_layout)

class EditarCitaWindow(QWidget):
    def __init__(self, cita=None, on_guardar=None, is_new=False):
        super().__init__()
        self.cita = cita
        self.is_new = is_new
        self.on_guardar = on_guardar
        self.ui = uic.loadUi("ui/cita_edit.ui", self)
        self.cargarDatos()
        self.conectarBotones()
        
    def cargarDatos(self):
        if self.cita:
            self.ui.editMotivo.setText(self.cita["motivo"])
            
            self.ui.editAnimal.clear()
            animales = repository().getAnimal()
            for animal in animales:
                self.ui.editAnimal.addItem(animal[1], animal[0])

            self.ui.editProfesional.clear()
            profesionales = repository().getVetarinarioNombreDNI()
            for profesional in profesionales:
                self.ui.editProfesional.addItem(profesional[1], profesional[0])
                
            self.ui.editFecha.setDateTime(QDateTime.fromString(self.cita["fecha"], "yyyy-MM-dd hh:mm"))
            self.ui.editPrecio.setValue(self.cita["precio"])
    
    def conectarBotones(self):
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnCancelar.clicked.connect(self.close)
    
    def guardar(self):
        cita_actualizada = {
            "id": self.cita["id"],
            "motivo": self.ui.editMotivo.text(),
            "animal": self.ui.editAnimal.currentData(),
            "profesional": self.ui.editProfesional.currentData(),
            "fecha": self.ui.editFecha.dateTime().toString("yyyy-MM-dd hh:mm"),
            "precio": self.ui.editPrecio.value()
        }
        self.on_guardar(cita_actualizada)
        postCita = Cita(
            fecha= cita_actualizada["fecha"],
            precio= cita_actualizada["precio"],
            motivo= cita_actualizada["motivo"],
            animal= cita_actualizada["animal"],
            profesional= cita_actualizada["profesional"]
        )
        if self.is_new:
            repository().postCita(postCita)
        self.close()     


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/cita.ui", self)
        self.citas = self.CitaDictionary()
        self.initUI()
    
    
    def CitaDictionary(self):
        citas = []
        
        citaRepository = repository().getCitas()
        for cita in citaRepository:
            d = {
                "id": cita[0],
                "fecha" : cita[1],
                "precio": cita[2],
                "motivo": cita[3],
                "animal": cita[4],
                "profesional": cita[5]
            } 
            citas.append(d)
        return citas
    
    
    def initUI(self):
        self.setWindowTitle("Citas Veterinarias")
        
        self.spinColumnas.valueChanged.connect(self.actualizarGrid)
        
        self.btnNuevaCita.clicked.connect(self.nuevaCita)
       
       # Widget contenedor del grid 
        self.grid_widget = QWidget()
        self.grid_layout = QGridLayout(self.grid_widget)
        
        self.scrollArea.setWidget(self.grid_widget)
        
        self.actualizarGrid()
    
    def actualizarGrid(self):
        # Limpiar el grid actual
        while self.grid_layout.count():
            item = self.grid_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        # Obtener el número de columnas
        num_columnas = self.spinColumnas.value()
        
        # Colocar las tarjetas en el grid
        row, col = 0, 0
        for cita in self.citas:
            tarjeta = TarjetaCita(
                cita=cita,
                on_eliminar=self.deleteCard,
                on_editar=self.editCard
            )
            self.grid_layout.addWidget(tarjeta, row, col)
            
            col += 1
            if col >= num_columnas:
                col = 0
                row += 1    
                
    def guardarCitaEditada(self, cita_actualizada):
        for i, cita in enumerate(self.citas):
            if cita["id"] == cita_actualizada["id"]:
                self.citas[i] = cita_actualizada
                putCita = Cita(
                    fecha= cita_actualizada["fecha"],
                    precio= cita_actualizada["precio"],
                    motivo= cita_actualizada["motivo"],
                    animal= cita_actualizada["animal"],
                    profesional= cita_actualizada["profesional"]
                )
                repository().putCita(cita["id"], putCita)
                break
        self.actualizarGrid()

    def editCard(self, cita):
        self.ventana_editar = EditarCitaWindow(cita=cita, on_guardar=self.guardarCitaEditada, is_new=False)
        self.ventana_editar.show()
    
    def deleteCard(self, id_cita):
        self.citas = [cita for cita in self.citas if cita["id"] != id_cita]
        repository().deleteCita(id_cita)
        self.actualizarGrid()
  
    def nuevaCita(self):
        # Crear un ID nuevo
        nuevo_id = max([cita["id"] for cita in self.citas]) + 1 if self.citas else 1
        
        # Crear una cita vacía
        nueva_cita = {
            "id": nuevo_id,
            "motivo": "Nueva cita",
            "animal": "",
            "profesional": "",
            "fecha": "2025-03-01 10:00",
            "precio": 0.0
        }
        
        # Abrir ventana de edición
        self.ventana_editar = EditarCitaWindow(cita=nueva_cita, on_guardar=self.guardarNuevaCita, is_new=True)
        self.ventana_editar.show()

    def guardarNuevaCita(self, nueva_cita):
        self.citas.append(nueva_cita)
        # repository().postCitas(nueva_cita)
        self.actualizarGrid()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())