from pytest_bdd import scenarios, given, when, then, parsers
from utilities.customLogger import LogGen
# Scenarios

scenarios('../features/test.feature')

logger = LogGen.log_gen()

polly = "panda"


@given('the DuckDuckGo home page is displayed')
def step_impl():

    logger.info("---------Test Home Page----------")


# When Steps

@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(phrase):
    logger.info("---------phrase= ----------"+phrase)


# Then Steps

@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(phrase):
    assert polly == phrase
    logger.info("polly is like phrase")
