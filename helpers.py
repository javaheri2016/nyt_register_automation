import os
import random
import string
import uuid
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def do_click(browser, locator, sec=10):
    """
    Waits and clicks on the chosen element
    Args:
        browser: webdriver
        locator (str): chosen locator from locators.py
        sec (int): default time to wait
    """
    WebDriverWait(browser, sec).until(EC.element_to_be_clickable(locator)).click()


def do_send_keys(browser, locator, text, sec=5):
    """
    Sends keys to the chosen element
    Args:
        browser: webdriver
        locator (str): chosen locator from locators.py
        text (str): text to be send
        sec (int): default time to wait
    """
    WebDriverWait(browser, sec).until(EC.visibility_of_element_located(locator)).send_keys(text)


def get_element_text(browser, locator):
    """
    Gets text of the chosen element
    Args:
        browser: webdriver
        locator (str): chosen locator from locators.py
    """
    elem_text = WebDriverWait(browser, 30).until(EC.presence_of_element_located(locator)).text
    return elem_text


def is_visible(browser, locator, sec=5) -> bool:
    """
    Waits and checks if element is visible
    Args:
        browser: webdriver
        locator (str): chosen locator from locators.py
        sec (int): default time to wait
    Returns:
        True or False
    """
    elem = WebDriverWait(browser, sec).until(EC.visibility_of_element_located(locator))
    return bool(elem)


def random_email_generator() -> str:
    """
    Generates proper e-mail for testing purposes
    Returns (str): e-mail
    """
    ran_email = 'test.new.york.times+' + uuid.uuid4().hex[:4] + '@gmail.com'
    return ran_email


def random_password_generator(length: int) -> str:
    """
    Generates random password with chosen length
    Args:
        length (int): password length
    """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

