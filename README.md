# Yandex Maps Scraper

The Yandex Maps Parser is a Python script that allows you to extract company data from Yandex Maps search results. It utilizes the Selenium library to automate the process of searching for specific requests and gathering information such as company names, categories, addresses, and coordinates.

## Prerequisites
Before running the script, make sure you have the following dependencies installed:
- Python 3.x
- Selenium
- tqdm
- ChromeDriver (for running Chrome browser)

## Installation
1. Clone the repository or download the script file (`main.py`) to your local machine.

2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

3. Download ChromeDriver from the official website: https://sites.google.com/a/chromium.org/chromedriver/
   Make sure to download the version compatible with your Chrome browser.

4. Extract the ChromeDriver executable to a location of your choice and make note of the file path.

## Usage
1. Prepare the input file:
   - Create a text file (`input.txt`) containing the search requests. Each request should be on a separate line. Example:
    ```
    Кремль, 1, Нижний Новгород
    улица Воровского 77 Киров
    58.603802, 49.670888
    ```
   - Save the file in the same directory as the script (`main.py`).

2. Run the script:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the following command to execute the script:
     ```
     python main.py
     ```

3. Monitor the progress:
   - The script will display a progress bar indicating the processing of each request.

4. View the results:
   - After the script completes, you will find the extracted data in a JSON file named `result_json.json`.
   - If any errors occur during the extraction process, the script will log the requests that caused the errors in a file named `error_address.txt`.

## Notes
- The script interacts with the Yandex Maps website and relies on its structure. Changes to the website's layout may require modifications to the script.
- If you encounter any issues, ensure that you have provided the correct paths and dependencies are properly installed.

## Contributing
Feel free to customize the script according to your needs or incorporate it into your own projects.

For any questions or issues, please contact Telegram @prepthedrill.

## License
This project is licensed under the MIT License.