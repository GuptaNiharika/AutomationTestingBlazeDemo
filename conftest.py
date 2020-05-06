import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def test_launchWebPage(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        driver = webdriver.Chrome(executable_path="C:\\niharika\\broadcom project\\selenium learn\\chromedriver.exe")
    elif browser_name=="firefox":
        driver = webdriver.Firefox(executable_path="C:\\niharika\\broadcom project\\selenium learn\\geckodriver.exe")
    driver.get("http://www.blazedemo.com/")
    request.cls.driver = driver

@pytest.fixture()
def dataload():
    return ["http://www.blazedemo.com/","niharika"]


