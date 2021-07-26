import logging


class LogGen:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename='automation.log',
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

        # logging.basicConfig(filename="Logs/app.log", level=logging.INFO)
        #
        # stream_handler = logging.StreamHandler(sys.stderr)
        # stream_handler.setFormatter(logging.Formatter(fmt='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %('
        #                                                   'message)s', datefmt='%m-%d %H:%M'))
        # logger = logging.getLogger()
        # logger.addHandler(stream_handler)
        # return logger
