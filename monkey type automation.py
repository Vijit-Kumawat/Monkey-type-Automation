
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time


browser = webdriver.Chrome(executable_path=r"C:/Users/Lenovo/Downloads/chromedriver")
browser.maximize_window()

browser.get("https://monkeytype.com/")
time.sleep(9)


def one_word_at_a_time():
    # version 3: detect one active word at a time and input (fastest way)
    try:
        while len(browser.find_elements_by_class_name("word")) != 0:
            ActionChains(browser).send_keys([letter.text for letter in browser.find_element_by_css_selector(".word.active").find_elements_by_tag_name("letter")] + [' ']).perform()
            time.sleep(.1)
    except Exception as e:
            print(e)
    print("Game Over")


one_word_at_a_time()
