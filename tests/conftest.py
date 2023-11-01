import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    chrome_options = webdriver.ChromeOptions()

    if browser_name == "chrome":
        # Add Chrome options here
        chrome_options.add_argument("--start-maximized")  # Example: maximize the browser window
        request.driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        request.driver = webdriver.Firefox()
    elif browser_name == "Edge":
        request.driver = webdriver.Edge()

    request.driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = request.driver

    yield
    request.driver.close()
