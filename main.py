from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

NAME_INPUT_FILE = 'input.txt'

with open(NAME_INPUT_FILE, 'r') as f:
    lines = f.readlines()
    COORDINATES = [line.strip() for line in lines]

browser = webdriver.Chrome()

result = {}
for coordinate in COORDINATES:
    browser.get('https://yandex.ru/maps/')

    time.sleep(1)

    search_box_root = browser.find_element(By.XPATH, "//div[@class='search-form-view__input']")
    search_box = search_box_root.find_element(By.XPATH, "//input[@class='input__control _bold']")
    search_box.send_keys(coordinate)  # Вводим текст запроса в окно поиска
    search_box.send_keys(Keys.RETURN)

    time.sleep(1)
    button_root = browser.find_element(By.XPATH, "//div[@class='carousel__content']")
    time.sleep(1)

    button = button_root.find_element(By.XPATH, "//a[@class='tabs-select-view__label']")

    href = button.get_attribute('href') + 'inside/'

    browser.get(href)
    companies_category = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//a[@class='search-business-snippet-view__category']")))

    list_category = []
    for category in companies_category:
        list_category.append(category.text)

    result[coordinate] = list_category

browser.quit()

with open("result.json", "w") as f:
    json.dump(result, f, ensure_ascii=False)
