from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/'


# данный тест нужно запускать командой pytest -s -v --language=ru/en test_change_language.py
# исходя из значения, переданного в --language, сайт будет отображаться на русском/английском
# логику фикстуры browser_change_language можно посмотреть в файле conftest.py
def test_guest_should_see_login_link(browser_change_language):
    browser_change_language.get(link)
    browser_change_language.find_element(By.CSS_SELECTOR, "#login_link")
    time.sleep(10)
