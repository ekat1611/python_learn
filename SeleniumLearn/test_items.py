from selenium.webdriver.common.by import By
from time import sleep

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


# запуск командой pytest -s -v --language=es test_items.py
def test_exist_button_add_to_basket(browser_change_language):
    browser_change_language.get(link)
    assert browser_change_language.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    # визуально оценить язык:
    sleep(5)