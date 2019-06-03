import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="type in browser name")

@pytest.fixture(scope="class")  # session only once, function for each function, class for a class
def test_setup(request):  # request when in conftest
    # global driver             not needed when in conftest fixture
    from selenium import webdriver

    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:/Users/JamesAutomation/PycharmProjects/AutomationFramework_1/drivers/chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:/Users/JamesAutomation/PycharmProjects/AutomationFramework_1/drivers/geckodriver.exe")

    # driver = webdriver.Chrome(
    #     executable_path="C:/Users/JamesAutomation/PycharmProjects/AutomationFramework_1/drivers/chromedriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test completed")