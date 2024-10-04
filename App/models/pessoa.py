from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Pessoa(db.Model):
    __tablename__ = 'pessoa'
    
    idPessoa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    CPF_CNPJ = db.Column(db.String(18), nullable=False)
    nascimento = db.Column(db.Date, nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)

    def __init__(self, nome: str, cpf_cnpj: str, nascimento: str, telefone: str, email: str, cargo: str) -> None:
        self.nome = nome
        self.CPF_CNPJ = cpf_cnpj
        self.nascimento = datetime.strptime(nascimento, '%Y-%m-%d').date()
        self.telefone = telefone
        self.email = email
        self.cargo = cargo

    def to_dict(self) -> dict:
        """Converte a instância para um dicionário."""
        return {
            "idPessoa": self.idPessoa,
            "nome": self.nome,
            "CPF_CNPJ": self.CPF_CNPJ,
            "nascimento": str(self.nascimento),
            "telefone": self.telefone,
            "email": self.email,
            "cargo": self.cargo
        }

    @classmethod
    def cadastrar(cls, nome: str, cpf_cnpj: str, nascimento: str, telefone: str, email: str, cargo: str) -> 'Pessoa':
        """Cadastra uma nova pessoa no banco de dados."""
        nova_pessoa = cls(nome, cpf_cnpj, nascimento, telefone, email, cargo)
        try:
            db.session.add(nova_pessoa)
            db.session.commit()
            return nova_pessoa
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao cadastrar: {e}")
            return None
