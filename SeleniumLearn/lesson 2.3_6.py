from selenium import webdriver
from selenium.webdriver.common.by import By
from math import sin, log

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    button = browser.find_element(By.CSS_SELECTOR, '.trollface')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(x_element.text)
    result = log(abs(12 * sin(x)))
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(result)
    submit = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    submit.click()
finally:
    print(browser.switch_to.alert.text)
    browser.quit()