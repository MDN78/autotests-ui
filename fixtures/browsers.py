import pytest
from playwright.sync_api import Playwright, Page, expect


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    # Передаем страницу для использования в тесте
    yield browser.new_page()

    browser.close()

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(email_input).to_be_visible()
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    expect(username_input).to_be_visible()
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(password_input).to_be_visible()
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_enabled()
    registration_button.click()

    context.storage_state(path="browser-state.json")
    browser.close()


@pytest.fixture  # по умолчанию scope=function явное указание не нужно
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    yield context.new_page()
    browser.close()