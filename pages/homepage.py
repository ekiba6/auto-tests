from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://demoblaze.com/')

    def click_galaxy_s6(self):
        galaxy = self.driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]').click()

    def click_category_monitor(self):
        monitor = self.driver.find_element(By.XPATH, '//*[@onclick="byCat(\'monitor\')"]').click()

    def check_products_count(self, count):
        monitors = self.driver.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == count