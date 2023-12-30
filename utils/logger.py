import logging
import time

creation_time = time.strftime('%Y%m%d_%H%M%S')


def createLogger(name: str, log_level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    file_path = f'logs/log_{creation_time}.log'
    formatter = logging.Formatter('%(asctime)s | %(levelname)-5s | %(name)-15s | %(message)s')
    handlers = [logging.FileHandler(file_path), logging.StreamHandler()]
    for handler in handlers:
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
