from pytest_bdd import scenarios, given, when, then, parsers
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants
logging.basicConfig(filename='test.log', level=logging.INFO)

# Scenarios

scenarios('../features/test.feature')

polly = "panda"


@given('the DuckDuckGo home page is displayed')
def step_impl(setup):

    logging.info("Home page")


# When Steps

@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase():
    print('to Bigboss')


# Then Steps

@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(phrase):
    logging.info(phrase)
    assert polly == phrase
