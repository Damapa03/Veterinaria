# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clinicas_information.ui'
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
        self.name = QLabel(self.horizontalLayoutWidget)
        self.name.setObjectName(u"name")

        self.horizontalLayout_4.addWidget(self.name)


        self.leftDisplay.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.id = QLabel(self.horizontalLayoutWidget)
        self.id.setObjectName(u"id")

        self.horizontalLayout_3.addWidget(self.id)


        self.leftDisplay.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.leftDisplay.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.leftDisplay)

        self.rightDisplay = QVBoxLayout()
        self.rightDisplay.setObjectName(u"rightDisplay")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.municipio = QLabel(self.horizontalLayoutWidget)
        self.municipio.setObjectName(u"municipio")

        self.horizontalLayout_5.addWidget(self.municipio)


        self.rightDisplay.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.provincia = QLabel(self.horizontalLayoutWidget)
        self.provincia.setObjectName(u"provincia")

        self.horizontalLayout_6.addWidget(self.provincia)


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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n de Cl\u00ednica", None))
        self.volverButton.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.modificarButton.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.borrarButton.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u"Nombre de la Cl\u00ednica", None))
        self.id.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.municipio.setText(QCoreApplication.translate("MainWindow", u"Municipio", None))
        self.provincia.setText(QCoreApplication.translate("MainWindow", u"Provincia", None))
    # retranslateUi

