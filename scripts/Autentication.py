import firebase_admin
from firebase_admin import credentials, auth
import pyrebase

# Paso 1: Configuración de credenciales de Firebase
# Descarga el archivo de configuración JSON desde la consola de Firebase

# Configuración de Pyrebase (librería adicional para autenticación)
config = {
    "apiKey": "AIzaSyDTjoAVrLiYZXmK5m2HvL6xb6dLkqeeyFw",
    "authDomain": "veterinaria-1188a.firebaseapp.com",
    "projectId": "veterinaria-1188a",
    "storageBucket": "veterinaria-1188a.firebasestorage.app",
    "messagingSenderId": "654216803356",
    "appId" : "1:654216803356:web:ad13cd7da22262e56b1bd9",
    "databaseURL": "https://veterinaria-1188a-default-rtdb.europe-west1.firebasedatabase.app/"
}

cred = credentials.Certificate("certs/veterinaria-1188a-firebase-adminsdk-fbsvc-88ed367b95.json")
firebase_admin.initialize_app(cred)
# Inicializar Pyrebase
pyrebase_config = pyrebase.initialize_app(config)
pb_auth = pyrebase_config.auth()

def registrar_usuario(email, password):
    """
    Registra un nuevo usuario con correo y contraseña
    """
    try:
        # Crear usuario con Firebase Admin SDK
        usuario = auth.create_user(
            email=email,
            password=password
        )
        print(f"Usuario registrado exitosamente. UID: {usuario.uid}")
        return usuario
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return None

def iniciar_sesion(email, password):
    """
    Inicia sesión con correo y contraseña
    """
    try:
        # Iniciar sesión con Pyrebase
        usuario = pb_auth.sign_in_with_email_and_password(email, password)
        token = usuario['idToken']
        print("Inicio de sesión exitoso")
        return token
    except Exception as e:
        print(f"Error al iniciar sesión: {e}")
        return None