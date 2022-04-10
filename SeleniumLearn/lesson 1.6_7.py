import math
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/find_link_text'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    text_link = str(math.ceil(math.pow(math.pi, math.e)*10000))
    search = browser.find_element_by_link_text(text_link)
    search.click()

    input1 = browser.find_element_by_tag_name(".form-group [name = first_name]")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_tag_name(".form-group [name = last_name]")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('.form-group .city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_css_selector('#country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
    browser.close()

