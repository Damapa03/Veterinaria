import firebase_admin
from firebase_admin import credentials, firestore

class FirebaseDAO:
    def __init__(self, cred_path: str):
        """Inicializa la conexión con Firebase Firestore."""
        self.cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
    
    def agregar_documento(self, collection: str, data: dict):
        """Agrega un documento a una colección."""
        doc_ref = self.db.collection(collection).add(data)
        return doc_ref
    
    def obtener_documento(self, collection: str, doc_id: str):
        """Obtiene un documento por su ID."""
        doc = self.db.collection(collection).document(doc_id).get()
        return doc.to_dict() if doc.exists else None
    
    def actualizar_documento(self, collection: str, doc_id: str, data: dict):
        """Actualiza un documento existente."""
        self.db.collection(collection).document(doc_id).update(data)
    
    def eliminar_documento(self, collection: str, doc_id: str):
        """Elimina un documento por su ID."""
        self.db.collection(collection).document(doc_id).delete()
    
    def obtener_todos(self, collection: str):
        """Obtiene todos los documentos de una colección."""
        docs = self.db.collection(collection).stream()
        return {doc.id: doc.to_dict() for doc in docs}

# Uso:
# dao = FirebaseDAO('ruta/a/credenciales.json')
# dao.agregar_documento('usuarios', {'nombre': 'Juan', 'edad': 30})
