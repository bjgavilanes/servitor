import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


# Load configuration
def load_config(file_path: str) -> configparser.ConfigParser:
    """Load configuration from file."""
    config = configparser.ConfigParser()
    config.read(file_path)
    return config


# Initialize WebDriver
def initialize_webdriver(headless_mode: bool = False) -> webdriver.Firefox:
    """Initialize Firefox WebDriver."""
    options = Options()
    service = FirefoxService(GeckoDriverManager().install())
    if headless_mode:
        options.add_argument("--headless")
    return webdriver.Firefox(service=service, options=options)


# Authenticate
def auth(
    driver: webdriver.Firefox,
    wait: WebDriverWait,
    auth_url: str,
    auth_mail: str,
    auth_password: str,
) -> None:
    """Authenticate with the website."""
    driver.get(auth_url)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login__form")))
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys(auth_mail)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(auth_password)
    driver.execute_script(
        "arguments[0].click();",
        driver.find_element(By.CSS_SELECTOR, ".btn__primary--large"),
    )


# Apply for jobs
def job_applying(driver: webdriver.Firefox, wait: WebDriverWait, url: str) -> None:
    """Apply for jobs."""
    driver.get(url)
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".HMyIuaHQTvatijhUGNtVoSMvZWgHCMThk")
        )
    )
    job_list = driver.find_element(
        By.CSS_SELECTOR, ".HMyIuaHQTvatijhUGNtVoSMvZWgHCMThk"
    ).find_elements(By.CSS_SELECTOR, "li")
    for element in job_list:
        driver.execute_script("arguments[0].click();", element)
        wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".jobs-apply-button--top-card")
            )
        )
        easy_apply_button = driver.find_element(
            By.CSS_SELECTOR, ".jobs-apply-button--top-card"
        ).find_element(By.CSS_SELECTOR, "button")
        driver.execute_script("arguments[0].click();", easy_apply_button)
        safe_easy_apply_button = driver.find_element(
            By.CSS_SELECTOR, ".jobs-s-apply"
        ).find_element(By.CSS_SELECTOR, "button")
        driver.execute_script("arguments[0].click();", safe_easy_apply_button)
        wait.until(
            EC.invisibility_of_element(
                (By.CSS_SELECTOR, '[aria-labelledby="jobs-apply-header"]')
            )
        )


# Main function
def main() -> None:
    config = load_config("config.ini")
    headless_mode = config["DEFAULT"].getboolean("HEADLESS_MODE")
    default_wait_time = config["DEFAULT"].getint("DEFAULT_WAIT_TIME")
    url = config["DEFAULT"]["URL"]
    auth_url = config["AUTH"]["AUTH_URL"]
    auth_mail = config["AUTH"]["AUTH_MAIL"]
    auth_password = config["AUTH"]["AUTH_PASSWORD"]

    driver = initialize_webdriver(headless_mode)
    wait = WebDriverWait(driver, default_wait_time)

    auth(driver, wait, auth_url, auth_mail, auth_password)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".global-nav__nav")))
    job_applying(driver, wait, url)


if __name__ == "__main__":
    main()
