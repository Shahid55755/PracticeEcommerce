import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        request.driver = webdriver.Chrome()
        #request.driver.get("https://rahulshettyacademy.com/angularpractice/")

    elif browser_name == "firefox":
        request.driver = webdriver.Firefox()

    elif browser_name == "Edge":
        request.driver = webdriver.Edge()

    request.driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.driver.maximize_window()
    request.cls.driver = request.driver

    yield
    request.driver.close()
