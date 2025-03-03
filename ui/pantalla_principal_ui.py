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
        MainWindow.resize(730, 478)
        self.botonCliente = QPushButton(MainWindow)
        self.botonCliente.setObjectName(u"botonCliente")
        self.botonCliente.setGeometry(QRect(50, 70, 131, 81))
        self.botonRegresar = QPushButton(MainWindow)
        self.botonRegresar.setObjectName(u"botonRegresar")
        self.botonRegresar.setGeometry(QRect(40, 380, 141, 51))
        self.tableViewClientes = QTableView(MainWindow)
        self.tableViewClientes.setObjectName(u"tableViewClientes")
        self.tableViewClientes.setGeometry(QRect(240, 30, 461, 421))

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Clientes", None))
        self.botonCliente.setText(QCoreApplication.translate("MainWindow", u"Crear Cliente", None))
        self.botonRegresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
    # retranslateUi

