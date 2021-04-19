import logging

class LogGen:

    @staticmethod
    def logGen():
        logging.basicConfig(filename=".//Logs//automation.log",
                            format="%(asctime)s: %(levelname)s: %(messagae)s", datefmt="%m%d%y %I:%M:%S %p")

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger