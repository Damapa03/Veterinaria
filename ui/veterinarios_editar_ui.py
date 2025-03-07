# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'veterinarios_editar.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 275)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 30, 351, 139))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.dniDisplayLabel = QLabel(self.formLayoutWidget)
        self.dniDisplayLabel.setObjectName(u"dniDisplayLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.dniDisplayLabel)

        self.nameLabel = QLabel(self.formLayoutWidget)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.nameLabel)

        self.nameInput = QLineEdit(self.formLayoutWidget)
        self.nameInput.setObjectName(u"nameInput")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nameInput)

        self.surnameLabel = QLabel(self.formLayoutWidget)
        self.surnameLabel.setObjectName(u"surnameLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.surnameLabel)

        self.surnameInput = QLineEdit(self.formLayoutWidget)
        self.surnameInput.setObjectName(u"surnameInput")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.surnameInput)

        self.emailLabel = QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.emailLabel)

        self.emailInput = QLineEdit(self.formLayoutWidget)
        self.emailInput.setObjectName(u"emailInput")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.emailInput)

        self.dniDisplay = QLabel(self.formLayoutWidget)
        self.dniDisplay.setObjectName(u"dniDisplay")
        font = QFont()
        font.setBold(True)
        self.dniDisplay.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dniDisplay)

        self.volverButton = QPushButton(self.centralwidget)
        self.volverButton.setObjectName(u"volverButton")
        self.volverButton.setGeometry(QRect(20, 210, 131, 51))
        self.guardarButton = QPushButton(self.centralwidget)
        self.guardarButton.setObjectName(u"guardarButton")
        self.guardarButton.setGeometry(QRect(570, 200, 211, 61))
        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(400, 30, 351, 105))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.passwordLabel = QLabel(self.formLayoutWidget_2)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.passwordLabel)

        self.passwordInput = QLineEdit(self.formLayoutWidget_2)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.passwordInput)

        self.telephoneLabel = QLabel(self.formLayoutWidget_2)
        self.telephoneLabel.setObjectName(u"telephoneLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.telephoneLabel)

        self.telephoneInput = QLineEdit(self.formLayoutWidget_2)
        self.telephoneInput.setObjectName(u"telephoneInput")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.telephoneInput)

        self.clinicaComboBox = QComboBox(self.formLayoutWidget_2)
        self.clinicaComboBox.setObjectName(u"clinicaComboBox")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.clinicaComboBox)

        self.clinicaLabel = QLabel(self.formLayoutWidget_2)
        self.clinicaLabel.setObjectName(u"clinicaLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.clinicaLabel)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Modificar Veterinario", None))
        self.dniDisplayLabel.setText(QCoreApplication.translate("MainWindow", u"DNI:", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.surnameLabel.setText(QCoreApplication.translate("MainWindow", u"Apellidos:", None))
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.dniDisplay.setText(QCoreApplication.translate("MainWindow", u"DNI del veterinario", None))
        self.volverButton.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.guardarButton.setText(QCoreApplication.translate("MainWindow", u"Guardar Cambios", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dejar en blanco para no cambiar", None))
        self.telephoneLabel.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.clinicaLabel.setText(QCoreApplication.translate("MainWindow", u"Cl\u00ednica:", None))
    # retranslateUi

