# Dashboard Class
# Verify the username

# Page Class
# Page Actions

from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, drier):
        self.driver=drier

    #   Page Locators
    user_logged_in = (By.XPATH, "//span[@data-qa='lufexuloga']")

    def get_user_logged_in(self):
        return self.driver.find_element(*DashboardPage.user_logged_in)

    #Page action

    def get_user_logged_in_text(self):
        return self.get_user_logged_in().text



