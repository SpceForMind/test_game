import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path


class RotationLogger:
    @staticmethod
    def create_rotating_log(path_to_log_file: str,
                            logger_name: str = __name__,
                            max_bytes: int = 15000000,
                            backup_count: int = 1) -> logging.Logger:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        Path(os.path.dirname(path_to_log_file)).mkdir(parents=True, exist_ok=True)

        if not os.path.exists(path_to_log_file):
            with open(path_to_log_file, 'a'):
                pass

        handler = RotatingFileHandler(path_to_log_file, maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(fmt=formatter)

        logger.addHandler(handler)

        return logger
