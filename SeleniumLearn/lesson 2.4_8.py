from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from math import log, sin

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    button.click()
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_element.text)
    result = (log(abs(12 * sin(x))))
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(result)
    submit = browser.find_element(By.CSS_SELECTOR, "#solve")
    submit.click()
finally:
    print(browser.switch_to.alert.text)
    browser.quit()