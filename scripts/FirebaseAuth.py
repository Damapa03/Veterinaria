import firebase_admin
from firebase_admin import credentials, auth
import os

class FirebaseAuth:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FirebaseAuth, cls).__new__(cls)
            # Inicializa la conexión a Firebase (solo para autenticación)
            try:
                # Busca el archivo de credenciales en diferentes ubicaciones
                possible_paths = [
                    'serviceAccountKey.json',
                    os.path.join(os.path.dirname(__file__), 'serviceAccountKey.json'),
                    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'serviceAccountKey.json')
                ]
                
                cred_path = None
                for path in possible_paths:
                    if os.path.exists(path):
                        cred_path = path
                        break
                
                if cred_path is None:
                    raise FileNotFoundError("No se encontró el archivo de credenciales de Firebase")
                
                # Inicializar Firebase solo si no está ya inicializado
                if not firebase_admin._apps:
                    cred = credentials.Certificate(cred_path)
                    firebase_admin.initialize_app(cred)
                
                print("Conexión a Firebase Auth establecida correctamente")
            except Exception as e:
                print(f"Error al conectar con Firebase Auth: {e}")
        return cls._instance
    
    def verify_id_token(self, id_token):
        """Verifica un token de ID de Firebase"""
        try:
            decoded_token = auth.verify_id_token(id_token)
            return decoded_token
        except Exception as e:
            print(f"Error al verificar token: {e}")
            return None
    
    # Aquí puedes añadir más métodos de autenticación según necesites