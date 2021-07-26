import configparser

config = configparser.RawConfigParser()


config.read('Configuration/config.ini')


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def get_browser():
        browser = config.get('commonInfo', 'browser')
        return browser

    @staticmethod
    def get_username():
        username = config.get('commonInfo', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('commonInfo', 'password')
        return password
