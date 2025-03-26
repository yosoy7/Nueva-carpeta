import hashlib
from database.db import Database
from models.user import User

class Registration:
    def __init__(self):
        self.db = Database()

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username: str, email: str, password: str) -> bool:
        try:
            cursor = self.db.conn.cursor()
            hashed_password = self.hash_password(password)
            
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, hashed_password)
            )
            self.db.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False