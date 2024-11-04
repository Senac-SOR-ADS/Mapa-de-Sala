import bcrypt

class Criptografia:
    TIPO_ENCODE = 'utf-8'
    
    @classmethod
    def criptografarSenha(cls, senha: str) -> bytes:
        """Criptografa a senha fornecida e retorna o hash gerado."""
        senha_codificada = senha.encode(cls.TIPO_ENCODE)
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(senha_codificada, salt)
    
    @classmethod
    def validarSenha(cls, senha: str, senha_criptografada: bytes) -> bool:
        """Valida se a senha fornecida corresponde à senha criptografada."""
        senha_codificada = senha.encode(cls.TIPO_ENCODE)
        if bcrypt.checkpw(senha_codificada, senha_criptografada):
            print('Senhas idênticas!')
            return True
        else:
            print('Senhas não são iguais!')
            return False
        
if __name__ == '__main__':
    pass
