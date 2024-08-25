import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from data import titles, titles_ids


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def is_element_present(driver, by_locator, value):
    try:
        driver.find_element(by_locator, value)
        return True
    except NoSuchElementException:
        return False


def test_admin(driver):
    driver.get("http://localhost/litecart/admin/")
    # Login
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.NAME, "login").click()
    for title in titles:
        driver.find_element(By.PARTIAL_LINK_TEXT, title).click()
        assert is_element_present(driver, By.TAG_NAME, "h1")
        action = titles_ids.get(title)
        if isinstance(action, list):
            for elmnt in action:
                driver.find_element(By.ID, elmnt).click()
        elif action:
            driver.find_element(By.ID, action).click()
