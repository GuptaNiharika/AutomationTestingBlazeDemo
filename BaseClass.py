import inspect
import logging

class BaseClass:
    def getLogger(self):
        loggerName=inspect.stack()[1][3]
        logger = logging.getLogger(loggerName) #to get filename from which this method is called
        #logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logFile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)   #Debug, Info, Warning, Error, Critical
        return logger