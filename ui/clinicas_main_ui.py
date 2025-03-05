# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clinicas_main.ui'
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
from PySide6.QtWidgets import (QApplication, QLayout, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 597)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.crearButton = QPushButton(self.centralwidget)
        self.crearButton.setObjectName(u"crearButton")
        self.crearButton.setGeometry(QRect(20, 20, 151, 51))
        self.volverButton = QPushButton(self.centralwidget)
        self.volverButton.setObjectName(u"volverButton")
        self.volverButton.setGeometry(QRect(20, 540, 91, 41))
        self.informationScroll = QScrollArea(self.centralwidget)
        self.informationScroll.setObjectName(u"informationScroll")
        self.informationScroll.setGeometry(QRect(210, 20, 571, 561))
        self.informationScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.informationScroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 569, 559))
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 571, 561))
        self.rows = QVBoxLayout(self.verticalLayoutWidget)
        self.rows.setObjectName(u"rows")
        self.rows.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.rows.setContentsMargins(0, 0, 0, 0)
        self.informationScroll.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Cl\u00ednicas", None))
        self.crearButton.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.volverButton.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
    # retranslateUi

