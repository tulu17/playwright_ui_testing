from playwright.sync_api import Page

LOGIN_PAGE_URL = 'https://practicetestautomation.com/practice-test-login'


class LoginPOM:

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_login_page(self):
        self.page.goto(LOGIN_PAGE_URL)

    def type_in_username(self, username):
        self.page.get_by_role('textbox', name='username').fill(username)

    def type_in_password(self, password):
        self.page.get_by_role('textbox', name='password').fill(password)

    def push_submit_button(self):
        self.page.get_by_role('button', name='Submit').click(force=True)

    def get_element_with_text(self, text):
        return self.page.get_by_text(text)

    def get_error_message_element(self):
        text = self.page.locator('[id="error"]').text_content
        return self.page.locator('[id="error"]')
