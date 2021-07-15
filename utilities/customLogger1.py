import logging
import logging.handlers
from logging.handlers import SysLogHandler
from logging import Formatter


class LogGen:

    @staticmethod
    def logGen():
        logger = logging.getLogger('BetterLogger')

        logger.setLevel(logging.INFO)

        handler = SysLogHandler(facility=SysLogHandler.LOG_DAEMON, address='Logs/dev.log')

        logger.addHandler(handler)

        log_format = '[%(levelname)s] %(filename)s:%(funcName)s:%(lineno)d \"%(message)s\"'

        handler.setFormatter(Formatter(fmt=log_format))

        return logger
