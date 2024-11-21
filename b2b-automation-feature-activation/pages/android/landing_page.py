from page_objects import PageElement

from pages.android.commom_page import CommomPage


class LandingPage(CommomPage):
    def __init__(self, driver):
        super().__init__(driver)

    sign_button = PageElement(id_='signinButton')
    signup_button = PageElement(id_='signupButton')
