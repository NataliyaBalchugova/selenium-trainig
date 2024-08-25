import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from data import catalog_id, customers_id, modules_id, reports_id, settings_id, translations_id, titles_id


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
    for titles in titles_id:
        driver.find_element(By.PARTIAL_LINK_TEXT, titles).click()
        assert is_element_present(driver, By.TAG_NAME, "h1")
        if titles == 'Appearance':
            driver.find_element(By.ID, "doc-logotype").click()
        elif titles == 'Catalog':
            for elmnt in catalog_id:
                driver.find_element(By.ID, elmnt).click()
        elif titles == "Customers":
            for elmnt in customers_id:
                driver.find_element(By.ID, elmnt).click()
        elif titles == "Languages":
            driver.find_element(By.ID, "doc-storage_encoding").click()
        elif titles == "Modules":
            for elmnt in modules_id:
                driver.find_element(By.ID, elmnt).click()
        elif titles == "Orders":
            driver.find_element(By.ID, "doc-order_statuses").click()
        elif titles == "Reports":
            for elmnt in reports_id:
                driver.find_element(By.ID, elmnt).click()
        elif titles == "Settings":
            for elmnt in settings_id:
                driver.find_element(By.ID, elmnt).click()
        elif titles == "Tax":
            driver.find_element(By.ID, "doc-tax_rates").click()
        elif titles == "Translations":
            for elmnt in translations_id:
                driver.find_element(By.ID, elmnt).click()
