from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
import pytest

from pageObject.CheckOutPage import CheckOut
from pageObject.ConfirmPage import ConfirmPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)  # object of HomePage
        checkout = CheckOut(self.driver)  # Object of CheckOut page
        confirmpage = ConfirmPage(self.driver) # Object of Confirm page
        log.info("Clicking the shop button")
        homepage.shopItems().click()  # click shop button
        log.info("Shop button is pressed")
        homepage.scrollTodown()  # scroll to down
        log.info("form is scrolled")
        AddToCart = homepage.addToCart()  # call add to cart page function on home page
        homepage.scrollToup()  # scroll to top
        homepage.homepage_Explicitlywait()  # call to explicit wait function
        log.info("Added to cart")
        for Adds in AddToCart:
            Adds.click()  # click all item
        chkout = checkout.checkOut()  # click checkout option
        log.info("Checkout")
        for chk in chkout:
            chk.click()

        chkBtn = checkout.checkOutsuccess()  # chekout success button
        for confirm in chkBtn:
            confirm.click()
        log.info("Checkout confirm button  is pressed")
        checkout.assertCheckouturl()
        log.info("assert current URL after checkout")# (assert  URL) of check out page is called
        checkout.countrySelect()   # search country
        log.info("Country is selected")
        checkout.webDriverwait().click()  # select country by name
        log.info("Wait for some time to select country")
        confirmpage.confirm_page().click()  # term & conition
        log.info("Term and condition is checked")
        confirmpage.purchase_option().click()  # purchase option
        log.info("Purchase option is clicked")
        confirmpage.book_order()
        log.info("Order is booked")
        success_mess = confirmpage.suc_message()
        log.info("Success message is displayed"+success_mess)
