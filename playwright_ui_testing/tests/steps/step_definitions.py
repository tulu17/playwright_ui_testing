from playwright.sync_api import expect
from pytest_bdd import scenarios, step, parsers

from ..pages.test_login_pom import LoginPOM

# link the feature file
scenarios("../features/test_login.feature")


# Step definitions
@step('the login page is launched')
def user_navigates_to_login_page(page):
    pom = LoginPOM(page)
    pom.navigate_to_login_page()


@step(parsers.parse('the user types "{username}" username into the username field'))
def user_enters_username(page, username):
    pom = LoginPOM(page)
    pom.type_in_username(username)


@step(parsers.parse('the user types "{password}" password into the password field'))
def user_enters_password(page, password):
    pom = LoginPOM(page)
    pom.type_in_password(password)


@step('the user pushes submit button')
def user_pushes_submit_button(page):
    pom = LoginPOM(page)
    pom.push_submit_button()


@step(parsers.parse('the new page url should contain "{text}" text'))
def verify_page_url(page, text):
    assert text in page.url


@step(parsers.parse('the new page should contain "{text}" text'))
def check_if_page_contains_text(page, text):
    pom = LoginPOM(page)
    expect(pom.get_element_with_text(text)).to_be_visible()


@step(parsers.parse('the "{button_text}" button should be displayed on the new page'))
def check_if_page_contains_button(page, button_text):
    pom = LoginPOM(page)
    expect(pom.get_element_with_text(button_text)).to_be_visible()

@step(parsers.parse('the error message should be displayed'))
def check_if_page_contains_error_message(page):
    pom = LoginPOM(page)
    expect(pom.get_error_message_element()).to_be_visible()

@step(parsers.parse('the error message text "{error_message}" should be displayed'))
def check_error_message_text(page, error_message):
    pom = LoginPOM(page)
    expect(pom.get_error_message_element()).to_have_text(error_message)

