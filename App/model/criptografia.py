import bcrypt


class Criptografia:
    TIPO_ENCODE = 'utf-8'
    
    @classmethod
    def criptografarSenha(cls, senha: str)->bytes:
        """Criptografa a senha que você passar para o método"""
        senhaEncode = senha.encode(cls.TIPO_ENCODE)
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(senhaEncode, salt)
    
    @classmethod
    def validarSenha(cls, senha: str, senhaCriptografada: bytes):
        """Valida se as senhas passadas são identicas"""
        if bcrypt.checkpw(senha.encode(cls.TIPO_ENCODE), senhaCriptografada):
            print('Senhas identicas!')
            return True
        else:
            print('Senhas não são iguais!')
            return False
        
if __name__ == '__main__':
    pass