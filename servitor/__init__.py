from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

HEADLESS_MODE = False
DEFAULT_WAIT_TIME = 20
URL = ""
AUTH_URL = ""
AUTH_USERNAME = ""
AUTH_PASSWORD = ""


def initialize_webdriver(headless_mode=False):
    """Initialize Firefox WebDriver."""
    options = Options()
    service = FirefoxService(GeckoDriverManager().install())
    if headless_mode:
        options.add_argument("--headless")
    return webdriver.Firefox(service=service, options=options)


driver = initialize_webdriver(HEADLESS_MODE)
wait = WebDriverWait(driver, DEFAULT_WAIT_TIME)


def auth():
    driver.get(f"{AUTH_URL}")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login__form")))
    driver.find_element(By.ID, "username").send_keys(AUTH_USERNAME)
    driver.find_element(By.ID, "password").send_keys(AUTH_PASSWORD)
    driver.execute_script(
        "arguments[0].click();",
        driver.find_element(By.CSS_SELECTOR, ".btn__primary--large"),
    )


def main():
    auth()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".global-nav__nav")))
    driver.get(f"{URL}")


if __name__ == "__main__":
    main()
