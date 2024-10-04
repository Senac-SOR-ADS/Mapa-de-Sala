from flask_sqlalchemy import SQLAlchemy
from models.criptografia import Criptografia

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = Criptografia.criptografar_senha(password)

    def verificar_senha(self, password: str) -> bool:
        """Verifica se a senha fornecida está correta."""
        return Criptografia.validar_senha(password, self.password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }
