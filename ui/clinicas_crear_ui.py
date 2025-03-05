# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clinicas_crear.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 275)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.volverButton = QPushButton(self.centralwidget)
        self.volverButton.setObjectName(u"volverButton")
        self.volverButton.setGeometry(QRect(20, 210, 131, 51))
        self.aceptarButton = QPushButton(self.centralwidget)
        self.aceptarButton.setObjectName(u"aceptarButton")
        self.aceptarButton.setGeometry(QRect(570, 200, 211, 61))
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 30, 721, 139))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.nameLabel = QLabel(self.formLayoutWidget)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameInput = QLineEdit(self.formLayoutWidget)
        self.nameInput.setObjectName(u"nameInput")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameInput)

        self.municipioLabel = QLabel(self.formLayoutWidget)
        self.municipioLabel.setObjectName(u"municipioLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.municipioLabel)

        self.municipioInput = QLineEdit(self.formLayoutWidget)
        self.municipioInput.setObjectName(u"municipioInput")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.municipioInput)

        self.provinciaLabel = QLabel(self.formLayoutWidget)
        self.provinciaLabel.setObjectName(u"provinciaLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.provinciaLabel)

        self.provinciaInput = QLineEdit(self.formLayoutWidget)
        self.provinciaInput.setObjectName(u"provinciaInput")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.provinciaInput)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Crear Cl\u00ednica", None))
        self.volverButton.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.aceptarButton.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.municipioLabel.setText(QCoreApplication.translate("MainWindow", u"Municipio:", None))
        self.provinciaLabel.setText(QCoreApplication.translate("MainWindow", u"Provincia:", None))
    # retranslateUi

