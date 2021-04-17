from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    """
    Configures driver parameters
    Use when calling pytest
    """
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(25)
    yield driver
    driver.quit()
