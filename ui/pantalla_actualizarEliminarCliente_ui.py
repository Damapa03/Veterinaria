# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_actualizarEliminarCliente.ui'
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
        Form.resize(456, 441)
        self.gridLayoutWidget_2 = QWidget(Form)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(30, 50, 411, 251))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)

        self.textEditDniActualizar = QTextEdit(self.gridLayoutWidget_2)
        self.textEditDniActualizar.setObjectName(u"textEditDniActualizar")

        self.gridLayout_2.addWidget(self.textEditDniActualizar, 0, 1, 1, 1)

        self.textEditTelefonoActualizar = QTextEdit(self.gridLayoutWidget_2)
        self.textEditTelefonoActualizar.setObjectName(u"textEditTelefonoActualizar")

        self.gridLayout_2.addWidget(self.textEditTelefonoActualizar, 4, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.textEditApellidosActualizar = QTextEdit(self.gridLayoutWidget_2)
        self.textEditApellidosActualizar.setObjectName(u"textEditApellidosActualizar")

        self.gridLayout_2.addWidget(self.textEditApellidosActualizar, 2, 1, 1, 1)

        self.textEditNombreActualizar = QTextEdit(self.gridLayoutWidget_2)
        self.textEditNombreActualizar.setObjectName(u"textEditNombreActualizar")

        self.gridLayout_2.addWidget(self.textEditNombreActualizar, 1, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.textEditEmailActualizar = QTextEdit(self.gridLayoutWidget_2)
        self.textEditEmailActualizar.setObjectName(u"textEditEmailActualizar")

        self.gridLayout_2.addWidget(self.textEditEmailActualizar, 3, 1, 1, 1)

        self.pushButtonActualizarCliente = QPushButton(Form)
        self.pushButtonActualizarCliente.setObjectName(u"pushButtonActualizarCliente")
        self.pushButtonActualizarCliente.setGeometry(QRect(50, 360, 131, 51))
        self.pushButtonEliminarCliente = QPushButton(Form)
        self.pushButtonEliminarCliente.setObjectName(u"pushButtonEliminarCliente")
        self.pushButtonEliminarCliente.setGeometry(QRect(300, 360, 131, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Email", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Telefono", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Apellidos", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Dni", None))
        self.pushButtonActualizarCliente.setText(QCoreApplication.translate("Form", u"Actualizar", None))
        self.pushButtonEliminarCliente.setText(QCoreApplication.translate("Form", u"Eliminar", None))
    # retranslateUi

