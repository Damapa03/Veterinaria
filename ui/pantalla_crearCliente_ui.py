# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_crearCliente.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(465, 415)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 30, 411, 306))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.textEditDni = QTextEdit(self.gridLayoutWidget)
        self.textEditDni.setObjectName(u"textEditDni")

        self.gridLayout.addWidget(self.textEditDni, 0, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.textEditTelefono = QTextEdit(self.gridLayoutWidget)
        self.textEditTelefono.setObjectName(u"textEditTelefono")

        self.gridLayout.addWidget(self.textEditTelefono, 4, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.textEditApellidos = QTextEdit(self.gridLayoutWidget)
        self.textEditApellidos.setObjectName(u"textEditApellidos")

        self.gridLayout.addWidget(self.textEditApellidos, 2, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.textEditNombre = QTextEdit(self.gridLayoutWidget)
        self.textEditNombre.setObjectName(u"textEditNombre")

        self.gridLayout.addWidget(self.textEditNombre, 1, 1, 1, 1)

        self.textEditEmail = QTextEdit(self.gridLayoutWidget)
        self.textEditEmail.setObjectName(u"textEditEmail")

        self.gridLayout.addWidget(self.textEditEmail, 3, 1, 1, 1)

        self.pushButtonCrear = QPushButton(Form)
        self.pushButtonCrear.setObjectName(u"pushButtonCrear")
        self.pushButtonCrear.setGeometry(QRect(220, 360, 131, 51))
        self.pushButtonCrear.setStyleSheet(u"QPushButton {\n"
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
        self.buttonRegresar = QPushButton(Form)
        self.buttonRegresar.setObjectName(u"buttonRegresar")
        self.buttonRegresar.setGeometry(QRect(30, 360, 111, 51))
        self.buttonRegresar.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Email", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Telefono", None))
        self.label.setText(QCoreApplication.translate("Form", u"Dni", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Apellidos", None))
        self.pushButtonCrear.setText(QCoreApplication.translate("Form", u"Crear", None))
        self.buttonRegresar.setText(QCoreApplication.translate("Form", u"Regresar", None))
    # retranslateUi

