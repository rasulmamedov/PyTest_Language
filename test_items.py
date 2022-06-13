from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")