from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math


# косяки/непредусмотренные ситуации:
# 1. если ранее было отправлено решение в test_teardown, то тест падает. Нужно сделать нажатие на "решить снова"
# 2. я бы хотела сделать test_teardown фикстурой, которая выполняется в конце тестов класса. Но в таком случае не
# получается сделать авторизацию, фикстура authorization требует на вход link из другой фикстуры. Из-за это пришлось
# делать его тоже методом и накручивать параметризацию
# файл passwords.txt неудобен для расширения
# авторизация происходит каждый раз заново, хотелось бы просто открывать ссылки в других вкладках этого окна браузера

class Test():

    result = []

    @classmethod
    def authorization(cls, browser, link):
        with open("/Users/user/Desktop/Тестирование/my-projects/python_learn/SeleniumLearn/passwords.txt",
                  "r") as passwords:
            contents = passwords.readlines()
            email = contents[0]
            password_value = contents[1]
        browser.get(link)
        button_login = browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login")
        button_login.click()
        input_email = browser.find_element(By.ID, "id_login_email")
        input_email.send_keys(email)
        input_password = browser.find_element(By.ID, "id_login_password")
        input_password.send_keys(password_value)
        button_login = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
        button_login.click()

    @pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
                                      'https://stepik.org/lesson/236897/step/1', "https://stepik.org/lesson/236903/step/1",
                                      "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1",
                                      "https://stepik.org/lesson/236904/step/1",
                                      "https://stepik.org/lesson/236905/step/1"])
    def test_get_result(self, browser, link):
        self.authorization(browser, link)
        try:
            input_answer = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ember-text-area")))
            input_answer.send_keys(str(math.log(int(time.time()))))
            submit = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
            submit.click()
        except:
            again_button = browser.find_element(By.CSS_SELECTOR, ".again-btn")
            again_button.click()
            input_answer = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ember-text-area")))
            input_answer.send_keys(str(math.log(int(time.time()))))
            submit = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
            submit.click()
        is_correct = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
        assert is_correct.text == "Correct!", "feedback не совпадает с ожидаемым"
        if is_correct.text != "Correct!":
            self.result.append(is_correct.text)
        print(*self.result)

    def test_end(self, browser):
        link_for_answer = "https://stepik.org/lesson/237240/step/5?thread=solutions&unit=209628"
        self.authorization(browser, link_for_answer)
        time.sleep(5)
        browser.get(link_for_answer)
        input_answer = browser.find_element(By.CSS_SELECTOR, '.ember-text-area')
        input_answer.send_keys(''.join(self.result))
        submit = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
        submit.click()

