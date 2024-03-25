from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler

class Log:
    def __init__(self, log_path: Path, log_name: str) -> None:
        fmt ='%(asctime)s -%(name)s -%(levelname)s -%(filename)s -%(lineno)d -%(message)s ' 
        log_formate = logging.Formatter(fmt)

        self.log_path = log_path
        self.log_path.mkdir(parents=True, exist_ok=True)
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel('DEBUG')

        stream_handle = logging.StreamHandler()
        stream_handle.setLevel('DEBUG')
        stream_handle.setFormatter(log_formate)

        file_handler = RotatingFileHandler(log_path / log_name, maxBytes=20*1024*1024, backupCount=1000, encoding='UTF-8')
        file_handler.setLevel('INFO')
        file_handler.setFormatter(log_formate)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handle)
