import time
import logging
import pytest
from selenium.webdriver.common.by import By

from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select


class TestRegisterPage(BaseClass):
    @pytest.fixture(params=[("shahidali", "shahd.bit@y.com", "45454", "01/02/2023"),
                            ("sadiq", "sadiq.bit@y.com", "45454", "01/02/2023"),
                            ("shahidali", "shahd.bit@y.com", "45454", "01/02/2023"),
                            ])
    def getData(self, request):
        return request.param

    def test_register(self, getData):
        try:
            log = self.getLogger()
            home_test = HomePage(self.driver)
            home_test.add_firstname().send_keys(getData[0])
            log.info("Firstname is : "+getData[0])
            home_test.add_email().send_keys(getData[1])
            log.info("Email is : " + getData[1])
            home_test.add_password().send_keys(getData[2])
            home_test.check_label().click()
            home_test.scrollTodown()
            home_test.select_gender()
            home_test.emp_status().click()
            home_test.date_of_birth().send_keys(getData[3])
            log.info("DOB is : " + getData[3])
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

