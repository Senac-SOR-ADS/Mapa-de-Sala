from flask_sqlalchemy import SQLAlchemy
from models.criptografia import Criptografia
from models.usuario import Usuario

db = SQLAlchemy()

class Login(db.Model):
    __tablename__ = 'login'
    idLogin = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.LargeBinary, nullable=False)

    usuario = db.relationship('Usuario', backref=db.backref('logins', lazy=True))

    def __init__(self, email, senha):
        self.email = email
        self.senha = Criptografia.criptografar_senha(senha)

    def to_dict(self):
        return {
            "idLogin": self.idLogin,
            "idUsuario": self.idUsuario,
            "email": self.email,
            "senha": self.senha
        }

    @classmethod
    def validar_login(cls, email, senha):
        """Valida o login com base no email e senha fornecidos."""
        usuario = cls.query.filter_by(email=email).first()
        if usuario and Criptografia.validar_senha(senha, usuario.senha):
            return usuario
        return None
