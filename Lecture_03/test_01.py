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
    testpage.go_to_site()
    testpage.enter_login("GB20230583da03")
    testpage.enter_pass("55aae3d70d")
    testpage.click_login_btn()
    assert testpage.get_good_text() == "Hello, GB20230583da03"
