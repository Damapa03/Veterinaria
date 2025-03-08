import os
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox

from scripts.model.Receta import Receta
from scripts.repositories.AnimalRepository import AnimalRepository
from scripts.repositories.RecetaRepository import RecetaRepository
from scripts.ui_functionality.receta.receta_editar import RecetaEditWindow


class RecetaDetailWindow(QtWidgets.QMainWindow):
    """Ventana para mostrar detalles de una receta médica"""

    def __init__(self, parent=None, receta=None):
        super().__init__()
        self.parent = parent
        self.receta = receta
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Cargar archivo UI
        ui_path = os.path.join(current_dir, '../../../ui/recetas_information.ui')

        try:
            uic.loadUi(ui_path, self)
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al cargar UI: {str(e)}")
            return

        # Inicializar repositorio
        self.recetaRepository = RecetaRepository()
        self.animalRepository = AnimalRepository()

        # Configurar título de la ventana
        self.setWindowTitle(f"Detalles de Receta #{receta.id}")

        # Mostrar información de la receta
        self.display_receta_info()

        # Conectar señales de botones
        self.volverButton.clicked.connect(self.on_volver_clicked)
        self.modificarButton.clicked.connect(self.on_modificar_clicked)
        self.borrarButton.clicked.connect(self.on_borrar_clicked)

    def display_receta_info(self):
        """Mostrar la información de la receta en la interfaz"""
        try:
            self.idLabel.setText(f"ID: {self.receta.id}")
            self.treatmentLabel.setText(f"Tratamiento: {self.receta.treatment}")
            self.startDateLabel.setText(f"Fecha de inicio: {self.receta.start_date}")

            # Mostrar estado de finalización
            estado = "Finalizada" if self.receta.finalized else "En curso"
            self.finalizedLabel.setText(f"Estado: {estado}")
            self.animalName = self.animalRepository.getAnimalName(self.receta.pacient)[0] #Saca el nombre
            self.pacientLabel.setText(f"Paciente: {self.animalName}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al mostrar información: {str(e)}")

    def on_volver_clicked(self):
        """Volver a la pantalla principal"""
        self.parent.show()
        self.close()

    def on_modificar_clicked(self):
        """Abrir ventana para modificar la receta"""
        self.edit_window = RecetaEditWindow(self, self.receta.id)
        self.edit_window.show()
        self.hide()

    def on_borrar_clicked(self):
        """Eliminar la receta actual previa confirmación"""
        reply = QMessageBox.question(self, 'Confirmar eliminación',
                                     f'¿Está seguro de que desea eliminar la receta #{self.receta.id}?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            try:
                # Intentar eliminar la receta
                result = self.recetaRepository.deleteReceta(self.receta.id)

                if result:
                    QMessageBox.information(self, "Éxito",
                                            "Receta eliminada correctamente")
                    self.parent.load_recetas()  # Recargar lista en ventana principal
                    self.parent.show()
                    self.close()
                else:
                    QMessageBox.critical(self, "Error",
                                         "No se pudo eliminar la receta. Ha ocurrido un error en la base de datos.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al eliminar receta: {str(e)}")