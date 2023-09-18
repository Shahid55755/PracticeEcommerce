from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BaseClass import BaseClass


class CheckOut(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    checkOutButton = (By.CLASS_NAME, "btn-primary")
    confirmCheckout = (By.CSS_SELECTOR, "button[class='btn btn-success']")
    selectCountry = (By.ID, "country")
    selectCountryName = (By.XPATH, "//a[text()='Indonesia']")

    def checkOut(self):
        return self.driver.find_elements(*CheckOut.checkOutButton)

    def checkOutsuccess(self):
        return self.driver.find_elements(*CheckOut.confirmCheckout)

    def assertCheckouturl(self):
        assert "https://rahulshettyacademy.com/angularpractice/shop" == self.driver.current_url

    def countrySelect(self):
        return self.driver.find_element(*CheckOut.selectCountry).send_keys("ind")

    def webDriverwait(self):
        wait = WebDriverWait(self.driver, 20)  #
        return wait.until(EC.presence_of_element_located(CheckOut.selectCountryName))
