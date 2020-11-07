from pages.create_course_page import CreateCoursePage
from pages.login_page import LoginPage
from pages.navigation_header_page import NavigationHeaderPage
from pages.my_courses_page import MyCoursesPage
from pages.course_page import CoursePage


def test_create_new_course_happy_path(chrome_browser):
    # Test Data
    email = "Test@email.com"
    password = "Password!"
    course_title = "TestCourse"
    subject_area = "Technology"
    course_level = "12"

    # Open Browser
    chrome_browser.get("https://app.schoology.com/login")
    chrome_browser.maximize_window()

    # Login
    login_page = LoginPage(chrome_browser)
    login_page.populate_username_field(email)
    login_page.populate_password_field(password)
    login_page.click_login_button()

    # Navigate to courses page
    navigation_header = NavigationHeaderPage(chrome_browser)
    navigation_header.verify_succesful_login()
    navigation_header.click_courses_header_button()
    navigation_header.click_my_courses_link()

    # Open create new course window
    my_courses = MyCoursesPage(chrome_browser)
    my_courses.click_create_course_button()

    # Create new course
    create_course = CreateCoursePage(chrome_browser)
        # Need to switch to create course frame?
    create_course.populate_course_name(course_title)
    create_course.select_subject_area(subject_area)
    create_course.select_level(course_level)
    create_course.click_grading_period_checkbox()

    # Verify course is created
    new_course = CoursePage(chrome_browser)
    result = new_course.verify_course_title(course_title)

    assert result






