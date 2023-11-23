from BaseApp import BasePage
from selenium.webdriver.common.by import By


class SeacrhLocators:
    LOCATOR_EMAIL_FIELD = (By.ID, "loginEmail")
    LOCATOR_PASS_FIELD = (By.XPATH, "//input[@type='password']")
    LOCATOR_LOGIN_BUTTON = (By.CSS_SELECTOR, ".uk-button")
    LOCATOR_MAIN_TITLE = (By.TAG_NAME, "h3")
    LOCATOR_VARIANT_BUTTON = (By.ID, "menuMore")
    LOCATOR_VARIANT_TITLE = (By.CLASS_NAME, "uk-card-title")
    LOCATOR_AUTH_BUTTON = (By.ID, "menuAuth")
    LOCATOR_AUTH_TITLE = (By.CLASS_NAME, "uk-legend")
    LOCATOR_USERS_BUTTON = (By.ID, "menuUsersOpener")
    LOCATOR_ADD_BUTTON = (By.ID, "addUser")
    LOCATOR_TABLES_BUTTON = (By.ID, "menuUsers")
    LOCATOR_USERS_TABLE = (By.ID, "dataTable")
    LOCATOR_ADD_EMAIL = (By.ID, "dataEmail")
    LOCATOR_ADD_PASS = (By.ID, "dataPassword")
    LOCATOR_ADD_NAME = (By.ID, "dataName")
    LOCATOR_SUBMIT_BUTTON = (By.ID, "dataSend")
    LOCATOR_EMPTY_EMAIL_ERROR = (By.ID, "emailFormatError")
    LOCATOR_PASS_ERROR = (By.ID, "blankPasswordError")
    LOCATOR_NAME_ERROR = (By.ID, "blankNameError")
    LOCATOR_OK = (By.CLASS_NAME, "uk-modal-close")


class SearchHelper(BasePage):

    def login(self):
        email_field = self.find_element(SeacrhLocators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys("test@protei.ru")
        pass_field = self.find_element(SeacrhLocators.LOCATOR_PASS_FIELD)
        pass_field.send_keys("test")
        return self.find_element(SeacrhLocators.LOCATOR_LOGIN_BUTTON, time=2).click()

    def add_user(self, email, password, name):
        email_field = self.find_element(SeacrhLocators.LOCATOR_ADD_EMAIL)
        email_field.send_keys(email)
        pass_field = self.find_element(SeacrhLocators.LOCATOR_ADD_PASS)
        pass_field.send_keys(password)
        name_field = self.find_element(SeacrhLocators.LOCATOR_ADD_NAME)
        name_field.send_keys(name)
        return self.find_element(SeacrhLocators.LOCATOR_SUBMIT_BUTTON, time=2).click()

    def check_main_title(self):
        main_title = self.find_element(SeacrhLocators.LOCATOR_MAIN_TITLE,time=2)
        return main_title

    def open_variant_page(self):
        return self.find_element(SeacrhLocators.LOCATOR_VARIANT_BUTTON, time=2).click()

    def open_auth_page(self):
        return self.find_element(SeacrhLocators.LOCATOR_AUTH_BUTTON, time=2).click()

    def open_users_page(self):
        self.find_element(SeacrhLocators.LOCATOR_USERS_BUTTON, time=2).click()
        return self.find_element(SeacrhLocators.LOCATOR_TABLES_BUTTON, time=2).click()

    def open_add_page(self):
        return self.find_element(SeacrhLocators.LOCATOR_ADD_BUTTON, time=2).click()

    def check_variant_title(self):
        variant_title = self.find_element(SeacrhLocators.LOCATOR_VARIANT_TITLE, time=2)
        return variant_title

    def check_auth_title(self):
        auth_title = self.find_element(SeacrhLocators.LOCATOR_AUTH_TITLE, time=2)
        return auth_title

    def check_users_table(self):
        auth_title = self.find_element(SeacrhLocators.LOCATOR_USERS_TABLE, time=2)
        return auth_title

    def check_user_in_table(self, email, name):
        user = self.find_element((By.XPATH, '//tr[descendant::td[text()="' + email + '"] and descendant::td[text()="' + name + '"]]'), time=2)
        return user

    def check_empty_email_error_title(self):
        email_title = self.find_element(SeacrhLocators.LOCATOR_EMPTY_EMAIL_ERROR,time=2)
        return email_title

    def check_pass_error_title(self):
        pass_title = self.find_element(SeacrhLocators.LOCATOR_PASS_ERROR,time=2)
        return pass_title

    def check_name_error_title(self):
        name_title = self.find_element(SeacrhLocators.LOCATOR_NAME_ERROR,time=2)
        return name_title

    def ok(self):
        return self.find_element(SeacrhLocators.LOCATOR_OK, time=2).click()
