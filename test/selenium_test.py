import time
from pages.homepage import HomePage
from pages.product import ProductPage



def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.validate_title_is('Samsung galaxy s6')



def test_check_two_mon(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_category_monitor()
    time.sleep(2) #плохая практика. нужно ожидать чего-то конкретного а не просто жестко фиксировать запуск
    homepage.check_products_count(2)
   