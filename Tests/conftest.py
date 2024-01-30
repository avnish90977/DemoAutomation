import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_option", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser_option")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        #options.add_argument("Headless")
        options.add_experimental_option("detach", True)
        serv_obj = Service()
        driver = webdriver.Chrome(options=options, service=serv_obj)
        driver.implicitly_wait(5)

    elif browser == "Edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        serv_obj = Service()
        driver = webdriver.Edge(options=options, service=serv_obj)
        driver.implicitly_wait(5)

    elif browser == "Firefox":
        options = webdriver.FirefoxOptions()
        #options.add_experimental_option("detach", True)
        serv_obj = Service()
        driver = webdriver.Firefox(options=options, service=serv_obj)
        driver.implicitly_wait(5)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

