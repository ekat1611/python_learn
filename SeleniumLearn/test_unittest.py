import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestUnittest(unittest.TestCase):
    def test_registration1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(link)

            first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder = "Input your first name"]')
            first_name.send_keys('Мой ответ')
            last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder = "Input your last name"]')
            last_name.send_keys('Мой ответ')
            email = browser.find_element(By.CSS_SELECTOR, '[placeholder = "Input your email"]')
            email.send_keys('Мой ответ')

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        finally:
            browser.quit()

    def test_registration2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(link)

            first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder = "Input your first name"]')
            first_name.send_keys('Мой ответ')
            last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder = "Input your last name"]')
            last_name.send_keys('Мой ответ')
            email = browser.find_element(By.CSS_SELECTOR, '[placeholder = "Input your email"]')
            email.send_keys('Мой ответ')

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        finally:
            browser.quit()

