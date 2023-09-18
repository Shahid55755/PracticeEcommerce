# import fileHandler
import inspect

from selenium import webdriver
import pytest
from selenium.webdriver.common.service import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
#import FileHandler


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        # to get the name of the test case file name at runtime
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        # FileHandler class to set the location of log file
        # filehandler = logging.FileHandler('logfile.log')
        filehandler = logging.FileHandler(r'C:\Users\HP\PycharmProjects\SeleniumFramework\utilities\logfile.log')

        # Formatter class to set the format of log file
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        # object of FileHandler gets formatting info from setFormatter #method
        filehandler.setFormatter(formatter)
        # logger object gets formatting, path of log file info with addHandler #method
        logger.addHandler(filehandler)
        # setting logging level to INFO
        logger.setLevel(logging.INFO)
        return logger
