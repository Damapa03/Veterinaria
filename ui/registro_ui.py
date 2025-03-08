# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(381, 484)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.passwordInput = QLineEdit(self.centralwidget)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setGeometry(QRect(30, 270, 311, 21))
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.emailInput = QLineEdit(self.centralwidget)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setGeometry(QRect(30, 180, 311, 21))
        self.emailInput.setEchoMode(QLineEdit.EchoMode.Normal)
        self.aceptatButton = QPushButton(self.centralwidget)
        self.aceptatButton.setObjectName(u"aceptatButton")
        self.aceptatButton.setGeometry(QRect(100, 370, 171, 51))
        self.loginTitle = QLabel(self.centralwidget)
        self.loginTitle.setObjectName(u"loginTitle")
        self.loginTitle.setGeometry(QRect(120, 20, 131, 41))
        self.emailLabel = QLabel(self.centralwidget)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setGeometry(QRect(30, 140, 121, 41))
        self.passwordLabel = QLabel(self.centralwidget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(30, 230, 121, 41))
        self.passwordLabel_2 = QLabel(self.centralwidget)
        self.passwordLabel_2.setObjectName(u"passwordLabel_2")
        self.passwordLabel_2.setGeometry(QRect(110, 430, 161, 41))
        self.passwordLabel_2.setStyleSheet(u"color: blue;")
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.emailInput, self.passwordInput)
        QWidget.setTabOrder(self.passwordInput, self.aceptatButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.aceptatButton.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.loginTitle.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Contrasena", None))
        self.passwordLabel_2.setText(QCoreApplication.translate("MainWindow", u"\u00bfYa tienes cuenta? Inicia sesi\u00f3n", None))
    # retranslateUi

