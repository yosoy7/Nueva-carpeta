from database.db import Database
import hashlib
import sqlite3

class Login:
    def __init__(self):
        self.db = Database()

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def authenticate(self, username: str, password: str) -> bool:
        try:
            cursor = self.db.conn.cursor()
            # First check if user exists
            cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            
            if result is None:
                print("Debug: Usuario no encontrado")
                return False
                
            stored_password = result[0]
            hashed_input_password = self.hash_password(password)
            
            if stored_password == hashed_input_password:
                return True
            else:
                print("Debug: Contraseña incorrecta")
                return False
                
        except sqlite3.Error as e:
            print(f"Debug: Error de base de datos: {e}")
            return False

    def test_connection(self):
        try:
            cursor = self.db.conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users")
            count = cursor.fetchone()[0]
            print(f"Debug: Número total de usuarios en la base de datos: {count}")
            return True
        except sqlite3.Error as e:
            print(f"Debug: Error al conectar con la base de datos: {e}")
            return False