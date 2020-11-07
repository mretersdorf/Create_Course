class CoursePage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _course_title = "//div[@id='course-title']"

    # Actions
    def verify_course_title(self, course):
        title = self.driver.find_element_by_xpath(self._course_title).text
        if title == course:
            return True
        else:
            return False
