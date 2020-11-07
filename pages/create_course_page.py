from selenium.webdriver.support.select import Select


class CreateCoursePage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _create_course_iframe = "//iframe[@id='create-course-iframe']"
    _course_name_field = "//btn[@id='create-course']"
    _subject_area_dropdown = "//select[id='subject-area']"
    _level_dropdown = "//select[id='level']"
    _grading_period_table = "//table[@id='grading-period']"
    _grading_period_checkbox = _grading_period_table + "//input[@type='checkbox']"
    _create_course_button = "//btn[@id=create-course']"
    # not worrying about advanced course options for happy path test

    # Actions
    def switch_to_create_course_frame(self):
        # Possibly not necessary
        frame = self.driver.find_element_by_xpath(self._create_course_iframe)
        self.driver.switch_to.frame(frame)

    def populate_course_name(self, course):
        self.driver.find_element_by_xpath(self._course_name_field).send_keys(course)

    def select_subject_area(self, subject):
        sel = Select(self.driver.find_element_by_xpath(self._subject_area_dropdown))
        sel.select_by_visible_text(subject)

    def select_level(self, level):
        sel = Select(self.driver.find_element_by_xpath(self._level_dropdown))
        sel.select_by_visible_text(level)

    def click_grading_period_checkbox(self):
        self.driver.find_element_by_xpath(self._grading_period_checkbox).click()

    def click_create_course_button(self):
        self.driver.find_element_by_xpath(self._create_course_button).click()






