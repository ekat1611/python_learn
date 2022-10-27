#настройка ожиданий
#достаточно один раз добавить implicitly_wait(количество секунд) и селениум будет ждать появления элемента
# указанное кол-во секунд, опрашивая раз в несколько милисекунд
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text