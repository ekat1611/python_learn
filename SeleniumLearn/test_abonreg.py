# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAbonreg():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_abonreg(self):
    # Test name: abon_reg
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://192.168.102.63:85/")
    # 2 | setWindowSize | 1552x840 | 
    self.driver.set_window_size(1552, 840)
    # 3 | click | id=login | 
    self.driver.find_element(By.ID, "login").click()
    # 4 | type | id=login | 123
    self.driver.find_element(By.ID, "login").send_keys("123")
    # 5 | click | id=password | 
    self.driver.find_element(By.ID, "password").click()
    # 6 | type | id=password | 12345678
    self.driver.find_element(By.ID, "password").send_keys("12345678")
    # 7 | click | css=.is-btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-btn").click()
    # 8 | mouseOver | css=.is-btn | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".is-btn")
    actions = ActionChains(self.driver)
    time.sleep(5)
    actions.move_to_element(element).perform()
    time.sleep(5)
    # 9 | click | linkText=Регистрация клиентов | 
    self.driver.find_element(By.LINK_TEXT, "Регистрация клиентов").click()
    time.sleep(5)
    # 10 | click | linkText=Закрепление договора | 
    self.driver.find_element(By.LINK_TEXT, "Закрепление договора").click()
    # 11 | click | css=.form-horizontal > .form-group .form-control | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-horizontal > .form-group .form-control").click()
    # 12 | mouseOver | css=.select2-default | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".select2-default")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 13 | mouseOut | css=.select2-default | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 14 | mouseDown | css=.select2-default | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".select2-default")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 15 | mouseUp | id=select2-drop-mask | 
    element = self.driver.find_element(By.ID, "select2-drop-mask")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 16 | click | css=div:nth-child(3) > .form-group .input-control .form-control | 
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > .form-group .input-control .form-control").click()
    # 17 | mouseDown | id=select2-chosen-6 | 
    element = self.driver.find_element(By.ID, "select2-chosen-6")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 18 | mouseUp | id=select2-drop-mask | 
    element = self.driver.find_element(By.ID, "select2-drop-mask")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 19 | click | css=.btn-success > .ladda-label > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success > .ladda-label > span").click()
    # 20 | mouseOver | css=.btn-success > .ladda-label > span | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn-success > .ladda-label > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 21 | mouseOut | css=.btn-success > .ladda-label > span | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 22 | click | css=.btn:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    # 23 | mouseOver | css=.btn:nth-child(2) | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 24 | mouseOut | css=.btn:nth-child(2) | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 25 | click | css=div:nth-child(7) .form-control | 
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(7) .form-control").click()
    # 26 | click | css=.btn-success > .ladda-label > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success > .ladda-label > span").click()
    # 27 | mouseOver | css=.btn-success > .ladda-label > span | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn-success > .ladda-label > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 28 | click | css=.row:nth-child(2) span | 
    self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(2) span").click()
    # 29 | click | css=.btn-success > .ladda-label > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success > .ladda-label > span").click()
    # 30 | click | css=.btn-primary:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(2)").click()
    # 31 | mouseOver | css=.btn-primary:nth-child(2) | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(2)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 32 | mouseOut | css=.btn-primary:nth-child(2) | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 33 | click | linkText=Изменить адрес | 
    self.driver.find_element(By.LINK_TEXT, "Изменить адрес").click()
    # 34 | mouseOver | linkText=Изменить адрес | 
    element = self.driver.find_element(By.LINK_TEXT, "Изменить адрес")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 35 | mouseOut | linkText=Изменить адрес | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 36 | mouseOver | css=.select2-default | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".select2-default")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 37 | mouseOut | css=.select2-default | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 38 | mouseDown | css=.select2-default | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".select2-default")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 39 | mouseUp | id=select2-drop-mask | 
    element = self.driver.find_element(By.ID, "select2-drop-mask")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 40 | mouseOver | id=select2-chosen-41 | 
    element = self.driver.find_element(By.ID, "select2-chosen-41")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 41 | mouseOut | id=select2-chosen-41 | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 42 | mouseDown | id=select2-chosen-41 | 
    element = self.driver.find_element(By.ID, "select2-chosen-41")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 43 | mouseUp | id=select2-drop-mask | 
    element = self.driver.find_element(By.ID, "select2-drop-mask")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 44 | click | css=.house | 
    self.driver.find_element(By.CSS_SELECTOR, ".house").click()
    # 45 | type | css=.house | 1
    self.driver.find_element(By.CSS_SELECTOR, ".house").send_keys("1")
    # 46 | click | css=.modal-footer > .btn-success | 
    self.driver.find_element(By.CSS_SELECTOR, ".modal-footer > .btn-success").click()
    # 47 | click | linkText=Скопировать из адреса установки | 
    self.driver.find_element(By.LINK_TEXT, "Скопировать из адреса установки").click()
    # 48 | click | css=.form-group:nth-child(1) .input-control .form-control | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) .input-control .form-control").click()
    # 49 | type | css=.form-group:nth-child(1) .input-control .form-control | просто
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) .input-control .form-control").send_keys("просто")
    # 50 | type | css=.form-group:nth-child(2) .input-control .form-control | тестовый
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) .input-control .form-control").send_keys("тестовый")
    # 51 | type | css=.form-group:nth-child(3) .input-control .form-control | абонент
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) .input-control .form-control").send_keys("абонент")
    # 52 | click | css=.form-group:nth-child(4) .glyphicon | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) .glyphicon").click()
    # 53 | click | css=.form-group:nth-child(4) > .col > .inline-block > .control-wrapper | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > .col > .inline-block > .control-wrapper").click()
    # 54 | click | css=.form-group:nth-child(6) .form-control | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(6) .form-control").click()
    # 55 | click | css=.form-group:nth-child(7) .form-control | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(7) .form-control").click()
    # 56 | click | css=.inline-block > .control-wrapper-right > .form-control | 
    self.driver.find_element(By.CSS_SELECTOR, ".inline-block > .control-wrapper-right > .form-control").click()
    # 57 | click | css=.form-group:nth-child(9) .form-control | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(9) .form-control").click()
    # 58 | click | css=.form-group:nth-child(10) .form-control | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(10) .form-control").click()
    # 59 | click | css=.form-group:nth-child(12) .control-wrapper:nth-child(2) > .form-control | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(12) .control-wrapper:nth-child(2) > .form-control").click()
    # 60 | click | css=div:nth-child(1) > .form-group .form-control | 
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .form-group .form-control").click()
    # 61 | click | css=.btn-success > .ladda-label > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success > .ladda-label > span").click()
    # 62 | mouseOver | css=.btn-success > .ladda-label > span | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn-success > .ladda-label > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 63 | mouseOut | css=.btn-success > .ladda-label > span | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 64 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 65 | click | css=.panel-wrapper:nth-child(1) .panel-body | 
    self.driver.find_element(By.CSS_SELECTOR, ".panel-wrapper:nth-child(1) .panel-body").click()
    # 66 | waitForElementVisible | css=.inline-block:nth-child(3) .form-control-static | 10
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".inline-block:nth-child(3) .form-control-static")))
  

test = TestAbonreg()
test.setup_method()
test.test_abonreg()
test.teardown_method()