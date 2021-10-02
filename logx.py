import logging
from typing import Any

LOGGING_LEVEL = logging.DEBUG


def setup_logger(logger_name: str) -> Any:
    if not logger_name:
        logger_name = __name__

    logger = logging.getLogger(logger_name)
    logger.setLevel(LOGGING_LEVEL)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOGGING_LEVEL)
    logger.addHandler(console_handler)

    return logger
