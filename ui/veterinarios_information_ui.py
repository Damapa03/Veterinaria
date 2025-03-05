# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'veterinarios_information.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 333)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.volverButton = QPushButton(self.centralwidget)
        self.volverButton.setObjectName(u"volverButton")
        self.volverButton.setGeometry(QRect(10, 270, 101, 41))
        self.modificarButton = QPushButton(self.centralwidget)
        self.modificarButton.setObjectName(u"modificarButton")
        self.modificarButton.setGeometry(QRect(500, 260, 131, 51))
        self.borrarButton = QPushButton(self.centralwidget)
        self.borrarButton.setObjectName(u"borrarButton")
        self.borrarButton.setGeometry(QRect(650, 260, 131, 51))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 30, 781, 141))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftDisplay = QVBoxLayout()
        self.leftDisplay.setObjectName(u"leftDisplay")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.nameAndSurname = QLabel(self.horizontalLayoutWidget)
        self.nameAndSurname.setObjectName(u"nameAndSurname")

        self.horizontalLayout_4.addWidget(self.nameAndSurname)


        self.leftDisplay.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dni = QLabel(self.horizontalLayoutWidget)
        self.dni.setObjectName(u"dni")

        self.horizontalLayout_3.addWidget(self.dni)


        self.leftDisplay.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.clinica = QLabel(self.horizontalLayoutWidget)
        self.clinica.setObjectName(u"clinica")

        self.horizontalLayout_2.addWidget(self.clinica)


        self.leftDisplay.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.leftDisplay)

        self.rightDisplay = QVBoxLayout()
        self.rightDisplay.setObjectName(u"rightDisplay")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.email = QLabel(self.horizontalLayoutWidget)
        self.email.setObjectName(u"email")

        self.horizontalLayout_5.addWidget(self.email)


        self.rightDisplay.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)


        self.rightDisplay.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.rightDisplay.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.rightDisplay)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.volverButton.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.modificarButton.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.borrarButton.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.nameAndSurname.setText(QCoreApplication.translate("MainWindow", u"Nombre y Apellidos", None))
        self.dni.setText(QCoreApplication.translate("MainWindow", u"DNI", None))
        self.clinica.setText(QCoreApplication.translate("MainWindow", u"Asignado en 'Cl\u00ednica'", None))
        self.email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
    # retranslateUi

