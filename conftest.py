import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    options = Options()
    # En GitHub Actions (CI=true) no hay monitor: modo headless
    if os.getenv("CI"):
        options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1366, 768)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            pytest_html = item.config.pluginmanager.getplugin("html")
            extras.append(pytest_html.extras.image(driver.get_screenshot_as_base64()))
            os.makedirs("screenshots", exist_ok=True)
            nombre = f"screenshots/{item.name}_{datetime.now():%Y%m%d_%H%M%S}.png"
            driver.save_screenshot(nombre)
    report.extras = extras
