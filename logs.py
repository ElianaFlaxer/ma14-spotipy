import os
import logging


def activate_system_logs():
    path = os.environ.get('LOGS_PATH')
    format = '%(asctime)s | %(levelname)s - %(message)s'
    datefmt = '%d-%b-%y %H:%M:%S'
    logging.basicConfig(filename=path, filemode='w', format=format, datefmt=datefmt)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    stream = logging.StreamHandler()
    stream.setLevel(logging.WARNING)
    streamformat = logging.Formatter(format, datefmt)
    stream.setFormatter(streamformat)
    logger.addHandler(stream)
    return logging
