import math
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/math.html')
time.sleep(5)
x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)

textarea = browser.find_element(By.CSS_SELECTOR, '#answer')
textarea.send_keys(y)

checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
checkbox.click()

radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
radiobutton.click()

submit = browser.find_element(By.CSS_SELECTOR, '.btn-default')
submit.click()

time.sleep(10)




browser.quit()