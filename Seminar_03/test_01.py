from test_page import OperationsHelper
import logging


def test_step_1_bad_login(browser):
    logging.info("Test_01 Starting...")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_btn()
    assert testpage.get_error_text() == "401"


def test_step_2_good_login(browser):
    logging.info("Test_02 Starting...")
    testpage = OperationsHelper(browser)
    testpage.enter_login("Ivan1234")
    testpage.enter_pass("416b69ce0b")
    testpage.click_login_btn()
    assert testpage.get_good_text() == "Hello, Ivan1234"


def test_step_3_new_post(browser):
    logging.info("Test_03 Starting...")
    testpage = OperationsHelper(browser)
    testpage.click_create_btn()
    testpage.enter_title("Test")
    testpage.enter_description("Test")
    testpage.enter_content("Test")
    testpage.enter_data("28.08.2023")
    Imagepath = """D:\\OneDrive\\Рабочий стол\\1234.jpg"""
    testpage.enter_image(Imagepath)
    testpage.click_send_btn()
    assert testpage.get_new_post() == "Test"
