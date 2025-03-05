import firebase_admin
from firebase_admin import credentials, auth
import pyrebase

# Paso 1: Configuración de credenciales de Firebase
# Descarga el archivo de configuración JSON desde la consola de Firebase
cred = credentials.Certificate("certs/veterinaria-1188a-firebase-adminsdk-fbsvc-88ed367b95.json")
firebase_admin.initialize_app(cred)

# Configuración de Pyrebase (librería adicional para autenticación)
config = {
    "apiKey": "AIzaSyDTjoAVrLiYZXmK5m2HvL6xb6dLkqeeyFw",
  "authDomain": "veterinaria-1188a.firebaseapp.com",
  "projectId": "veterinaria-1188a",
  "storageBucket": "veterinaria-1188a.firebasestorage.app",
  "messagingSenderId": "654216803356",
  "appId" : "1:654216803356:web:ad13cd7da22262e56b1bd9",
  "measurementId": "G-V857EBJKYC"
}

# Inicializar Pyrebase
pyrebase_firebase = pyrebase.initialize_app(config)
auth_pyrebase = pyrebase_firebase.auth()

# Función para registrar un nuevo usuario
def registrar_usuario(email, password):
    try:
        # Método de Firebase Admin SDK
        usuario = auth.create_user(
            email=email,
            password=password
        )
        print(f"Usuario creado con éxito. UID: {usuario.uid}")
        return usuario
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        return None

# Función para iniciar sesión
def iniciar_sesion(email, password):
    try:
        # Método de Pyrebase
        usuario = auth_pyrebase.sign_in_with_email_and_password(email, password)
        
        # Obtener token de Firebase Admin SDK
        token = auth.verify_id_token(usuario['idToken'])
        
        print("Inicio de sesión exitoso")
        return token
    except Exception as e:
        print(f"Error al iniciar sesión: {e}")
        return None

# Función para restablecer contraseña
def restablecer_contrasena(email):
    try:
        auth.generate_password_reset_link(email)
        print("Enlace de restablecimiento de contraseña enviado")
    except Exception as e:
        print(f"Error al enviar enlace de restablecimiento: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    # Registro de usuario
    nuevo_usuario = registrar_usuario("ejemplo@correo.com", "contraseña123")
    
    # Inicio de sesión
    token_sesion = iniciar_sesion("ejemplo@correo.com", "contraseña123")
    
    # Restablecer contraseña
    restablecer_contrasena("damapa2003@gmail.com")