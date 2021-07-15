from pytest_bdd import scenarios, given, when, then
from utilities.customLogger import LogGen

scenarios('../features/login.feature')

logger = LogGen.logGen()


@given('the user navigate to the URL')
def step_impl():
    logger.info("----------Open Browser----------")


@then('verify the title of the page')
def search_results(setup):
    logger.info("----------Verify Title----------")
    ack_title = setup.title
    logger.info(ack_title)
    print(ack_title)
    if ack_title == "Nory - Serving Up Success":
        assert True
    else:
        assert False


@then('user should able to login successfully')
def search_results():
    print('to Bigboss')


@when('the user enter the credentials for valid user')
def search_phrase():
    print('to Bigboss')
