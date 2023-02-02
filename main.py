from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
# set using device description and hide that it is a bot
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86-64; rv:84.0) Gecko/20100101 Firefox/84.0")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")

# You need to change executable_path for your system, especially if you are using Linux
driver = webdriver.Chrome(
    executable_path="C:\\Users\\Alexandr\\PycharmProjects\\flruParser\\chromedriver.exe",
    options=options
)

try:
    url = "https://www.fl.ru/search/?type=projects"
    # keyword for searching
    key_word = "python"

    driver.get(url=url)

    # max time that webdriver will be searching element otherwise will raise an error
    driver.implicitly_wait(10)
    search_bar = driver.find_element(By.ID, "search-request")
    search_bar.clear()
    search_bar.send_keys(key_word)
    time.sleep(2)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(5)

    # Parsing of all vacancies boxes on the current page then parsing of requirement elements

    vacancies_list = driver.find_elements(By.CLASS_NAME, "search-lenta-item")

    for vacancy in vacancies_list[:10]:
        title = vacancy.find_element(By.CSS_SELECTOR, "h3")
        print(title.text)
        # price = vacancy.find_element(By.CLASS_NAME, "search-price")
        # print(price.text)
        posted_time = vacancy.find_element(By.CLASS_NAME, "search-meta")
        print(posted_time.text)
        applied = vacancy.find_element(By.CLASS_NAME, "search-answer")
        print(applied.text)

        if "/" in title.text:
            title = title.text.replace('/', '')

        # for each vacancy it creates a new text file and write down information in it
        with open(file=title, mode="w", encoding='utf8') as file:
            file.write(f"{title.text}\n")
            # file.write(f"Price: {price.text}\n")
            # file.write(f"{deadline.text}\n")
            file.write(f"Posted: {posted_time.text}\n")
            # file.write(f"{views.text}\n")
            file.write(f"{applied.text}\n")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
