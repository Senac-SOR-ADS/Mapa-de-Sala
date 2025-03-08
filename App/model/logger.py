import logging
import threading
import json
from pathlib import Path
from logging.handlers import RotatingFileHandler

class JSONFormatter(logging.Formatter):
    """Classe para formatar logs como JSON corretamente."""
    def __init__(self, datefmt="%d-%m-%Y %H:%M:%S"): super().__init__(datefmt=datefmt); self.datefmt = datefmt
    def format(self, record): return json.dumps({"time": self.formatTime(record, self.datefmt), "name": record.name, "level": record.levelname, "message": record.getMessage()}, ensure_ascii=False)

class Log:
    """Classe Singleton para configuração centralizada de logs."""
    _instances, _lock = {}, threading.Lock()
    SUCCESS = 25
    if "SUCCESS" not in logging._nameToLevel: logging.addLevelName(SUCCESS, "SUCCESS")

    def __new__(cls, name="basic", log_dir="env/log", log_console=False, json_format=False, level=logging.INFO):
        key = (name, log_console, json_format)
        with cls._lock:
            if key not in cls._instances:
                instance = super().__new__(cls)
                instance._initialize(name, log_dir, log_console, json_format, level)
                cls._instances[key] = instance
            return cls._instances[key]

    # =================== _initialize ===================
    def _initialize(self, name, log_dir, log_console, json_format, level):
        self.logger = logging.getLogger(name)
        if not self.logger.hasHandlers():
            self.logger.setLevel(level); self.logger.propagate = False
            self.log_dir = Path(log_dir); self.log_dir.mkdir(parents=True, exist_ok=True)
            self._configurar_file_handler(self.log_dir / f"{name}.log", json_format)
            if log_console: self._configurar_console_handler(json_format)
            setattr(self.logger, "success", lambda mensagem, *args: self.log(self.SUCCESS, mensagem, *args))

    # =================== _configurar_file_handler ===================
    def _configurar_file_handler(self, log_path, json_format):
        formatter = JSONFormatter() if json_format else logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%d-%m-%Y %H:%M:%S")
        file_handler = RotatingFileHandler(log_path, maxBytes=10 * 1024 * 1024, backupCount=5, encoding="utf-8")
        file_handler.setFormatter(formatter); self.logger.addHandler(file_handler)

    # =================== _configurar_console_handler ===================
    def _configurar_console_handler(self, json_format):
        formatter = JSONFormatter() if json_format else logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%d-%m-%Y %H:%M:%S")
        console_handler = logging.StreamHandler(); console_handler.setFormatter(formatter); self.logger.addHandler(console_handler)

    # =================== log ===================
    def log(self, level, mensagem, *args):
        nivel_log = logging._nameToLevel.get(level.upper()) if isinstance(level, str) else level
        if nivel_log is None: raise ValueError(f"Nível de log inválido: {level}")
        self.logger.log(nivel_log, mensagem, *args)

    # =================== set_level ===================
    def set_level(self, level):
        nivel_log = logging._nameToLevel.get(level.upper()) if isinstance(level, str) else level
        if nivel_log is None or not isinstance(nivel_log, int): raise ValueError("O nível de log deve ser um valor válido de logging")
        self.logger.setLevel(nivel_log)

    # =================== Métodos de Log ===================
    def debug(self, mensagem, *args): self.log(logging.DEBUG, mensagem, *args)
    def info(self, mensagem, *args): self.log(logging.INFO, mensagem, *args)
    def warning(self, mensagem, *args): self.log(logging.WARNING, mensagem, *args)
    def error(self, mensagem, *args): self.log(logging.ERROR, mensagem, *args)
    def critical(self, mensagem, *args): self.log(logging.CRITICAL, mensagem, *args)
    def success(self, mensagem, *args): self.log(self.SUCCESS, mensagem, *args)

# Criar instâncias com nível INFO temporário
log_instance = Log("MapadeSala-Web", log_console=False, json_format=False, level=logging.INFO)
logger = log_instance.logger
log_instance_conexao = Log("conexao", log_console=False, json_format=False, level=logging.INFO)
logger_conexao = log_instance_conexao.logger
log_instance_model = Log("model", log_console=False, json_format=False, level=logging.INFO)
logger_model = log_instance_model.logger

# --- Após a inicialização, ativamos outros níveis de log ---
log_instance.set_level(logging.DEBUG)
log_instance_conexao.set_level(logging.DEBUG)
log_instance_model.set_level(logging.DEBUG)
