import configparser

config = configparser.RawConfigParser()

try:
    config.read('Configuration/config.ini')
except Exception as e:
    print(str(e))

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def getBrowser():
        browser = config.get('commonInfo', 'browser')
        return browser
