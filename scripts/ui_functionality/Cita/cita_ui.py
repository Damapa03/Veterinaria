# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cita.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.controlsLayout = QHBoxLayout()
        self.controlsLayout.setObjectName(u"controlsLayout")
        self.columnsLabel = QLabel(self.centralwidget)
        self.columnsLabel.setObjectName(u"columnsLabel")

        self.controlsLayout.addWidget(self.columnsLabel)

        self.columnsSpinBox = QSpinBox(self.centralwidget)
        self.columnsSpinBox.setObjectName(u"columnsSpinBox")
        self.columnsSpinBox.setMinimum(1)
        self.columnsSpinBox.setMaximum(10)
        self.columnsSpinBox.setValue(4)

        self.controlsLayout.addWidget(self.columnsSpinBox)

        self.addCardButton = QPushButton(self.centralwidget)
        self.addCardButton.setObjectName(u"addCardButton")

        self.controlsLayout.addWidget(self.addCardButton)

        self.updateButton = QPushButton(self.centralwidget)
        self.updateButton.setObjectName(u"updateButton")

        self.controlsLayout.addWidget(self.updateButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.controlsLayout.addItem(self.horizontalSpacer)


        self.mainLayout.addLayout(self.controlsLayout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cardFrame1 = QFrame(self.scrollAreaWidgetContents)
        self.cardFrame1.setObjectName(u"cardFrame1")
        self.cardFrame1.setFrameShape(QFrame.Box)
        self.cardFrame1.setFrameShadow(QFrame.Raised)
        self.cardFrame1.setLineWidth(2)
        self.cardFrame1.setMinimumSize(QSize(200, 150))
        self.cardFrame1.setMaximumSize(QSize(200, 150))
        self.cardLayout1 = QVBoxLayout(self.cardFrame1)
        self.cardLayout1.setObjectName(u"cardLayout1")
        self.titleLabel1 = QLabel(self.cardFrame1)
        self.titleLabel1.setObjectName(u"titleLabel1")

        self.cardLayout1.addWidget(self.titleLabel1)

        self.contentLabel1 = QLabel(self.cardFrame1)
        self.contentLabel1.setObjectName(u"contentLabel1")
        self.contentLabel1.setAlignment(Qt.AlignCenter)
        self.contentLabel1.setWordWrap(True)

        self.cardLayout1.addWidget(self.contentLabel1)

        self.detailsButton1 = QPushButton(self.cardFrame1)
        self.detailsButton1.setObjectName(u"detailsButton1")

        self.cardLayout1.addWidget(self.detailsButton1)


        self.gridLayout.addWidget(self.cardFrame1, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.mainLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Grid Scrolleable de Tarjetas", None))
        self.columnsLabel.setText(QCoreApplication.translate("MainWindow", u"Columnas:", None))
        self.addCardButton.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Tarjeta", None))
        self.updateButton.setText(QCoreApplication.translate("MainWindow", u"Actualizar Grid", None))
        self.cardFrame1.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: white;\n"
"border-radius: 10px;\n"
"padding: 10px;\n"
"margin: 5px;", None))
        self.titleLabel1.setText(QCoreApplication.translate("MainWindow", u"Tarjeta 1", None))
        self.titleLabel1.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-weight: bold; font-size: 16px;", None))
        self.contentLabel1.setText(QCoreApplication.translate("MainWindow", u"Contenido para tarjeta 1", None))
        self.detailsButton1.setText(QCoreApplication.translate("MainWindow", u"Ver Detalles", None))
        self.detailsButton1.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #4CAF50;\n"
"color: white;\n"
"border-radius: 5px;\n"
"padding: 5px;", None))
    # retranslateUi

