from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

class DriverFactory:
    @staticmethod
    def get_driver(browser_name="chrome"):
        if browser_name.lower() == "chrome":
            return webdriver.Chrome(service=ChromeService())
        elif browser_name.lower() == "firefox":
            return webdriver.Firefox(service=FirefoxService())
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")