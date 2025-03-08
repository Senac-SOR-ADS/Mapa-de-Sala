import bcrypt
from App.model.logger import logger_model

class Criptografia:
    TIPO_ENCODE = 'utf-8'

    # =================== criptografar Senha ===================
    @staticmethod
    def criptografarSenha(senha: str) -> bytes:
        """Criptografa a senha fornecida."""
        try:
            if not isinstance(senha, str):
                logger_model.error('Erro ao criptografar senha: Tipo inválido. Esperado str, recebido %s.', type(senha).__name__)
                raise ValueError('A senha deve ser uma string.')

            logger_model.debug('Iniciando processo de criptografia da senha. Convertendo para bytes.')
            senha_encoded = senha.encode(Criptografia.TIPO_ENCODE)

            logger_model.debug('Gerando hash da senha usando bcrypt.')
            senha_criptografada = bcrypt.hashpw(senha_encoded, bcrypt.gensalt())

            if not isinstance(senha_criptografada, bytes):
                logger_model.error('Erro ao gerar hash: resultado não é do tipo bytes.')
                raise ValueError('A senha criptografada não é válida.')

            logger_model.info('Senha criptografada com sucesso.')
            return senha_criptografada

        except ValueError as e:
            logger_model.error('Erro ao criptografar senha: %s.', str(e))
            raise
        except Exception as e:
            logger_model.error('Erro inesperado ao criptografar senha: %s.', str(e))
            raise

    # =================== validar Senha ===================
    @staticmethod
    def validarSenha(senha: str, senhaCriptografada: bytes) -> bool:
        """Valida se a senha fornecida corresponde à senha criptografada."""
        try:
            if not isinstance(senha, str) or not isinstance(senhaCriptografada, bytes):
                logger_model.error('Erro ao validar senha: Tipos inválidos. senha: %s, senhaCriptografada: %s.', 
                                   type(senha).__name__, type(senhaCriptografada).__name__)
                raise ValueError('Os parâmetros devem ser do tipo string e bytes, respectivamente.')

            logger_model.debug('Iniciando validação de senha. Convertendo senha para bytes.')
            senha_encoded = senha.encode(Criptografia.TIPO_ENCODE)

            logger_model.debug('Comparando senha fornecida com hash armazenado.')
            resultado = bcrypt.checkpw(senha_encoded, senhaCriptografada)

            if resultado:
                logger_model.info('Senha validada com sucesso.')
            else:
                logger_model.warning('Falha na validação: senha incorreta.')

            logger_model.debug('Finalizando validação de senha.')
            return resultado

        except ValueError as e:
            logger_model.error('Erro ao validar senha: %s.', str(e))
            raise
        except Exception as e:
            logger_model.error('Erro inesperado ao validar senha: %s.', str(e))
            raise

if __name__ == '__main__':
    pass
