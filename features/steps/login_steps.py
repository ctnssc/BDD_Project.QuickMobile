# Login_steps este un fisier de tipul step definition file si ajuta la
# implementarea tehnica  a scenariilor descrise in login_steps.feature.

from behave import *
from features.pages.login_page import LoginPage

@given('I am on the login page')
def step_impl(context):
    context.loginpage = LoginPage()
    context.loginpage.open_page()

@when('I enter a valid email')
def step_impl(context):
    context.loginpage.enter_valid_email()

@when('I enter a valid password')
def step_impl(context):
    context.loginpage.enter_valid_password()

@when('I enter an invalid email')
def step_impl(context):
    context.loginpage.enter_invalid_email()

@when('I enter an invalid password')
def step_impl(context):
    context.loginpage.enter_invalid_password()

@when('I press login button "Autentificare"')
def step_impl(context):
    context.loginpage.click_submit_login()

@then('I should be on the user home page')
def step_impl(context):
    assert context.loginpage.get_expected_url_login() == context.loginpage.get_current_url(), "Actual URL is not the same as expected."

@then('I should see "Bun venit, Cristian!"')
def step_impl(context):
    assert context.loginpage.VALID_LOGIN_MESSAGE == context.loginpage.get_valid_login_message(), "Login message not as expected."

@then('I should see the logout button "Delogare Cristian"')
def step_impl(context):
    assert context.loginpage.is_log_out_button_displayed(), "Logout button is not visible."

@then('I should see an error message')
def step_impl(context):
    assert context.loginpage.INVALID_LOGIN_MESSAGE in context.loginpage.get_err_message(), 'Error message not found.'

@when('I press logout button')
def step_impl(context):
    context.loginpage.click_submit_logout()

@then('I should be on the website home page')
def step_impl(context):
    assert context.loginpage.get_expected_url_homepage() == context.loginpage.get_current_url(), "Actual URL is not the same as expected."

