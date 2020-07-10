import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    dr = webdriver.Chrome()
    yield dr
    print("\nquit browser..")
    dr.quit()


languages = [
    ("ru", "русский"),
    ("de", "немецкий"),
    pytest.param("ua", "украинский", marks=pytest.mark.xfail(reason="no ua language")),
    ("en-gb", "английский")
]
labels = ["russian", "german", "ukrainian", "english", ]

@pytest.mark.parametrize("code, lang", languages, ids=labels)
def test_guest_should_see_login_link(browser, code, lang):
    link = "http://selenium1py.pythonanywhere.com/{}/".format(code)
    print("Проверяемый язык %s" % lang)
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")