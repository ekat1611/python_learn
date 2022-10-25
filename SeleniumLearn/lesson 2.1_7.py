import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    textarea = browser.find_element(By.CSS_SELECTOR, '#answer')
    textarea.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radiobutton.click()
    submit = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()
