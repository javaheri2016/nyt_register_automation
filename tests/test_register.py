from pytest_bdd import when, then
from pages.register_page import *


@when('I go to NYT registration page')
def go_to_NYT_reg_page(browser):
    register_page_url(browser)


@when('I provide my email')
def enter_email(browser):
    enter_generated_email(browser)


@when('I provide my too short password')
def enter_short_password(browser):
    enter_generated_short_password(browser)


@when('I click on create account button')
def click_create_button(browser):
    click_create_btn(browser)


@then('I verify an error message')
def verify_an_error(browser):
    verify_error_msg(browser)