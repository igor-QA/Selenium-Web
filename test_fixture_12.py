import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def answer():
    return str(math.log(int(time.time())))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestOpenPage(object):
    def test_open_page(self, browser, link):
        link = "https://stepik.org/lesson/{}/step/1".format(link)
        browser.get(link)
        browser.implicitly_wait(10)
        browser.find_element(By.CLASS_NAME, "textarea").send_keys(answer())
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        feedback = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
        assert feedback == 'Correct!', f'Feedback is not "Correct!", real={feedback}'