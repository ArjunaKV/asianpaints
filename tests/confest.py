import pytest
from selenium import webdriver

driver = None


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.asianpaints.com/")
    request.cls.driver = driver
    yield
    driver.quit()
