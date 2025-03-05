from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

class CreateForm(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        
        # Cargar acrhivo UI
        uic.loadUi("ui\pantalla_crearCliente.ui", self)
        self.setWindowTitle('Crear Cliente')
        
        self.pushButtonCrear.clicked.connect(self.createClient)
        
        self.buttonRegresar.clicked.connect(self.returnToMainScreen)
    
    def returnToMainScreen(self):
        self.parent.show()
        self.close()
    
    def createClient(self):
        dni = self.textEditDni.toPlainText().strip()
        nombre = self.textEditNombre.toPlainText().strip()
        apellidos = self.textEditApellidos.toPlainText().strip()
        email = self.textEditEmail.toPlainText().strip()
        telefono = self.textEditTelefono.toPlainText().strip()
        
        if not dni or not nombre or not apellidos:
            QMessageBox.warning(self, "Campos requeridos", "Los campos DNI, Nombre y Apellidos son obligatorios")
            return
        
        client_data = [dni, nombre, apellidos, email, telefono]
        
        if self.parent.addClient(client_data):
            QMessageBox.information(self, "Éxito", "Cliente creado correctamente")
            self.parent.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "No se pudo crear el cliente")


class UpdateForm(QWidget):
    def __init__(self, parent, row):
        super().__init__()
        self.parent = parent
        self.row = row
        self.client_data = parent.clients[row]
        
        # Cargar acrhivo UI
        uic.loadUi("ui\pantalla_actualizarEliminarCliente.ui", self)
        self.setWindowTitle('Actualizar/Eliminar Cliente')
        
        self.fillClientData()
        
        self.pushButtonActualizarCliente.clicked.connect(self.updateClient)
        self.pushButtonEliminarCliente.clicked.connect(self.deleteClient)
        
        self.buttonRegresar.clicked.connect(self.returnToMainScreen)
    
    def returnToMainScreen(self):
        self.parent.show()
        self.close()
    
    def fillClientData(self):
        self.textEditDniActualizar.setText(self.client_data[0])
        self.textEditNombreActualizar.setText(self.client_data[1])
        self.textEditApellidosActualizar.setText(self.client_data[2])
        self.textEditEmailActualizar.setText(self.client_data[3])
        self.textEditTelefonoActualizar.setText(self.client_data[4])
    
    def updateClient(self):
        dni = self.textEditDniActualizar.toPlainText().strip()
        nombre = self.textEditNombreActualizar.toPlainText().strip()
        apellidos = self.textEditApellidosActualizar.toPlainText().strip()
        email = self.textEditEmailActualizar.toPlainText().strip()
        telefono = self.textEditTelefonoActualizar.toPlainText().strip()
        
        if not dni or not nombre or not apellidos:
            QMessageBox.warning(self, "Campos requeridos", "Los campos DNI, Nombre y Apellidos son obligatorios")
            return
        
        # Update client
        client_data = [dni, nombre, apellidos, email, telefono]
        
        if self.parent.updateClient(self.row, client_data):
            QMessageBox.information(self, "Éxito", "Cliente actualizado correctamente")
            self.parent.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "No se pudo actualizar el cliente")
    
    def deleteClient(self):
        reply = QMessageBox.question(self, 'Confirmar eliminación', 
                                    '¿Está seguro que desea eliminar este cliente?',
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                    QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            if self.parent.deleteClient(self.row):
                QMessageBox.information(self, "Éxito", "Cliente eliminado correctamente")
                self.parent.show()
                self.close()
            else:
                QMessageBox.warning(self, "Error", "No se pudo eliminar el cliente")