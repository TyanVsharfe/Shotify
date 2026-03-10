import time
from http import HTTPStatus

from fastapi import HTTPException

from selenium import webdriver
from selenium.common import WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from shotify.api.config import settings


def get_selenium_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument('--disable-browser-side-navigation')
    options.add_argument('--disable-features=VizDisplayCompositor')
    options.add_argument('--blink-settings=imagesEnabled=true')
    options.add_argument("--no-sandbox")
    options.page_load_strategy = 'eager'
    options.add_argument('--headless=new')
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Remote(
        command_executor=f'http://{settings.SELENIUM_HOST}:4444/wd/hub',
        options=options
    )

    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script(
            "return Array.from(document.images).every(i => i.complete)"
        )
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
