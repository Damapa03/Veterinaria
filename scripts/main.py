import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QTableView, QLabel, 
    QTextEdit, QGridLayout, QHBoxLayout, QVBoxLayout
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Inicializar la lista de clientes antes de usarla
        self.clients = []
        
        self.setupUi()
        self.setWindowTitle('Gestión de Clientes')
        
        # Configurar la tabla con las columnas
        self.setupTableView()
        
        # Añadir cliente de prueba
        self.addTestClient()
        
        # Conectar botones
        self.botonCliente.clicked.connect(self.openCreateForm)
        self.tableViewClientes.doubleClicked.connect(self.openUpdateForm)
    
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
    
    def addTestClient(self):
        # Añadir cliente de prueba
        client_data = ['12345678A', 'Prueba', 'Test', 'prueba@test.com', '123456789']
        row = []
        
        for data in client_data:
            item = QStandardItem(data)
            row.append(item)
        
        self.model.appendRow(row)
        self.clients.append(client_data)
    
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
        # Añadir nuevo cliente a la tabla
        row = []
        
        for data in client_data:
            item = QStandardItem(data)
            row.append(item)
        
        self.model.appendRow(row)
        self.clients.append(client_data)
    
    def updateClient(self, row, client_data):
        # Actualizar cliente existente
        for col, data in enumerate(client_data):
            self.model.setItem(row, col, QStandardItem(data))
        
        self.clients[row] = client_data
    
    def deleteClient(self, row):
        # Eliminar cliente
        self.model.removeRow(row)
        del self.clients[row]

class CreateForm(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setupUi()
        self.setWindowTitle('Crear Cliente')
        self.parent = parent
        
        # Conectar botón
        self.pushButtonCrear.clicked.connect(self.createClient)
    
    def setupUi(self):
        # Crear los widgets
        self.label_dni = QLabel("Dni")
        self.label_nombre = QLabel("Nombre")
        self.label_apellidos = QLabel("Apellidos")
        self.label_email = QLabel("Email")
        self.label_telefono = QLabel("Telefono")
        
        self.textEditDni = QTextEdit()
        self.textEditNombre = QTextEdit()
        self.textEditApellidos = QTextEdit()
        self.textEditEmail = QTextEdit()
        self.textEditTelefono = QTextEdit()
        
        self.pushButtonCrear = QPushButton("Crear")
        
        # Configurar el tamaño de los QTextEdit
        for widget in [self.textEditDni, self.textEditNombre, self.textEditApellidos, 
                      self.textEditEmail, self.textEditTelefono]:
            widget.setMaximumHeight(30)
        
        # Crear el layout para el formulario
        form_layout = QGridLayout()
        form_layout.addWidget(self.label_dni, 0, 0)
        form_layout.addWidget(self.textEditDni, 0, 1)
        form_layout.addWidget(self.label_nombre, 1, 0)
        form_layout.addWidget(self.textEditNombre, 1, 1)
        form_layout.addWidget(self.label_apellidos, 2, 0)
        form_layout.addWidget(self.textEditApellidos, 2, 1)
        form_layout.addWidget(self.label_email, 3, 0)
        form_layout.addWidget(self.textEditEmail, 3, 1)
        form_layout.addWidget(self.label_telefono, 4, 0)
        form_layout.addWidget(self.textEditTelefono, 4, 1)
        
        # Crear layout principal
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.pushButtonCrear, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Establecer el layout
        self.setLayout(main_layout)
        self.resize(465, 417)
    
    def createClient(self):
        # Obtener datos de los campos
        dni = self.textEditDni.toPlainText()
        nombre = self.textEditNombre.toPlainText()
        apellidos = self.textEditApellidos.toPlainText()
        email = self.textEditEmail.toPlainText()
        telefono = self.textEditTelefono.toPlainText()
        
        # Verificar que al menos DNI y nombre no estén vacíos
        if dni and nombre:
            client_data = [dni, nombre, apellidos, email, telefono]
            
            # Añadir cliente a la tabla principal
            self.parent.addClient(client_data)
            
            # Limpiar campos
            self.textEditDni.clear()
            self.textEditNombre.clear()
            self.textEditApellidos.clear()
            self.textEditEmail.clear()
            self.textEditTelefono.clear()
            
            # Volver a la pantalla principal
            self.parent.show()
            self.close()

class UpdateForm(QWidget):
    def __init__(self, parent, row):
        super().__init__()
        self.setupUi()
        self.setWindowTitle('Actualizar Cliente')
        self.parent = parent
        self.row = row
        
        # Cargar datos del cliente seleccionado
        self.loadClientData()
        
        # Conectar botones
        self.pushButtonActualizarCliente.clicked.connect(self.updateClient)
        self.pushButtonEliminarCliente.clicked.connect(self.deleteClient)
    
    def setupUi(self):
        # Crear los widgets
        self.label_dni = QLabel("Dni")
        self.label_nombre = QLabel("Nombre")
        self.label_apellidos = QLabel("Apellidos")
        self.label_email = QLabel("Email")
        self.label_telefono = QLabel("Telefono")
        
        self.textEditDniActualizar = QTextEdit()
        self.textEditNombreActualizar = QTextEdit()
        self.textEditApellidosActualizar = QTextEdit()
        self.textEditEmailActualizar = QTextEdit()
        self.textEditTelefonoActualizar = QTextEdit()
        
        self.pushButtonActualizarCliente = QPushButton("Actualizar")
        self.pushButtonEliminarCliente = QPushButton("Eliminar")
        
        # Configurar el tamaño de los QTextEdit
        for widget in [self.textEditDniActualizar, self.textEditNombreActualizar, 
                       self.textEditApellidosActualizar, self.textEditEmailActualizar, 
                       self.textEditTelefonoActualizar]:
            widget.setMaximumHeight(30)
        
        # Crear el layout para el formulario
        form_layout = QGridLayout()
        form_layout.addWidget(self.label_dni, 0, 0)
        form_layout.addWidget(self.textEditDniActualizar, 0, 1)
        form_layout.addWidget(self.label_nombre, 1, 0)
        form_layout.addWidget(self.textEditNombreActualizar, 1, 1)
        form_layout.addWidget(self.label_apellidos, 2, 0)
        form_layout.addWidget(self.textEditApellidosActualizar, 2, 1)
        form_layout.addWidget(self.label_email, 3, 0)
        form_layout.addWidget(self.textEditEmailActualizar, 3, 1)
        form_layout.addWidget(self.label_telefono, 4, 0)
        form_layout.addWidget(self.textEditTelefonoActualizar, 4, 1)
        
        # Crear layout para los botones
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.pushButtonActualizarCliente)
        button_layout.addWidget(self.pushButtonEliminarCliente)
        
        # Crear layout principal
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        
        # Establecer el layout
        self.setLayout(main_layout)
        self.resize(456, 441)
    
    def loadClientData(self):
        # Obtener datos del cliente seleccionado
        client_data = self.parent.clients[self.row]
        
        # Cargar datos en los campos
        self.textEditDniActualizar.setText(client_data[0])
        self.textEditNombreActualizar.setText(client_data[1])
        self.textEditApellidosActualizar.setText(client_data[2])
        self.textEditEmailActualizar.setText(client_data[3])
        self.textEditTelefonoActualizar.setText(client_data[4])
    
    def updateClient(self):
        # Obtener datos de los campos
        dni = self.textEditDniActualizar.toPlainText()
        nombre = self.textEditNombreActualizar.toPlainText()
        apellidos = self.textEditApellidosActualizar.toPlainText()
        email = self.textEditEmailActualizar.toPlainText()
        telefono = self.textEditTelefonoActualizar.toPlainText()
        
        # Verificar que al menos DNI y nombre no estén vacíos
        if dni and nombre:
            client_data = [dni, nombre, apellidos, email, telefono]
            
            # Actualizar cliente en la tabla principal
            self.parent.updateClient(self.row, client_data)
            
            # Volver a la pantalla principal
            self.parent.show()
            self.close()
    
    def deleteClient(self):
        # Eliminar cliente
        self.parent.deleteClient(self.row)
        
        # Volver a la pantalla principal
        self.parent.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())