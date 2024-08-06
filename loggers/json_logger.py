import json
import time
import traceback
import sys
import os

from loggers.rotation_logger import RotationLogger


class JsonLogger:
    def __init__(self,
                 file_log: str = None):
        if file_log is not None:
            self.__logger = RotationLogger.create_rotating_log(
                path_to_log_file=file_log,
                logger_name=os.path.basename(file_log).split('.')[0]
            )
        else:
            self.__logger = None

    def info(self,
             msg: str):
        dict_log = {
            "log_level": "INFO",
            "timestamp_ms": round(time.time() * 1000),
            "msg": msg,
        }
        log = json.dumps(obj=dict_log,
                         ensure_ascii=False)

        if self.__logger is not None:
            self.__logger.info(log)

        sys.stdout.write(f"{log}\n")

    def debug(self,
              msg: str):
        dict_log = {
            "log_level": "DEBUG",
            "timestamp_ms": round(time.time() * 1000),
            "msg": msg,
        }
        log = json.dumps(obj=dict_log,
                         ensure_ascii=False)
        # self.__logger.info(log)

        if self.__logger is not None:
            self.__logger.info(log)

        sys.stdout.write(f"{log}\n")

    def error(self,
              exc: Exception):
        dict_log = {
            "log_level": "ERROR",
            "timestamp_ms": round(time.time() * 1000),
            "error": repr(exc),
            "traceback_top": traceback.format_tb(exc.__traceback__)
        }
        log = json.dumps(obj=dict_log,
                         ensure_ascii=False)

        if self.__logger is not None:
            self.__logger.info(log)

        # self.__logger.info(log)
        sys.stderr.write(f"{log}\n")