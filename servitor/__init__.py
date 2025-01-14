from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

HEADLESS_MODE = config["DEFAULT"].getboolean("HEADLESS_MODE")
DEFAULT_WAIT_TIME = config["DEFAULT"].getint("DEFAULT_WAIT_TIME")
URL = config["DEFAULT"]["URL"]
AUTH_URL = config["AUTH"]["AUTH_URL"]
AUTH_MAIL = config["AUTH"]["AUTH_MAIL"]
AUTH_PASSWORD = config["AUTH"]["AUTH_PASSWORD"]


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
    driver.find_element(By.ID, "username").send_keys(AUTH_MAIL)
    driver.find_element(By.ID, "password").send_keys(AUTH_PASSWORD)
    driver.execute_script(
        "arguments[0].click();",
        driver.find_element(By.CSS_SELECTOR, ".btn__primary--large"),
    )


def job_applying():
    driver.get(f"{URL}")
    """ Use job list CSS Selector """
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".HMyIuaHQTvatijhUGNtVoSMvZWgHCMThk")
        )
    )
    job_list = driver.find_element(
        By.CSS_SELECTOR, ".HMyIuaHQTvatijhUGNtVoSMvZWgHCMThk"
    ).find_elements(By.CSS_SELECTOR, "li")


def main():
    auth()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".global-nav__nav")))
    job_applying()


if __name__ == "__main__":
    main()
