import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver


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
    # Appearance
    driver.find_element(By.XPATH, "//span[@class='name' and text()='Appearence']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element(By.ID, "doc-logotype").click()
    # Catalog
    driver.find_element(By.XPATH, "//span[@class='name' and text()='Catalog']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element(By.ID, "doc-product_groups").click()
    driver.find_element(By.ID, "doc-option_groups").click()
    driver.find_element(By.ID, "doc-manufacturers").click()
    driver.find_element(By.ID, "doc-suppliers").click()
    driver.find_element(By.ID, "doc-delivery_statuses").click()
    driver.find_element(By.ID, "doc-sold_out_statuses").click()
    driver.find_element(By.ID, "doc-quantity_units").click()
    driver.find_element(By.XPATH, "//span[@class='name' and text()='CSV Import/Export']").click()
    # Countries
    driver.find_element(By.XPATH, "//span[@class='name' and text()='Countries']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
    # Currencies
    driver.find_element(By.XPATH, "//span[@class='name' and text()='Currencies']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
    # Customers
    driver.find_element(By.XPATH, "//span[@class='name' and text()='Customers']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element(By.ID, "doc-csv").click()
    driver.find_element(By.ID, "doc-newsletter").click()
    # Geo Zones
    driver.find_element(By.XPATH, "//span[@class='name' and text()='Geo Zones']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
    # Languages
    driver.find_element(By.XPATH, "//span[@class='name' and text()='Languages']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element(By.ID, "doc-storage_encoding").click()
    # Modules
    driver.find_element(By.XPATH, "//span[@class='name' and text()='Modules']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element(By.ID, "doc-customer").click()
    driver.find_element(By.ID, "doc-shipping").click()
    driver.find_element(By.ID, "doc-payment").click()
    driver.find_element(By.ID, "doc-order_total").click()
    driver.find_element(By.ID, "doc-order_success").click()
    driver.find_element(By.ID, "doc-order_action").click()
    # Orders
    driver.find_element(By.XPATH, "//span[@class='name' and text()='Orders']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element(By.ID, "doc-order_statuses").click()
    # Pages
    driver.find_element(By.XPATH, "//span[@class='name' and text()='Pages']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
    # Reports
    driver.find_element(By.XPATH, "//span[@class='name' and text()='Reports']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element(By.ID, "doc-monthly_sales").click()
    driver.find_element(By.ID, "doc-most_sold_products").click()
    driver.find_element(By.ID, "doc-most_shopping_customers").click()
    # Settings
    driver.find_element(By.XPATH, "//span[@class='name' and text()='Settings']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element(By.ID, "doc-store_info").click()
    driver.find_element(By.ID, "doc-defaults").click()
    driver.find_element(By.ID, "doc-general").click()
    driver.find_element(By.ID, "doc-listings").click()
    driver.find_element(By.ID, "doc-images").click()
    driver.find_element(By.ID, "doc-checkout").click()
    driver.find_element(By.ID, "doc-advanced").click()
    driver.find_element(By.ID, "doc-security").click()
    # Slides
    driver.find_element(By.XPATH, "//span[@class='name' and text()='Slides']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
    # Tax
    driver.find_element(By.XPATH, "//span[@class='name' and text()='Tax']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element(By.ID, "doc-tax_rates").click()
    # Translations
    driver.find_element(By.XPATH, "//span[@class='name' and text()='Translations']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
    driver.find_element(By.ID, "doc-scan").click()
    driver.find_element(By.XPATH, "//span[@class='name' and text()='CSV Import/Export']").click()
    # Users
    driver.find_element(By.XPATH, "//span[@class='name' and text()='Users']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
    # vQmods
    driver.find_element(By.XPATH, "//span[@class='name' and text()='vQmods']").click()
    assert is_element_present(driver, By.TAG_NAME, "h1")
