#In login page am definit toate datele, caile si actiunile ce sunt necesare
# pentru a putea defini pasii de testare pentru login.

from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class LoginPage(BasePage):
    #Date
    LOG_IN_PAGE_URL = 'https://www.quickmobile.ro/autentificare'
    HOMEPAGE_URL = 'https://www.quickmobile.ro/'
    VALID_EMAIL = 'ctnssc@gmail.com'
    INVALID_EMAIL = 'ctnss@gmail.com'
    VALID_PASSWORD = 'ITFfinalPROJECT'
    INVALID_PASSWORD = 'Parola123'
    VALID_LOGIN_URL = "https://www.quickmobile.ro/cont?loggedin=1"
    VALID_LOGIN_MESSAGE = "Bun venit, Cristian!"
    INVALID_LOGIN_MESSAGE = 'Adresa de email sau parola nu este corecta.'
    #XPATHuri
    EMAIL_LABEL = (By.XPATH, "//input[@id='email']")
    PASSWORD_LABEL = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON_LABEL = (By.XPATH, "//button[contains(text(),'Autentificare')]")
    VALID_LOGIN_LABEL = (By.XPATH, "//h2[@class='section-title']")
    INVALID_LOGIN_LABEL = (By.XPATH, "//div[@class='alert alert-with-icon alert-danger']")
    LOGOUT_BUTTON_LABEL = (By.XPATH, "//a[@href='/?logout']")

    def open_page(self):
        return self.open_url(self.LOG_IN_PAGE_URL)

    def enter_valid_email(self):
        self.type(self.EMAIL_LABEL, self.VALID_EMAIL)

    def enter_invalid_email(self):
        self.type(self.EMAIL_LABEL, self.INVALID_EMAIL)

    def enter_valid_password(self):
        self.type(self.PASSWORD_LABEL, self.VALID_PASSWORD)

    def enter_invalid_password(self):
        self.type(self.PASSWORD_LABEL, self.INVALID_PASSWORD)

    def click_submit_login(self):
        self.click(self.LOGIN_BUTTON_LABEL)

    def click_submit_logout(self):
        self.click(self.LOGOUT_BUTTON_LABEL)

    def get_expected_url_login(self):
        return self.VALID_LOGIN_URL

    def get_expected_url_homepage(self):
        return self.HOMEPAGE_URL

    def get_valid_login_message(self):
        return self.get_text(self.VALID_LOGIN_LABEL)

    def is_log_out_button_displayed(self):
        return self.is_displayed(self.LOGOUT_BUTTON_LABEL)

    def get_err_message(self):
        return self.get_text(self.INVALID_LOGIN_LABEL)

