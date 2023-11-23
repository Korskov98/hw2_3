import random
import string

from Pages import SearchHelper

"""Успешная авторизация"""


def test_auth(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.login()
    main_title = main_page.check_main_title()
    assert main_title.is_displayed()
    assert main_title.text == "Добро пожаловать!"


"""Переход на страницу Варианты"""


def test_variants(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.login()
    main_page.open_variant_page()
    element = main_page.check_variant_title()
    assert element.is_displayed()
    assert element.text == "НТЦ ПРОТЕЙ"


"""Переход на страницу Авторизация с главной"""


def test_to_auth(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.login()
    main_page.open_auth_page()
    element = main_page.check_auth_title()
    assert element.is_displayed()
    assert element.text == "Привет с демо-сайта для автотестов!"


"""Переход на страницу Пользователи"""


def test_users(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.login()
    main_page.open_users_page()
    element = main_page.check_users_table()
    assert element.is_displayed()


"""Успешное добавление пользователя"""


def test_add_users(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.login()
    main_page.open_users_page()
    main_page.open_add_page()
    email = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '@' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    main_page.add_user(email, password, name)
    main_page.ok()
    main_page.open_users_page()
    element = main_page.check_user_in_table(email, name)
    assert element


"""Добавление пользователя без email"""


def test_add_users_without_email(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.login()
    main_page.open_users_page()
    main_page.open_add_page()
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    main_page.add_user("", password, name)
    main_title = main_page.check_empty_email_error_title()
    assert main_title.is_displayed()
    assert main_title.text == "Неверный формат E-Mail"


"""Добавление пользователя без пароля"""


def test_add_users_without_pass(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.login()
    main_page.open_users_page()
    main_page.open_add_page()
    email = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '@' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    main_page.add_user(email, "", name)
    main_title = main_page.check_pass_error_title()
    assert main_title.is_displayed()
    assert main_title.text == "Поле Пароль не может быть пустым"


"""Добавление пользователя без пароля"""


def test_add_users_without_name(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.login()
    main_page.open_users_page()
    main_page.open_add_page()
    email = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '@' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    main_page.add_user(email, password, "")
    main_title = main_page.check_name_error_title()
    assert main_title.is_displayed()
    assert main_title.text == "Поле Имя не может быть пустым"

