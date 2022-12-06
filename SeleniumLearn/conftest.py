import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# просто фикстура, которая применяется к каждому тесту (= к каждой функции в тестовом классе)
# в ней создаётся и возвращается экземпляр класса webdriver
# грубо говоря, всё что до yield является setup (действия перед тестом), всё что после - teardown (действия после теста)
@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(50)
    yield browser
    browser.quit()


def pytest_addoption(parser):
    # тут парсим из команды переданное в --browser_name значение
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    # тут парсим из команды переданное в --language значение
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or en")


# фикстура, которая идёт в pytest_addoption и вытаскивает значение атрибута language, переданного в командной строке
# эта фикстура задействована в файле test_change_language.py
@pytest.fixture(scope="function")
def browser_change_language(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def browser_addopt(request):
    """
    Усовершенствованная фикстура, которая внутри себя вызывает request.config.getoption. Идёт обращение к методу
    pytest_addoption (который выше) и в результате фикстура вынимает значение переданное при запуске теста:
    pytest -s -v --browser_name=chrome test_addoption.py
    После этого идёт развилка, создавать экземпляр движка Chrome или Firefox.
    Если в тест была передана такая фикстура, то команда вида pytest -s -v test_addoption.py его уронит,
    т.к. фикстура будет вызывать pytest_addoption, а этот метод будет искать параметр --browser_name в команде
    """
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()