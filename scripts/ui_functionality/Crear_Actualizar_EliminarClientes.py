from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

class CreateForm(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        
        # Load UI file
        uic.loadUi("ui\pantalla_crearCliente.ui", self)
        self.setWindowTitle('Crear Cliente')
        
        # Connect buttons
        self.pushButtonCrear.clicked.connect(self.createClient)
        
        # Connect the return button to go back to the main screen
        self.buttonRegresar.clicked.connect(self.returnToMainScreen)
    
    def returnToMainScreen(self):
        # Show the parent (main) window and close the current window
        self.parent.show()
        self.close()
    
    def createClient(self):
        # Validate fields
        dni = self.textEditDni.toPlainText().strip()
        nombre = self.textEditNombre.toPlainText().strip()
        apellidos = self.textEditApellidos.toPlainText().strip()
        email = self.textEditEmail.toPlainText().strip()
        telefono = self.textEditTelefono.toPlainText().strip()
        
        if not dni or not nombre or not apellidos:
            QMessageBox.warning(self, "Campos requeridos", "Los campos DNI, Nombre y Apellidos son obligatorios")
            return
        
        # Create client
        client_data = [dni, nombre, apellidos, email, telefono]
        
        if self.parent.addClient(client_data):
            QMessageBox.information(self, "Éxito", "Cliente creado correctamente")
            # Return to main screen
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
        
        # Load UI file
        uic.loadUi("ui\pantalla_actualizarEliminarCliente.ui", self)
        self.setWindowTitle('Actualizar/Eliminar Cliente')
        
        # Fill fields with client information
        self.fillClientData()
        
        # Connect buttons
        self.pushButtonActualizarCliente.clicked.connect(self.updateClient)
        self.pushButtonEliminarCliente.clicked.connect(self.deleteClient)
        
        # Connect the return button to go back to the main screen
        self.buttonRegresar.clicked.connect(self.returnToMainScreen)
    
    def returnToMainScreen(self):
        # Show the parent (main) window and close the current window
        self.parent.show()
        self.close()
    
    def fillClientData(self):
        # Fill the fields with the selected client's information
        self.textEditDniActualizar.setText(self.client_data[0])
        self.textEditNombreActualizar.setText(self.client_data[1])
        self.textEditApellidosActualizar.setText(self.client_data[2])
        self.textEditEmailActualizar.setText(self.client_data[3])
        self.textEditTelefonoActualizar.setText(self.client_data[4])
    
    def updateClient(self):
        # Validate fields
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
            # Return to main screen
            self.parent.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "No se pudo actualizar el cliente")
    
    def deleteClient(self):
        # Confirm deletion
        reply = QMessageBox.question(self, 'Confirmar eliminación', 
                                    '¿Está seguro que desea eliminar este cliente?',
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                    QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            if self.parent.deleteClient(self.row):
                QMessageBox.information(self, "Éxito", "Cliente eliminado correctamente")
                # Return to main screen
                self.parent.show()
                self.close()
            else:
                QMessageBox.warning(self, "Error", "No se pudo eliminar el cliente")