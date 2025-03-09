import sys
import sqlite3
import os
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QDialog, QVBoxLayout, QTableWidget,
    QTableWidgetItem, QLabel
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from scripts.repositories.ClienteRepository import ClienteRepository
from scripts.model.Cliente import Cliente
from scripts.ui_functionality.clientes.Crear_Actualizar_EliminarClientes import UpdateForm
from scripts.ui_functionality.clientes.Crear_Actualizar_EliminarClientes import CreateForm

class AnimalSearchDialog(QDialog):
    def __init__(self, parent, animals):
        super().__init__(parent)
        self.setWindowTitle('Animales del Cliente')
        layout = QVBoxLayout()

        if not animals:
            no_animals_label = QLabel('No se encontraron animales para este cliente.')
            layout.addWidget(no_animals_label)
        else:
            table = QTableWidget()
            table.setColumnCount(5)
            table.setHorizontalHeaderLabels(['Nombre', 'Especie', 'Raza', 'Edad', 'Sexo'])
            table.setRowCount(len(animals))

            for row, animal in enumerate(animals):
                for col, value in enumerate(animal):
                    table.setItem(row, col, QTableWidgetItem(str(value)))

            layout.addWidget(table)

        self.setLayout(layout)

class ClientesMainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))),
                               'ui/pantalla_principal.ui')
        try:
            uic.loadUi(ui_path, self)
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al cargar UI: {str(e)}")
            return

        # Store parent reference directly
        self.main_window = parent

        self.clients = []

        try:
            self.controller = ClienteRepository()
        except ConnectionError as e:
            QMessageBox.critical(self, "Error de conexión", str(e))
            sys.exit(1)

        self.setupTableView()
        self.loadAllClients()

        # Conectar señales a slots
        self.botonCliente.clicked.connect(self.openCreateForm)
        self.tableViewClientes.doubleClicked.connect(self.openUpdateForm)
        self.botonRegresar.clicked.connect(self.toMenu)

        # Conectar el botón filtra_animales ya existente en el UI
        self.filtra_animales.clicked.connect(self.searchAnimals)

    def toMenu(self):
        self.parent().show()
        self.close()

    def setupTableView(self):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['DNI', 'Nombre', 'Apellido', 'Email', 'Teléfono'])
        self.tableViewClientes.setModel(self.model)

        for column in range(5):
            self.tableViewClientes.setColumnWidth(column, 90)

    def loadAllClients(self):
        self.model.removeRows(0, self.model.rowCount())
        self.clients.clear()

        sqlite_clients = self.controller.getClientes()
        for client_data in sqlite_clients:
            self.clients.append([
                client_data['DNI'],  # Usando 'DNI' en mayúsculas
                client_data['name'],
                client_data['surname'],
                client_data['email'],
                client_data['telephone']
            ])

            row = []
            for data in self.clients[-1]:
                # Convertir datos a cadena (en caso de que no lo sean)
                item = QStandardItem(str(data))
                row.append(item)

            self.model.appendRow(row)

    def searchAnimals(self):
        dni, ok = QtWidgets.QInputDialog.getText(self, 'Buscar Animales', 'Ingrese DNI del cliente:')
        if ok and dni.strip():
            animals = self.findAnimalsByDNI(dni.strip())
            dialog = AnimalSearchDialog(self, animals)
            dialog.exec()

    def findAnimalsByDNI(self, dni):
        try:
            # Usar la misma conexión a la base de datos que el resto de la aplicación
            # a través del controlador existente
            query = """
            SELECT a.name as nombre, a.species as especie, a.description as raza, 
                a.id as edad, 'No disponible' as sexo
            FROM Animales a
            WHERE a.owner = ?
            """

            # Acceder al cursor y conexión a través del controlador
            self.controller.db.cursor.execute(query, (dni,))
            animals = self.controller.db.cursor.fetchall()

            # Convertir los resultados en una lista de tuplas
            result = []
            for animal in animals:
                # Acceder a los elementos por índice, no por nombre de columna
                result.append((
                    animal[0],  # nombre
                    animal[1],  # especie
                    animal[2],  # raza
                    animal[3],  # edad
                    animal[4]   # sexo
                ))

            return result
        except sqlite3.Error as e:
            QMessageBox.warning(self, "Error", f"No se pudo acceder a la base de datos de animales: {e}")
            return []
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Ocurrió un error inesperado: {e}")
            return []

    def openCreateForm(self):
        self.create_form = CreateForm(self)
        self.create_form.show()
        self.hide()

    def openUpdateForm(self, index):
        row = index.row()
        self.update_form = UpdateForm(self, row)
        self.update_form.show()
        self.hide()

    def addClient(self, client_data):
        # Verificar si el DNI ya existe en la base de datos
        existing_client = self.controller.getCliente(client_data[0])
        if existing_client:
            return f"Ya existe un cliente con el DNI {client_data[0]}"

        cliente = Cliente(
            dni=client_data[0],
            name=client_data[1],
            surname=client_data[2],
            email=client_data[3],
            tlfn=client_data[4]
        )

        error = self.controller.postCliente(cliente)
        if error is None:  # Si no hay error
            row = []
            for data in client_data:
                item = QStandardItem(str(data))
                row.append(item)

            self.model.appendRow(row)
            self.clients.append(client_data)
            return True
        else:
            return f"Error: {error}"

    def updateClient(self, row, client_data):
        original_dni = self.clients[row][0]

        # Si el DNI ha cambiado, verificar que el nuevo DNI no exista
        if original_dni != client_data[0]:
            existing_client = self.controller.getCliente(client_data[0])
            if existing_client:
                return f"Ya existe un cliente con el DNI {client_data[0]}"

        cliente = Cliente(
            dni=client_data[0],
            name=client_data[1],
            surname=client_data[2],
            email=client_data[3],
            tlfn=client_data[4]
        )

        error = self.controller.putCliente(original_dni, cliente)
        if error is None:  # Si no hay error
            for col, data in enumerate(client_data):
                self.model.setItem(row, col, QStandardItem(str(data)))

            self.clients[row] = client_data
            return True
        else:
            return f"Error: {error}"

    def deleteClient(self, row):
        dni = self.clients[row][0]

        try:
            self.controller.deleteCliente(dni)
            self.model.removeRow(row)
            del self.clients[row]
            return True
        except Exception as e:
            return f"Error: {str(e)}"