# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDoubleSpinBox,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitulo = QLabel(Form)
        self.labelTitulo.setObjectName(u"labelTitulo")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelTitulo)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.editMotivo = QLineEdit(Form)
        self.editMotivo.setObjectName(u"editMotivo")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.editMotivo)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.editFecha = QDateTimeEdit(Form)
        self.editFecha.setObjectName(u"editFecha")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.editFecha)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.editPrecio = QDoubleSpinBox(Form)
        self.editPrecio.setObjectName(u"editPrecio")
        self.editPrecio.setMaximum(9999.989999999999782)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.editPrecio)

        self.editProfesional = QComboBox(Form)
        self.editProfesional.setObjectName(u"editProfesional")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.editProfesional)

        self.editAnimal = QComboBox(Form)
        self.editAnimal.setObjectName(u"editAnimal")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.editAnimal)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnGuardar = QPushButton(Form)
        self.btnGuardar.setObjectName(u"btnGuardar")

        self.horizontalLayout.addWidget(self.btnGuardar)

        self.btnCancelar = QPushButton(Form)
        self.btnCancelar.setObjectName(u"btnCancelar")

        self.horizontalLayout.addWidget(self.btnCancelar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Detalle de Cita", None))
        self.labelTitulo.setText(QCoreApplication.translate("Form", u"Editar Cita", None))
        self.label.setText(QCoreApplication.translate("Form", u"Motivo:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Animal:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Profesional:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Fecha:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Precio:", None))
        self.editPrecio.setSuffix(QCoreApplication.translate("Form", u" \u20ac", None))
        self.btnGuardar.setText(QCoreApplication.translate("Form", u"Guardar", None))
        self.btnCancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
    # retranslateUi

