class LoginPage:
    textbox_username_id = "email"
    textbox_password_id = "password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    button_logout_1 = "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/button[1]"
    button_logout_2 = "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]"
    forgot_password_link = "//div[contains(text(),'Forgot Password?')]"
    reset_password_link = "//button[contains(text(),'Reset')]"

    def __init__(self, driver):
        self.driver = driver

    def locate_username(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def locate_password(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def locate_login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def locate_logout_1(self):
        self.driver.find_element_by_xpath(self.button_logout_1).click()

    def locate_logout_2(self):
        self.driver.find_element_by_xpath(self.button_logout_2).click()

    def locate_forgot_password(self):
        self.driver.find_element_by_xpath(self.forgot_password_link).click()

    def locate_reset_password(self):
        self.driver.find_element_by_xpath(self.reset_password_link).click()
