import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("https://sgugit.ru/")
    driver.find_element(By.LINK_TEXT, "УНИВЕРСИТЕТ").click()




