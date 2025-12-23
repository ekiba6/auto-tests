import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window
    driver.implicitly_wait(3)
    yield driver



