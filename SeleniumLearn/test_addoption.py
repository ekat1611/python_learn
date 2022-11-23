from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


# данный тест обязательно должен запускаться командой, содержащей параметр --browser_name
# чтобы понять как это работает, можно провалиться в файл conftest.py и ознакомиться с документацией pytest на русском:
# https://pytest-docs-ru.readthedocs.io/ru/latest/example/simple.html
def test_guest_should_see_login_link(browser_addopt):
    browser_addopt.get(link)
    browser_addopt.find_element(By.CSS_SELECTOR, "#login_link")
