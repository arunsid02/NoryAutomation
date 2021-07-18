from pytest_bdd import scenarios, given, when, then
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

scenarios('../features/login.feature')

logger = LogGen.logGen()


@given('the user navigate to the URL')
def step_impl(setup):
    logger.info("----------Open Browser----------")


@then('verify the title of the page')
def search_results(setup):
    logger.info("----------Verify Title----------")
    driver = setup
    ack_title = driver.title
    logger.info(ack_title)
    print(ack_title)
    if ack_title == "Nory - Serving Up Success":
        assert True
    else:
        assert False


@then('user should able to login successfully')
def search_results(setup):
    logger.info("----------Verify Title----------")
    driver = setup
    ack_title = driver.title
    logger.info(ack_title)
    print(ack_title)
    if ack_title == "Nory - Serving Up Success":
        assert True
    else:
        assert False


@when('the user enter the credentials for valid user')
def search_phrase(setup):
    driver=setup
    lp = LoginPage(driver)
    lp.setUserName(ReadConfig.getusername())
    lp.setPassword(ReadConfig.getpassword())
    lp.clickLogin()
