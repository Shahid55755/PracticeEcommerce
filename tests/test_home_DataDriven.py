import time
import logging
import pytest
from openpyxl.utils import datetime
from selenium.webdriver.common.by import By

from pageObject.HomePage import HomePage
from testData.excelDemofile import HomePageData
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select
import openpyxl


class TestRegisterPageDataDriven(BaseClass):

    @pytest.fixture(params=HomePageData.gettestdata())
    def getdata(self, request):
        return request.param

    def test_newuser(self, getdata):
        try:
            log = self.getLogger()
            home_test = HomePage(self.driver)
            home_test.add_firstname().send_keys(getdata["Name"])
            log.info("Firstname is : " + getdata["Name"])
            home_test.add_email().send_keys(getdata["email"])
            log.info("Email is : " + getdata["email"])
            home_test.add_password().send_keys(getdata["password"])
            home_test.check_label().click()
            home_test.scrollTodown()
            home_test.select_gender()
            home_test.emp_status().click()

            home_test.date_of_birth().send_keys(getdata["dob"])
            log.info("DOB is : " + getdata["dob"])
            home_test.submit_form().click()
            message = home_test.verify_success()
            log.info(message)
            home_test.scrollToup()
            time.sleep(2)
            self.driver.refresh()
        except Exception as e:
            log = self.getLogger()
            log.error(f"error during the action {str(e)}")
            log.critical(f"Critical error {str(e)}")
            log.warning(f"Warning during the program {str(e)}")
