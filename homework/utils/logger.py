import logging


class LoggerWrapper:
    def __init__(self):
        self._logger = logging.getLogger('homework')
        self._logger.setLevel(logging.DEBUG)

    def info(self, *args, **kwargs):
        self._logger.info(*args, **kwargs)

    def debug(self, *args, **kwargs):
        self._logger.debug(*args, **kwargs)

    def warning(self, *args, **kwargs):
        self._logger.warning(*args, **kwargs)

    def error(self, *args, **kwargs):
        self._logger.error(*args, **kwargs)
