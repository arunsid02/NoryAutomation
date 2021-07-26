from selenium import webdriver
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

logger = LogGen.log_gen()


@pytest.fixture
def setup():
    logger.info("------browser is chrome-----")
    if ReadConfig.get_browser() == 'chrome':
        driver = webdriver.Chrome(executable_path='Drivers/chromedriver')
    elif ReadConfig.get_browser() == 'firefox':
        driver = webdriver.Firefox(executable_path='Drivers/chromedriver')
    else:
        print("specify browser name")
    driver.get(ReadConfig.get_application_url())
    return driver
