import json
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

NAME_INPUT_FILE = 'input.txt'
OUTPUT_TXT_FILE = True
OUTPUT_JSON_FILE = True
# Задержка
TIME_SLEEP = 1
# Что извлекать у организации
# NAME = True
# CATEGORY = True

with open(NAME_INPUT_FILE, 'r') as f:
    lines = f.readlines()
    REQUESTS = [line.strip() for line in lines]

browser = webdriver.Chrome()
coordinate_category = {}
coordinate_name = {}

browser.get('https://yandex.ru/maps/')
time.sleep(TIME_SLEEP)

for request in REQUESTS:
    search_box_root = browser.find_element(By.XPATH, "//div[@class='search-form-view__input']")
    search_box = search_box_root.find_element(By.XPATH, "//input[@class='input__control _bold']")
    search_box.send_keys(request)  # Вводим текст запроса в окно поиска
    search_box.send_keys(Keys.RETURN)

    time.sleep(TIME_SLEEP)
    button_root = browser.find_element(By.XPATH, "//div[@class='carousel__content']")
    time.sleep(0.6)

    button = button_root.find_element(By.XPATH, "//a[@class='tabs-select-view__label']")

    browser.get(button.get_attribute('href') + 'inside/')

    scroll_origin = ScrollOrigin.from_viewport(100, 200)
    scroll_container = browser.find_element(By.CLASS_NAME, "scroll__container")

    scroll_height = browser.execute_script("return arguments[0].scrollHeight", scroll_container)
    while True:
        ActionChains(browser).scroll_from_origin(scroll_origin, 0, 5000).perform()
        time.sleep(0.9)
        if scroll_height == browser.execute_script("return arguments[0].scrollHeight", scroll_container):
            break
        else:
            scroll_height = browser.execute_script("return arguments[0].scrollHeight", scroll_container)

    result = {}
    # CATEGORY
    companies_category = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//a[@class='search-business-snippet-view__category']")))
    list_category = []
    for category in companies_category:
        if len(list_category) > 0 and (category.text).islower():
            list_category[-1] += f', {category.text}'
        else:
            list_category.append(category.text)
    coordinate_category[request] = list_category
    # NAME
    companies_name = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='search-business-snippet-view__title']")))
    list_name = []
    for name in companies_name:
        list_name.append(name.text)
    coordinate_name[request] = list_name


browser.quit()

if OUTPUT_TXT_FILE:
    with open("result_txt.txt", "w") as f_txt:
        f_txt.write('CATEGORY\n')
        f_txt.write(str(coordinate_category))
        f_txt.write('\nNAME\n')
        f_txt.write(str(coordinate_name))
if OUTPUT_JSON_FILE:
    with open("result_json.json", "w") as f_json:
        json.dump(coordinate_category, f_json, indent=2, ensure_ascii=False)
        json.dump(coordinate_name, f_json, indent=2, ensure_ascii=False)
