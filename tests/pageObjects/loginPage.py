# Login Page Class

# Responsibility ->
# get username and send keys - email
# # get password and send keys - email
# # click the submit button and navigate to dashboard Page
# Invalid -> error message
# Forgot password


# Page Class

# Page Locators
# Page Actions
# WebDriver Init
# Custom Functions
# No assertions(in Page Object Class)

from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver= driver

    # Page locators
    username= (By.ID, "login-username")
    password= (By.NAME, "password")
    submit_button= (By.XPATH, "//button[@id='js-login-btn']")
    error_message= (By.XPATH, "//*[@id='js-notification-box-msg']")
    #forgot_password= (By.XPATH, "//button[normalize-space()='Forgot Password?']")
    free_trial= (By.XPATH, "//a[normalize-space()='Start a free trial']")
    #remember_checkbox = (By.XPATH, "//label[@for='checkbox-remember']//span[@class='checkbox-radio-button ng-scope']//*[name()='svg']")
    #sso_login = (By.XPATH, "//button[normalize-space()='Sign in using SSO']")

    # Page Actions
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    def get_free_trial(self):
        return self.driver.find_element(*LoginPage.free_trial)

    # Page Action - Main Action

    def login_to_vwo(self,usr,pwd):
        self.get_username().send_keys(usr)
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()

    #def login_to_vwo(self,usr,pwd,iserror):
    #    if iserror is True:
    #        self.get_username().send_keys("wrong")
    #        self.get_password().send_keys("wrong")
    #       self.get_submit_button().click()

    def get_error_message_text(self):
        return self.get_error_message().text

    def click_free_trial(self):
        self.get_free_trial().click()





