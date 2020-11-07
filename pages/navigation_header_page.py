class NavigationHeaderPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators (stubbed due to no access)
    _header_user_name = "//class[@id='header-name']"
    _header_courses_button = "//class[@id='header-courses']"
    _courses_my_courses_link = "//class[@id='my-courses']"

    # Actions
    def verify_succesful_login(self):
        self.driver.find_element_by_xpath(self._header_user_name).is_displayed()

    def click_courses_header_button(self):
        self.driver.find_element_by_xpath(self._header_courses_button).click()

    def click_my_courses_link(self):
        self.driver.find_element_by_xpath(self._courses_my_courses_link).click()
