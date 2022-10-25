import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects2.html')
    x_element = browser.find_element(By.CSS_SELECTOR, '#num1')
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, '#num2')
    y = y_element.text
    z = int(x) + int(y)
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(z))
    submit = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()

