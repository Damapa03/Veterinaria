# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(649, 477)
        self.botonCliente = QPushButton(MainWindow)
        self.botonCliente.setObjectName(u"botonCliente")
        self.botonCliente.setGeometry(QRect(30, 70, 121, 61))
        self.botonCliente.setStyleSheet(u"QPushButton {\n"
"    background-color: lightgreen;\n"
"    color: Black;\n"
"    border: 2px solid #006400;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #00b300;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004d00;\n"
"}\n"
"")
        self.botonRegresar = QPushButton(MainWindow)
        self.botonRegresar.setObjectName(u"botonRegresar")
        self.botonRegresar.setGeometry(QRect(20, 360, 141, 51))
        self.botonRegresar.setStyleSheet(u"QPushButton {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: darkgray;\n"
"}\n"
"")
        self.tableViewClientes = QTableView(MainWindow)
        self.tableViewClientes.setObjectName(u"tableViewClientes")
        self.tableViewClientes.setGeometry(QRect(180, 30, 461, 421))
        self.tableViewClientes.setMinimumSize(QSize(451, 0))
        self.tableViewClientes.setStyleSheet(u"")
        self.tableViewClientes.verticalHeader().setVisible(False)
        self.filtra_animales = QPushButton(MainWindow)
        self.filtra_animales.setObjectName(u"filtra_animales")
        self.filtra_animales.setGeometry(QRect(20, 200, 141, 31))
        self.filtra_animales.setStyleSheet(u"QPushButton {\n"
"    background-color: lightgray;\n"
"    color: black;\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: darkgray;\n"
"}\n"
"")

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Clientes", None))
        self.botonCliente.setText(QCoreApplication.translate("MainWindow", u"Crear Cliente", None))
        self.botonRegresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.filtra_animales.setText(QCoreApplication.translate("MainWindow", u"Ver animales por DNI ", None))
    # retranslateUi

