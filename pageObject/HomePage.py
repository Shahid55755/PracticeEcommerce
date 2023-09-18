import selenium
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[contains(text(),'Shop')]")
    cart = (By.CLASS_NAME, "btn-info")
    firstname = (By.CSS_SELECTOR, "input[name='name'][minlength='2']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.ID, "exampleInputPassword1")
    label = (By.CSS_SELECTOR, "label[class='form-check-label'][for='exampleCheck1']")
    gender = (By.ID, "exampleFormControlSelect1")
    status = (By.CSS_SELECTOR, "label[class*='form-check-label'][for='inlineRadio2']")
    dob = (By.CSS_SELECTOR, "input[class$='form-control'][name='bday']")
    submit = (By.CSS_SELECTOR, "input[type='submit'][value='Submit']")
    success = (By.CLASS_NAME, "alert-success")


    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def addToCart(self):
        return self.driver.find_elements(*HomePage.cart)

    def scrollTodown(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scrollToup(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

    def homepage_Explicitlywait(self):
        self.driver.implicitly_wait(10)

    def add_firstname(self):
        return self.driver.find_element(*HomePage.firstname)

    def add_email(self):
        return self.driver.find_element(*HomePage.email)

    def add_password(self):
        return self.driver.find_element(*HomePage.password)

    def check_label(self):
        return self.driver.find_element(*HomePage.label)

    def select_gender(self):
        select = Select(self.driver.find_element(*HomePage.gender))
        return select.select_by_visible_text("Male")

    def emp_status(self):
        return self.driver.find_element(*HomePage.status)

    def date_of_birth(self):
        return self.driver.find_element(*HomePage.dob)

    def submit_form(self):
        #return self.driver.find_element(*HomePage.submit)
        element = self.driver.find_element(*HomePage.submit)
        color = element.value_of_css_property("color")  # get color of web element
        print(color)
        return element

    def verify_success(self):
        wait = WebDriverWait(self.driver, 20)
        success_message = wait.until(EC.visibility_of_element_located(HomePage.success))
        assert "Success! The Form has been submitted" in success_message.text
        return success_message.text




