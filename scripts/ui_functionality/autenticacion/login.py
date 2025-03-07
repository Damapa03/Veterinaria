import os
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox, QApplication
import scripts.Autentication as auth

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/login.ui', self)

        # Connect the bottom label to switch to registration window
        self.passwordLabel_2.mousePressEvent = self.switch_to_register

        # Connect the login button to login function
        self.aceptatButton.clicked.connect(self.perform_login)

    def switch_to_register(self, event):
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()

    def perform_login(self):
        email = self.emailInput.text()
        password = self.passwordInput.text()

        # Placeholder login function
        login_result = self.validate_login(email, password)

        if login_result:
            # If login is successful, you would typically navigate to the main application window
            # For now, we'll just print a success message
            print("Login successful!")
            # Here you would create and show your main application window
            # self.main_window = MainWindow()
            # self.main_window.show()
            # self.close()
        else:
            # Show error message if login fails
            QMessageBox.warning(self, "Error", "Las credenciales son incorrectas")

    def validate_login(self, email, password):
        # Placeholder login validation
        # Replace this with actual authentication logic
        return auth.iniciar_sesion(email,password)


class RegisterWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/registro.ui', self)

        # Connect the bottom label to switch to login window
        self.passwordLabel_2.mousePressEvent = self.switch_to_login

        # Connect the register button to register function
        self.aceptatButton.clicked.connect(self.perform_register)

    def switch_to_login(self, event):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

    def perform_register(self):
        email = self.emailInput.text()
        password = self.passwordInput.text()

        # Placeholder registration function
        register_result = self.validate_registration(email, password)

        if register_result:
            # If registration is successful, you would typically navigate to the login window or main application

            print("Registration successful!")
            self.login_window = LoginWindow()
            self.login_window.show()
            self.close()
        else:
            # Show error message if registration fails
            QMessageBox.warning(self, "Error", "Los datos son incorrectos")

    def validate_registration(self, email, password):
        # Placeholder registration validation
        # Replace this with actual registration logic
        # Example simple validation: email must contain @ and password must be at least 6 characters

        if '@' in email and len(password) >= 6:
            return auth.registrar_usuario(email, password)


def main():
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()