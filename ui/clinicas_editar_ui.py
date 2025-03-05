# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clinicas_editar.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 275)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 30, 721, 139))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.idDisplayLabel = QLabel(self.formLayoutWidget)
        self.idDisplayLabel.setObjectName(u"idDisplayLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.idDisplayLabel)

        self.nameLabel = QLabel(self.formLayoutWidget)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.nameLabel)

        self.nameInput = QLineEdit(self.formLayoutWidget)
        self.nameInput.setObjectName(u"nameInput")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nameInput)

        self.municipioLabel = QLabel(self.formLayoutWidget)
        self.municipioLabel.setObjectName(u"municipioLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.municipioLabel)

        self.municipioInput = QLineEdit(self.formLayoutWidget)
        self.municipioInput.setObjectName(u"municipioInput")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.municipioInput)

        self.provinciaLabel = QLabel(self.formLayoutWidget)
        self.provinciaLabel.setObjectName(u"provinciaLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.provinciaLabel)

        self.provinciaInput = QLineEdit(self.formLayoutWidget)
        self.provinciaInput.setObjectName(u"provinciaInput")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.provinciaInput)

        self.idDisplay = QLabel(self.formLayoutWidget)
        self.idDisplay.setObjectName(u"idDisplay")
        font = QFont()
        font.setBold(True)
        self.idDisplay.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.idDisplay)

        self.volverButton = QPushButton(self.centralwidget)
        self.volverButton.setObjectName(u"volverButton")
        self.volverButton.setGeometry(QRect(20, 210, 131, 51))
        self.guardarButton = QPushButton(self.centralwidget)
        self.guardarButton.setObjectName(u"guardarButton")
        self.guardarButton.setGeometry(QRect(570, 200, 211, 61))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Modificar Cl\u00ednica", None))
        self.idDisplayLabel.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.municipioLabel.setText(QCoreApplication.translate("MainWindow", u"Municipio:", None))
        self.provinciaLabel.setText(QCoreApplication.translate("MainWindow", u"Provincia:", None))
        self.idDisplay.setText(QCoreApplication.translate("MainWindow", u"ID de la cl\u00ednica", None))
        self.volverButton.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.guardarButton.setText(QCoreApplication.translate("MainWindow", u"Guardar Cambios", None))
    # retranslateUi

