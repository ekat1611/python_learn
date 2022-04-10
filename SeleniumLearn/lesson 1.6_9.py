from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get(" http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements_by_css_selector('.form-group input') * (1)
    for element in elements:
       element.send_keys("Мой ответ")

    button = browser.find_element_by_xpath("//*[text() = \"Submit\"]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()