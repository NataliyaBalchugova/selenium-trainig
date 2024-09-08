import random
import string
from faker import Faker
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver


# Инициализация драйвера
@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


# Генерация данных
fake = Faker()
firstname = fake.first_name()
lastname = fake.last_name()
address1 = fake.street_address()
postcode = fake.postcode()
city = fake.city()
email = fake.email()
password_length = 10
password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
phone_length = 12
phone = "".join(random.choices(string.digits, k=phone_length))


def logout(driver):
    left = driver.find_element(By.ID, "box-account")
    left.find_element(By.LINK_TEXT, "Logout").click()


def test_registration_user(driver):
    driver.get("http://localhost/litecart/en/")
    # Регистрация
    driver.find_element(By.LINK_TEXT, "New customers click here").click()
    driver.find_element(By.NAME, "firstname").send_keys(firstname)
    driver.find_element(By.NAME, "lastname").send_keys(lastname)
    driver.find_element(By.NAME, "address1").send_keys(address1)
    driver.find_element(By.NAME, "postcode").send_keys(postcode)
    driver.find_element(By.NAME, "city").send_keys(city)
    select = driver.find_element(By.NAME, "country_code")
    country_code = select.text
    country_code_list = country_code.splitlines()
    cleaned_countries_list = [country.strip() for country in country_code_list]
    index = cleaned_countries_list.index("United States")
    driver.execute_script("arguments[0].selectedIndex = arguments[1];"
                          "arguments[0].dispatchEvent(new Event('change'))",
                          select, index)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "phone").send_keys(phone)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "confirmed_password").send_keys(password)
    driver.find_element(By.NAME, "create_account").click()
    # Выход (logout)
    logout(driver)
    # Повторный вход
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    login = driver.find_element(By.ID, "box-account-login")
    login.find_element(By.NAME, "login").click()
    # Выход (logout)
    logout(driver)
