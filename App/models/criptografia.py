import bcrypt

class Criptografia:
    TIPO_ENCODE = 'utf-8'
    
    @classmethod
    def criptografar_senha(cls, senha: str) -> bytes:
        """Criptografa a senha que você passar para o método."""
        senha_encode = senha.encode(cls.TIPO_ENCODE)
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(senha_encode, salt)
    
    @classmethod
    def validar_senha(cls, senha: str, senha_criptografada: bytes) -> bool:
        """Valida se as senhas passadas são idênticas."""
        return bcrypt.checkpw(senha.encode(cls.TIPO_ENCODE), senha_criptografada)
