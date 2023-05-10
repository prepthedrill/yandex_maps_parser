from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('https://yandex.ru/maps/')

time.sleep(1.5)

# Ищем родительский класс для поискового окна
search_box_root = browser.find_element(By.XPATH, "//div[@class='search-form-view__input']")
# Ищем поисковое окно
search_box = search_box_root.find_element(By.XPATH, "//input[@class='input__control _bold']")
# Вводим текст запроса в поисковое окно
search_box.send_keys("56.264527, 44.020764")
search_box.send_keys(Keys.RETURN)

time.sleep(0.85)

button_root = browser.find_element(By.XPATH, "//div[@class='carousel__content']")
print('Успех')
time.sleep(0.85)

button = button_root.find_element(By.XPATH, "//a[@class='tabs-select-view__label']")

href = button.get_attribute('href') + 'inside/'
href.c
print(href)
print('Ура')

time.sleep(2)

browser.quit()
