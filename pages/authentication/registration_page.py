from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page
from elements.button import Button
from elements.link import Link
import re


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration button')
        self.registration_page_login_link = Link(page, 'registration-page-login-link', 'Login link')

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.registration_page_login_link.click()
        self.check_current_url(re.compile('.*/#/auth/login'))
