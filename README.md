# Yandex Maps Parser

This script allows you to extract information about companies from Yandex Maps search results. It uses the Selenium library to automate the web browser and retrieve the desired data.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.10
- Selenium library
- Chrome WebDriver (compatible with your Chrome browser version)

You can install the required packages using pip:

```
pip install -r requrements.txt
```

## Usage

1. Place the script in a directory of your choice.

2. Create a text file named `input.txt` in the same directory. Each line in the file should contain a search request for Yandex Maps.
Example:
```
Кремль, 1, Нижний Новгород
улица Воровского 77 Киров
58.603802, 49.670888
```


3. Run the script by executing the following command:

```
python main.py
```

## Output

The script will perform a search for each request in the `input.txt` file and extract the following information for each company:

- Company name
- Company category
- Company address
- Company coordinates

The extracted data will be saved in a JSON file named `result_json.json`. Each line in the file will contain the JSON representation of the extracted data for one company.

## Note

- Make sure you have the Chrome WebDriver executable (`chromedriver`) in your system's PATH or provide the path to it in the script (`webdriver.Chrome(executable_path='path/to/chromedriver')`).

- The script uses explicit waits to ensure that the elements on the page are loaded before performing any actions. You can adjust the timeout values in the `WebDriverWait` calls if needed.

- The script assumes that you are using Chrome as the web browser. If you are using a different browser, make sure to modify the script accordingly.

- Please be aware of the website's terms of service and usage policies. Web scraping should be done responsibly and in compliance with the website's guidelines.

Feel free to customize the script according to your needs or incorporate it into your own projects.

For any questions or issues, please contact Telegram @prepthedrill.