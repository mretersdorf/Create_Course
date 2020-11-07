class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _username_field = "//input[@id='edit-mail']"
    _password_field = "//input[@id='edit-pass']"
    _login_button = "//input[@id='edit-submit']"

    # Actions
    def populate_username_field(self, username):
        self.driver.find_element_by_xpath(self._username_field).send_keys(username)

    def populate_password_field(self, password):
        self.driver.find_element_by_xpath(self._password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(self._login_button).click()

