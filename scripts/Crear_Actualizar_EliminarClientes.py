from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

class CreateForm(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        
        # Cargar el archivo UI directamente (ajuste la ruta según sea necesario)
        uic.loadUi("scripts\crear_cliente.ui", self)
        self.setWindowTitle('Crear Cliente')
        
        # Conectar botones
        self.pushButtonCrear.clicked.connect(self.createClient)
    
    def createClient(self):
        # Validar campos
        dni = self.textEditDni.toPlainText().strip()
        nombre = self.textEditNombre.toPlainText().strip()
        apellidos = self.textEditApellidos.toPlainText().strip()
        email = self.textEditEmail.toPlainText().strip()
        telefono = self.textEditTelefono.toPlainText().strip()
        
        if not dni or not nombre or not apellidos:
            QMessageBox.warning(self, "Campos requeridos", "Los campos DNI, Nombre y Apellidos son obligatorios")
            return
        
        # Crear cliente
        client_data = [dni, nombre, apellidos, email, telefono]
        
        if self.parent.addClient(client_data):
            QMessageBox.information(self, "Éxito", "Cliente creado correctamente")
            # Volver a la pantalla principal
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
        
        # Cargar el archivo UI directamente (ajuste la ruta según sea necesario)
        uic.loadUi("scripts/actualizar_cliente.ui", self)
        self.setWindowTitle('Actualizar/Eliminar Cliente')
        
        # Llenar campos con la información del cliente
        self.fillClientData()
        
        # Conectar botones
        self.pushButtonActualizarCliente.clicked.connect(self.updateClient)
        self.pushButtonEliminarCliente.clicked.connect(self.deleteClient)
    
    def fillClientData(self):
        # Llenar los campos con la información del cliente seleccionado
        self.textEditDniActualizar.setText(self.client_data[0])
        self.textEditNombreActualizar.setText(self.client_data[1])
        self.textEditApellidosActualizar.setText(self.client_data[2])
        self.textEditEmailActualizar.setText(self.client_data[3])
        self.textEditTelefonoActualizar.setText(self.client_data[4])
    
    def updateClient(self):
        # Validar campos
        dni = self.textEditDniActualizar.toPlainText().strip()
        nombre = self.textEditNombreActualizar.toPlainText().strip()
        apellidos = self.textEditApellidosActualizar.toPlainText().strip()
        email = self.textEditEmailActualizar.toPlainText().strip()
        telefono = self.textEditTelefonoActualizar.toPlainText().strip()
        
        if not dni or not nombre or not apellidos:
            QMessageBox.warning(self, "Campos requeridos", "Los campos DNI, Nombre y Apellidos son obligatorios")
            return
        
        # Actualizar cliente
        client_data = [dni, nombre, apellidos, email, telefono]
        
        if self.parent.updateClient(self.row, client_data):
            QMessageBox.information(self, "Éxito", "Cliente actualizado correctamente")
            # Volver a la pantalla principal
            self.parent.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "No se pudo actualizar el cliente")
    
    def deleteClient(self):
        # Confirmar eliminación
        reply = QMessageBox.question(self, 'Confirmar eliminación', 
                                    '¿Está seguro que desea eliminar este cliente?',
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                    QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            if self.parent.deleteClient(self.row):
                QMessageBox.information(self, "Éxito", "Cliente eliminado correctamente")
                # Volver a la pantalla principal
                self.parent.show()
                self.close()
            else:
                QMessageBox.warning(self, "Error", "No se pudo eliminar el cliente")