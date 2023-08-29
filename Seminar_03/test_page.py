from base_app import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '''//*[@id="login"]/div[1]/label/input''')
    LOCATOR_PASS_FIELD = (By.XPATH, '''//*[@id="login"]/div[2]/label/input''')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, '''//*[@id="app"]/main/div/div/div[2]/h2''')
    
    LOCATOR_GOOD_FIELD = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[3]/a''')
    
    LOCATOR_CREATE_BTN = (By.CSS_SELECTOR, "#create-btn")
    LOCATOR_TITLE_FIELD = (By.XPATH, '''//*[@id="create-item"]/div/div/div[1]/div/label/input''')
    LOCATOR_DESCRIPTION_FIELD = (By.XPATH, '''//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea''')
    LOCATOR_CONTENT_FIELD = (By.XPATH, '''//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea''')
    LOCATOR_DATA_FIELD = (By.XPATH, '''//*[@id="create-item"]/div/div/div[5]/div/div/label/input''')
    LOCATOR_IMAGE_FIELD = (By.XPATH, '''//*[@id="create-item"]/div/div/div[6]/div/div/label/input''')
    LOCATOR_SEND_BTN = (By.CSS_SELECTOR, "div:nth-child(7) > div > button")
    LOCATOR_SEND_FIELD = (By.XPATH, '''//*[@id="app"]/main/div/div[1]/div/div[3]''')


class OperationsHelper(BasePage):
    
    def enter_login(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_btn(self):
        logging.info("Click login button...")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=4)
        text = error_field.text
        logging.info(f'We find text "{text}" in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text
    
    def get_good_text(self):
        good_field = self.find_element(TestSearchLocators.LOCATOR_GOOD_FIELD, time=4)
        text = good_field.text
        logging.info(f'We find text "{text}" in good field {TestSearchLocators.LOCATOR_GOOD_FIELD[1]}')
        return text
    
    def get_new_post(self):
        post_field = self.find_element(TestSearchLocators.LOCATOR_SEND_FIELD, time=4)
        text = post_field.text
        logging.info(f'We find text "{text}" in send field {TestSearchLocators.LOCATOR_SEND_FIELD[1]}')
        return text
    
    def click_create_btn(self):
        logging.info("Click create button...")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_BTN).click()
    
    def enter_title(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_TITLE_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    
    def enter_description(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_DESCRIPTION_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    
    def enter_content(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_CONTENT_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    
    def enter_data(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_DATA_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_DATA_FIELD)
        login_field.clear()
        login_field.send_keys(word)
    
    def enter_image(self, file):
        logging.info(f'Send "{file}" to element {TestSearchLocators.LOCATOR_IMAGE_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_IMAGE_FIELD)
        login_field.clear()
        login_field.send_keys(file)
    
    def click_send_btn(self):
        logging.info("Click send button...")
        self.find_element(TestSearchLocators.LOCATOR_SEND_BTN).click()
