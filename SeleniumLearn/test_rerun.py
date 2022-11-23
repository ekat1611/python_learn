from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


# для того, чтобы перезапустить упавшие тесты, можно установить расширение командой pip3 install pytest-rerunfailures
# тесты должны быть запущены командой pytest -v --reruns 1 test_rerun.py, где 1 - это количество попыток запуска
def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")