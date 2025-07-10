import pytest
import uuid
import os
from utils.driver_factory import DriverFactory
from utils.api_client import ApiClient

@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    browser = request.param
    driver = DriverFactory.get_driver(browser)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def user():
    email = f"testuser_{uuid.uuid4().hex[:8]}@example.com"
    password = "password123"
    name = "Test User"
    response = ApiClient.create_user(email, password, name)
    token = response.json()["accessToken"]
    yield {"email": email, "password": password}
    ApiClient.delete_user(token)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            driver.save_screenshot(f"screenshots/{item.name}.png")