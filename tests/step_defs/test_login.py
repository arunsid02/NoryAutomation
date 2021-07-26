from pytest_bdd import scenarios, given, when, then
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


scenarios('../features/login.feature')

logger = LogGen.log_gen()


@given('the user navigate to the URL')
def navigate_to_url(setup):
    logger.info("----------Open Browser----------")


@then('verify the title of the page')
def verify_title(setup):
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
def verify_login(setup):
    logger.info("----------Login Successful----------")
    driver = setup
    ack_title = driver.title
    logger.info(ack_title)
    print(ack_title)
    if ack_title == "Nory - Serving Up Success":
        assert True
    else:
        assert False

@when('the user enter the credentials for valid user')
def enter_login_details(setup):
    logger.info("----------Enter Credentials----------")
    driver=setup
    lp = LoginPage(driver)
    lp.locate_username(ReadConfig.get_username())
    lp.locate_password(ReadConfig.get_password())
    lp.locate_login()


@then('user click on logout button')
def verify_login(setup):
    logger.info("----------clicked on logout----------")
    driver = setup
    driver.implicitly_wait(10)
    lp = LoginPage(driver)
    lp.locate_logout_1()
    lp.locate_logout_2()


@then('user should be able to logout successfully')
def verify_login(setup):
    logger.info("----------Logout Successful----------")
    driver = setup
    ack_title = driver.title
    logger.info(ack_title)
    print(ack_title)
    if ack_title == "Nory - Serving Up Success":
        assert True
    else:
        assert False


@when('user click on forgot password link')
def verify_login(setup):
    logger.info("----------clicked on forgot password----------")
    driver = setup
    lp = LoginPage(driver)
    lp.locate_forgot_password()


@then('user click on reset button')
def verify_login(setup):
    logger.info("----------clicked on reset button----------")
    driver = setup
    lp = LoginPage(driver)
    lp.locate_reset_password()


@then('user enter the email address to reset the password')
def enter_login_details(setup):
    logger.info("----------Enter EmailId for reset password----------")
    driver=setup
    lp = LoginPage(driver)
    lp.locate_username(ReadConfig.get_username())


@then('Email should be sent to user')
def enter_login_details():
    logger.info("----------Sent Email to user---------")