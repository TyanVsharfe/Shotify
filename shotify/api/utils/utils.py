import time
from selenium import webdriver

from shotify.api.config import settings


def get_selenium_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Remote(
        command_executor=f'http://{settings.SELENIUM_HOST}:4444/wd/hub',
        options=options
    )
    return driver


def capture_screenshot(url):
    driver = get_selenium_driver()
    driver.get(url)
    time.sleep(2)
    screenshot_path = f"/tmp/screenshot_{int(time.time())}.png"
    driver.save_screenshot(screenshot_path)
    driver.quit()
    return screenshot_path
