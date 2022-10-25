from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    button = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    sleep(3)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(x_element.text)
    result = log(abs(12 * sin(x)))
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(result)
    submit = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    submit.click()
finally:
    print(browser.switch_to.alert.text)
    browser.quit()