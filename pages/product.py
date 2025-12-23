from selenium.webdriver.common.by import By

class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def validate_title_is(self, title):
        validate = self.driver.find_element(By.XPATH, '//*[@id="tbodyid"]/h2')
        assert validate.text == title