from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    termAndCond = (By.CSS_SELECTOR, "label[for*='checkbox2']")
    purchase = (By.CSS_SELECTOR, "input[class*='btn-success']")
    bookOrder = (By.CLASS_NAME, "alert-success")

    def confirm_page(self):
        return self.driver.find_element(*ConfirmPage.termAndCond)

    def purchase_option(self):
        print("testing change for github")
        print("testing change for github")
        return self.driver.find_element(*ConfirmPage.purchase)

    def book_order(self):
        return self.driver.find_element(*ConfirmPage.bookOrder)

    def suc_message(self):
        success = self.driver.find_element(*ConfirmPage.bookOrder)
        assert "Success! Thank you!" in success.text
        return success.text
