from selenium import webdriver
import pytest
import allure
import moment
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import Utils as utils

@pytest.mark.usefixtures("test_setup")      # will check conftest and check for function
class TestLogin():


    # def test_login(self,test_setup):      # do not need test_setup here if called from conftest, same for test_logout below
    def test_login(self):
        driver = self.driver        # called from conftest
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

        # driver.find_element_by_id("txtUsername").send_keys("Admin")
        # driver.find_element_by_id("txtPassword").send_keys("admin123")
        # driver.find_element_by_id("btnLogin").click()


    def test_logout(self):
        try:
            driver = self.driver

            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()

            x = driver.title
            assert x == "OrangeHRQ"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()       # uses inspect to get function/test name
            # screenshotName = "screenshot_"+currTime
            screenshotName = testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,attachment_type=allure.attachment_type.PNG) # attachment type can be different
            driver.get_screenshot_as_file("C:/Users//JamesAutomation/PycharmProjects/AutomationFramework_1/screenshots/"+screenshotName+".png")
            raise

        except:
            print("there was an exception")
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)

            raise                               # raises an exception. leave out if want test to pass

        else:
            print("no exception occurred")

        finally:
            print("I am inside the finally block")

        # driver.find_element_by_id("welcome").click()
        # driver.find_element_by_link_text("Logout").click()




