import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/selects2.html')

x_element = browser.find_element_by_css_selector('#num1')
x = x_element.text

y_element = browser.find_element_by_css_selector('#num2')
y = y_element.text

z = int(x) + int(y)

select = Select(browser.find_element_by_css_selector("#dropdown"))
select.select_by_value(str(z))

submit = browser.find_element_by_css_selector('.btn-default')
submit.click()

#time.sleep(10)

browser.quit()

