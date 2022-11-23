from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys('Ekaterina')
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys('Shiganova')
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys('test_addoption.py@mail.ru')
    file = browser.find_element(By.CSS_SELECTOR, '#file')
    file.send_keys('/Users/user/Desktop/Тестирование/my-projects/python_learn/SeleniumLearn/lesson 2.1_7.py')
    submit = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    submit.click()
finally:
    sleep(10)
    browser.quit()