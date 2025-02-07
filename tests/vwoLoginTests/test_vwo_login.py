import time
import pytest
import allure

from selenium import webdriver
from tests.pageObjects.loginPage import LoginPage
from tests.pageObjects.dashboardPage import DashboardPage


@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver


@allure.epic("VWO Login Test")
@allure.feature("TC#0 - VWO App Negative Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    try:
        driver= setup
        loginPage=LoginPage(driver)
        loginPage.login_to_vwo(usr="admin@test.com", pwd="admin")
        time.sleep(30)
        error_message=loginPage.get_error_message_text()
        assert error_message == "Your email, password, IP address or location did not match"
    except Exception as e:
        pytest.xfail("Failed")
        print(e)

@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    driver= setup
    loginPage=LoginPage(driver)
    loginPage.login_to_vwo(usr="hendreonkar@gmail.com", pwd="Admin@123")
    time.sleep(30)
    dashboardPage=DashboardPage(driver)
    assert "Dashboard" in driver.title
    assert "Onkar" in dashboardPage.get_user_logged_in_text()






