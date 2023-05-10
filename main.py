from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.get('https://yandex.ru/maps/')

time.sleep(1.5)

search_box_root = browser.find_element(By.XPATH, "//div[@class='search-form-view__input']")
search_box = search_box_root.find_element(By.XPATH, "//input[@class='input__control _bold']")
search_box.send_keys("56.264527, 44.020764")  # Вводим текст запроса в окно поиска
search_box.send_keys(Keys.RETURN)

time.sleep(0.85)

button_root = browser.find_element(By.XPATH, "//div[@class='carousel__content']")
time.sleep(0.85)

button = button_root.find_element(By.XPATH, "//a[@class='tabs-select-view__label']")

href = button.get_attribute('href') + 'inside/'

browser.get(href)
companies_category = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//a[@class='search-business-snippet-view__category']")))

for category in companies_category:
    print(category.text)

browser.quit()
