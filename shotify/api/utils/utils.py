import time
from http import HTTPStatus

from fastapi import HTTPException

from selenium import webdriver
from selenium.common import WebDriverException, TimeoutException

from shotify.api.config import settings


def get_selenium_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Remote(
        command_executor=f'http://{settings.SELENIUM_HOST}:4444/wd/hub',
        options=options
    )
    return driver


def capture_screenshot(url, timeout=20):
    try:
        driver = get_selenium_driver()
        driver.set_page_load_timeout(timeout)
        driver.get(url)
        time.sleep(2)
        screenshot_path = f"/tmp/screenshot_{int(time.time())}.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()
        return screenshot_path
    except TimeoutException:
        driver.quit()
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Item not found")
