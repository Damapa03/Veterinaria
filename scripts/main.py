import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QTableView, QLabel, 
    QTextEdit, QGridLayout, QHBoxLayout, QVBoxLayout, QMessageBox
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem

# Importamos el controlador de SQLite y el modelo Cliente
from repository.ClienteRepository import ClienteRepository
from model.Cliente import Cliente
from ui_functionality.Crear_Actualizar_EliminarClientes import UpdateForm
from ui_functionality.Crear_Actualizar_EliminarClientes import CreateForm


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Inicializar la lista de clientes
        self.clients = []
        
        # Inicializar el controlador de SQLite
        try:
            self.controller = ClienteRepository()
        except ConnectionError as e:
            QMessageBox.critical(self, "Error de conexión", str(e))
            sys.exit(1)
        
        self.setupUi()
        self.setWindowTitle('Gestión de Clientes')
        
        # Configurar la tabla con las columnas
        self.setupTableView()
        
        # Cargar todos los clientes desde SQLite
        self.loadAllClients()
        
        # Conectar botones
        self.botonCliente.clicked.connect(self.openCreateForm)
        self.tableViewClientes.doubleClicked.connect(self.openUpdateForm)
        self.botonRegresar.clicked.connect(self.close)
    
    def setupUi(self):
        # Crear los widgets de la pantalla principal
        self.botonCliente = QPushButton("Crear Cliente")
        self.botonRegresar = QPushButton("Regresar")
        self.tableViewClientes = QTableView()
        
        # Configurar el layout
        main_layout = QHBoxLayout()
        
        # Panel izquierdo con botones
        left_panel = QVBoxLayout()
        left_panel.addWidget(self.botonCliente)
        left_panel.addStretch()
        left_panel.addWidget(self.botonRegresar)
        
        # Añadir widgets al layout principal
        main_layout.addLayout(left_panel)
        main_layout.addWidget(self.tableViewClientes, 1)  # El 1 da más espacio a la tabla
        
        # Establecer el layout
        self.setLayout(main_layout)
        self.resize(730, 476)
        
    def setupTableView(self):
        # Crear modelo para la tabla
        self.model = QStandardItemModel()
        
        # Definir las columnas
        self.model.setHorizontalHeaderLabels(['DNI', 'Nombre', 'Apellido', 'Email', 'Teléfono'])
        
        # Asignar el modelo a la tabla
        self.tableViewClientes.setModel(self.model)
        
        # Ajustar el ancho de las columnas
        for column in range(5):
            self.tableViewClientes.setColumnWidth(column, 90)
    
    def loadAllClients(self):
        # Limpiar la tabla
        self.model.removeRows(0, self.model.rowCount())
        self.clients.clear()
        
        # Obtener todos los clientes desde SQLite
        sqlite_clients = self.controller.getClientes()
        
        # Añadir cada cliente a la tabla
        for client_data in sqlite_clients:
            self.clients.append([
                client_data['dni'],
                client_data['name'],
                client_data['surname'],
                client_data['email'],
                client_data['telephone']
            ])
            row = []
            for data in self.clients[-1]:
                item = QStandardItem(data)
                row.append(item)
            self.model.appendRow(row)
    
    def openCreateForm(self):
        # Abrir formulario de creación
        self.create_form = CreateForm(self)
        self.create_form.show()
        self.hide()
    
    def openUpdateForm(self, index):
        # Obtener la fila seleccionada
        row = index.row()
        
        # Abrir formulario de actualización con los datos seleccionados
        self.update_form = UpdateForm(self, row)
        self.update_form.show()
        self.hide()
    
    def addClient(self, client_data):
        # Crear un objeto Cliente
        cliente = Cliente(
            dni=client_data[0],
            name=client_data[1],
            surname=client_data[2],
            email=client_data[3],
            tlfn=client_data[4]
        )
        
        # Añadir a SQLite
        success = self.controller.postCliente(cliente)
        
        if success:
            # Añadir a la tabla si se añadió correctamente a SQLite
            row = []
            for data in client_data:
                item = QStandardItem(data)
                row.append(item)
            
            self.model.appendRow(row)
            self.clients.append(client_data)
            return True
        else:
            QMessageBox.warning(self, "Error", "No se pudo añadir el cliente a la base de datos")
            return False
    
    def updateClient(self, row, client_data):
        # Obtener el DNI original
        original_dni = self.clients[row][0]
        
        # Crear un objeto Cliente con los nuevos datos
        cliente = Cliente(
            dni=client_data[0],
            name=client_data[1],
            surname=client_data[2],
            email=client_data[3],
            tlfn=client_data[4]
        )
        
        # Actualizar en SQLite
        success = self.controller.putCliente(original_dni, cliente)
        
        if success:
            # Actualizar en la tabla si se actualizó correctamente en SQLite
            for col, data in enumerate(client_data):
                self.model.setItem(row, col, QStandardItem(data))
            
            self.clients[row] = client_data
            return True
        else:
            QMessageBox.warning(self, "Error", "No se pudo actualizar el cliente en la base de datos")
            return False
    
    def deleteClient(self, row):
        # Obtener el DNI del cliente
        dni = self.clients[row][0]
        
        # Eliminar de SQLite
        success = self.controller.deleteCliente(dni)
        
        if success:
            # Eliminar de la tabla si se eliminó correctamente de SQLite
            self.model.removeRow(row)
            del self.clients[row]
            return True
        else:
            QMessageBox.warning(self, "Error", "No se pudo eliminar el cliente de la base de datos")
            return False

# Las clases CreateForm y UpdateForm permanecen igual que en tu código original
# ya que solo interactúan con la clase MainWindow

if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    
    # Create the main window
    window = MainWindow()
    
    # Show the window
    window.show()
    
    # Start the event loop
    sys.exit(app.exec())