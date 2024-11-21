from behave import given

from pages.android.landing_page import LandingPage


@given('that "{name}" as an "{rule}" user is in the login screen')
def step_impl(context, name, rule):
    landing_page = LandingPage(context.driver)
    landing_page.sign_button.click()
