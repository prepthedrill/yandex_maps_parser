import json
import time
from tqdm import tqdm

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def extract_category(driver):
    """
    Extracts the categories of companies from the search results.
    Args: driver (WebDriver): The WebDriver instance.
    Returns: list: A list of categories.
    """
    companies_category = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//a[@class='search-business-snippet-view__category']")
        )
    )
    list_category = []
    for category in companies_category:
        if len(list_category) > 0 and category.text.islower():
            list_category[-1] += f', {category.text}'
        else:
            list_category.append(category.text)
    return list_category


def extract_name(driver):
    """
    Extracts the names of companies from the search results.
    Args:driver (WebDriver): The WebDriver instance.
    Returns:list: A list of company names.
    """
    companies_name = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='search-business-snippet-view__title']")
        )
    )
    list_name = [name.text for name in companies_name]
    return list_name


def extract_address(driver):
    """
    Extracts the addresses of companies from the search results.
    Args: driver (WebDriver): The WebDriver instance.
    Returns: list: A list of company addresses.
    """
    companies_address = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='toponym-card-title-view__description']")
        )
    )
    addresses = [element.text for element in companies_address]
    return addresses


def extract_coordinates(driver):
    """
    Extracts the coordinates of companies from the search results.
    Args: driver (WebDriver): The WebDriver instance.
    Returns: list: A list of company coordinates.
    """
    companies_coordinates = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='toponym-card-title-view__coords-badge']")
        )
    )
    coordinates = [element.text for element in companies_coordinates]
    return coordinates


def perform_search(driver, request, TIME_SLEEP=1):
    """
    Performs a search for a specific request on Yandex Maps.
    Args:
        driver (WebDriver): The WebDriver instance.
        request (str): The search request.
        TIME_SLEEP (int, optional): The time to sleep between actions. Defaults to 1.
    """
    search_box_root = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='search-form-view__input']")
        )
    )
    search_box = search_box_root.find_element(
        By.XPATH, "//input[@class='input__control _bold']"
    )
    search_box.send_keys(request)
    search_box.send_keys(Keys.RETURN)
    time.sleep(TIME_SLEEP)
    button_root = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='carousel__content']")
        )
    )
    button = button_root.find_element(
        By.XPATH, "//a[@class='tabs-select-view__label']"
    )
    driver.get(button.get_attribute('href') + 'inside/')

    scroll_origin = ScrollOrigin.from_viewport(100, 200)
    scroll_container = driver.find_element(By.CLASS_NAME, "scroll__container")
    scroll_height = driver.execute_script(
        "return arguments[0].scrollHeight", scroll_container
    )
    while True:
        ActionChains(driver).scroll_from_origin(scroll_origin, 0, 5000).perform()
        time.sleep(0.9)
        if scroll_height == driver.execute_script(
                "return arguments[0].scrollHeight", scroll_container
        ):
            break
        else:
            scroll_height = driver.execute_script(
                "return arguments[0].scrollHeight", scroll_container
            )


if __name__ == '__main__':
    """
    The main entry point of the script.
    """
    # Настройка работы без открывания браузера
    chrome_options = Options()
    # chrome_options.add_argument('--headless')

    NAME_INPUT_FILE = 'input.txt'
    BROWSER = webdriver.Chrome(options=chrome_options)
    YANDEX_MAP_LINK = 'https://yandex.ru/maps/'

    try:
        with open(NAME_INPUT_FILE, 'r') as f:
            REQUESTS = [line.strip() for line in f.readlines()]

        try:
            BROWSER.get(YANDEX_MAP_LINK)
            time.sleep(1)

            # Использование tqdm для отображения шкалы выполнения
            for request in tqdm(REQUESTS, desc='Processing requests', unit='request'):
                perform_search(BROWSER, request)

                with open("result_json.json", "a") as f_json:
                    result = {
                        "ADDRESS": extract_address(BROWSER),
                        "COORDINATES": extract_coordinates(BROWSER),
                        "CATEGORY": extract_category(BROWSER),
                        "NAME": extract_name(BROWSER)
                    }
                    f_json.write(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")
        finally:
            BROWSER.quit()

    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{NAME_INPUT_FILE}' not found.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the input file: {str(e)}")
