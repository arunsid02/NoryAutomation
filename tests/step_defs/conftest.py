from selenium import webdriver
import pytest
from utilities.readProperties import ReadConfig


@pytest.fixture
def setup():
    if ReadConfig.getBrowser() == 'chrome':
        driver = webdriver.Chrome(executable_path='Drivers/chromedriver')
    elif ReadConfig.getBrowser() == 'firefox':
        driver = webdriver.Firefox(executable_path='Drivers/chromedriver')
    else:
        print("specify browser name")
    driver.get(ReadConfig.getApplicationURL())
    return driver


def pytest_configure(config):
    config._metadata['Project Name'] = 'Nory Automation'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Arun Sidana'
