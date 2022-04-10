import math
from selenium import webdriver

import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/math.html')
time.sleep(5)
x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)

textarea = browser.find_element_by_css_selector('#answer')
textarea.send_keys(y)

checkbox = browser.find_element_by_css_selector('#robotCheckbox')
checkbox.click()

radiobutton = browser.find_element_by_css_selector('#robotsRule')
radiobutton.click()

submit = browser.find_element_by_css_selector('.btn-default')
submit.click()

time.sleep(10)




browser.quit()