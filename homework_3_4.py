def print_funk_and_argument(func, *args):
    printable_function = func.__name__.title().replace("_", " ")
    print(printable_function, *args)


def open_browser(browser_name):
    print_funk_and_argument(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_funk_and_argument(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_funk_and_argument(find_registration_button_on_login_page, page_url, button_text)


open_browser(browser_name="Chrome")
go_to_companyname_homepage(page_url="https://sports.ru")
find_registration_button_on_login_page(page_url="https://sports.ru", button_text="Войти")