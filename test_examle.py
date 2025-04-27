import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера
driver = webdriver.Chrome()
driver.maximize_window()

# Открытие сайта
driver.get("https://example.com")

# Проверка заголовка страницы
try:
    assert "Example" in driver.title
except AssertionError:
    sys.exit("Ошибка: заголовок не содержит 'Example'")

# Поиск элемента "More Information"
more_information = driver.find_element(By.CSS_SELECTOR, "a")
more_information.click()

# Проверка перенаправления
try:
    assert "https://www.iana.org/domains/example" in driver.current_url
except AssertionError:
    sys.exit("Ошибка: открыта неверная страница")

print("Тест выполнен успешно")

# Закрытие браузера
driver.quit()
