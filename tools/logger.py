import logging


def get_logger(name: str) -> logging.Logger:
    # create logger and set level
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # handler for writing in console
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # format message
    formater = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formater)

    logger.addHandler(handler)

    return logger
