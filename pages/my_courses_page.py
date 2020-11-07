class MyCoursesPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _create_course_button = "//btn[@id='create-course']"

    # Actions
    def click_create_course_button(self):
        self.driver.find_element_by_xpath(self._create_course_button).click()
