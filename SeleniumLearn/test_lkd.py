import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


def authorization():
    try:
        link = 'http://192.168.102.63:85'
        browser.get(link)
        element_present = EC.presence_of_element_located((By.XPATH, '//button[@type = "submit"]'))
        WebDriverWait(browser, 5).until(element_present)

        login = browser.find_element_by_xpath('//input[@id = "login"]')
        login.send_keys("123")
        password = browser.find_element_by_xpath('//input[@id = "password"]')
        password.send_keys("12345678")
        button = browser.find_element_by_xpath('//button[@type = "submit"]')
        button.click()
        time.sleep(1)
    except Exception as error:
        time.sleep(10)
        browser.close()
        print(f'Так вот в чём ошибка: {error}')

def fix_contract(smart_card_id):
    try:
        authorization()
        browser.find_elements_by_link_text('Регистрация клиентов')[0].click()
        browser.find_elements_by_link_text('Закрепление договора')[0].click()
        time.sleep(1)
        input = browser.find_element_by_css_selector('[data-attribute=\'SmartCardId\'].form-control')
        input.click()
        input.send_keys(smart_card_id)
        time.sleep(1)
        menu_model = browser.find_element_by_css_selector('.select2-choice.select2-default')
        menu_model.click()
        time.sleep(2)
        model_id = browser.find_element_by_css_selector('.select2-results-dept-0:nth-child(4) div')
        model_id.click()
        serial_number = browser.find_element_by_css_selector('input[data-attribute = \'SerialNumber\']')
        serial_number.send_keys(smart_card_id*2)
        contract = browser.find_element_by_xpath('//*[text() = \'Электронный договор\']')
        contract.click()
        browser.find_element_by_xpath('//div[text() = \'Бумажный договор\']').click()
        button_fix = browser.find_element_by_css_selector('.btn-success')
        button_fix.click()
        browser.find_element_by_css_selector('[data-bb-handler=\'ok\']').click()
        time.sleep(5)
        code = browser.find_element_by_css_selector('.form-control[data-attribute=\'SID\']')
        code.click()
        code.send_keys('11111111')
        button_fix = browser.find_element_by_css_selector('.btn-success')
        button_fix.click()
        time.sleep(5)
        registration(smart_card_id)

    except Exception as error:
        time.sleep(10)
        browser.close()
        print(f'Так вот в чём ошибка: {error}')


def registration(smart_card_id):
    try:
        # # авторизуемся
        # authorization()
        # # немного ждем
        # time.sleep(2)
        # ищем "Регистрация клиентов"
        # browser.find_elements_by_link_text('Регистрация клиентов')[0].click()
        time.sleep(2)
        # ищем "Регистрация клиента"
        browser.find_elements_by_link_text('Регистрация клиента')[0].click()
        time.sleep(1)
        # Вводим номер смарт-карты
        registration = browser.find_element_by_css_selector('[data-attribute=\'SmartCardId\']:first-child')
        registration.send_keys(smart_card_id)
        browser.find_element_by_css_selector('.btn-success').click()
        # расправляемся с алертом
        browser.find_element_by_css_selector('[data-bb-handler=\'ok\']').click()
        time.sleep(10)
        # нажимаем на "Изменить адрес"
        browser.find_element_by_css_selector('a[data-attribute=\'InstallationAddress\']').click()
        # вводим индекс
        index = browser.find_element_by_css_selector('.validation-error')
        index.send_keys('111395')
        # нажимаем ок
        browser.find_element_by_css_selector('.start-search').click()
        time.sleep(2)
        # нажимаем на "Москва г."
        browser.find_element_by_css_selector('.select2-result-label').click()
        # нажимаем на поле "Улица"
        browser.find_element_by_css_selector('.street .select2-choice').click()
        # нажимаем "нет улицы"
        browser.find_element_by_xpath('//*[text()="Нет улицы"]').click()
        # вводим номер дома
        house = browser.find_element_by_css_selector('.house')
        house.click()
        house.send_keys('1')
        # нажимаем на "Подтвердить"
        browser.find_element_by_css_selector('.modal-footer .btn-success').click()
        # нажимаем на "скопировать из адреса установки"
        browser.find_element_by_xpath('//*[text()=\'Скопировать из адреса установки\']').click()
        # вводим фамилию
        surname = browser.find_element_by_css_selector('.control-wrapper [data-attribute=\'SurName\']')
        surname.click()
        surname.send_keys('тест')
        # вводим имя
        name = browser.find_element_by_css_selector('.control-wrapper [data-attribute=\'FirstName\']')
        name.click()
        name.send_keys('тест')
        # вводим отчество
        second_name = browser.find_element_by_css_selector('.control-wrapper [data-attribute=\'SecondName\']')
        second_name.click()
        second_name.send_keys('тест')
        # вводим дату рождения
        birthday_name = browser.find_element_by_css_selector('.control-wrapper [data-attribute=\'BirthDate\']')
        birthday_name.click()
        birthday_name.send_keys('11111911')
        # вводим серию паспорта
        series = browser.find_element_by_css_selector('.control-wrapper [data-attribute=\'DocumentSeries\']')
        series.click()
        series.send_keys('1111')
        # вводим номер документа
        series = browser.find_element_by_css_selector('.control-wrapper [data-attribute=\'DocumentNumber\']')
        series.click()
        series.send_keys('111111')
        # вводим дату выдачи
        series = browser.find_element_by_css_selector('.control-wrapper [data-attribute=\'DocumentIssueDate\']')
        series.click()
        series.send_keys('11112011')
        # вводим место выдачи документа
        series = browser.find_element_by_css_selector('.control-wrapper [data-attribute=\'DocumentIssuedBy\']')
        series.click()
        series.send_keys('Москва')
        # вводим домашний телефон
        series = browser.find_element_by_css_selector('.control-wrapper [data-attribute=\'HomePhone\']')
        series.click()
        series.send_keys('9999999999')
        # вводим мобильный телефон
        series = browser.find_element_by_css_selector('.control-wrapper [data-attribute=\'MobilePhone\']')
        series.click()
        series.send_keys('9999999999')
        # вводим email
        series = browser.find_element_by_css_selector('.control-wrapper [data-attribute=\'Email\']')
        series.click()
        series.send_keys('test@mail.ru')
        # ставим галочку напротив 21 мая
        browser.find_element_by_xpath('//*[@id="page-wrap"]/div/div/div[3]/section/div/div/div/form[2]'
                                      '/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[2]/input').click()
        # нажимаем "зарегистрировать"
        browser.find_element_by_css_selector('.btn-success').click()

    except Exception as error:
        time.sleep(10)
        browser.close()
        print(f'Так вот в чём ошибка: {error}')
    finally:
        time.sleep(10)
        browser.close()


fix_contract('43002316385447')
# registration('42002316388254')