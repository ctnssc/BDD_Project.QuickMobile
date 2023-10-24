#Pentru a nu fi nevoiti sa rescriem aceleasi functii/linii de cod in mai multe
# locuri astfel aparand cod redundant in aplicatie, am creat base page unde am definit
# toate actiunile de care avem nevoie in procesul de testare.

from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from browser import Browser

class BasePage(Browser):
    def open_url(self, url:str):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find(self, identifier: tuple):
        return self.driver.find_element(*identifier)

    def wait_for_visible_element(self, identifier: tuple, time:int = 10):
        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.visibility_of_element_located(identifier), "Element not visible")

    def get_text(self, identifier: tuple, time: int = 10):
        self.wait_for_visible_element(identifier, time)
        return self.find(identifier).text

    def type(self, identifier:tuple, message:str,time: int = 10):
        self.wait_for_visible_element(identifier, time)
        self.find(identifier).send_keys(message)

    def delete_text(self, identifier:tuple, time: int = 10):
        self.wait_for_visible_element(identifier, time)
        self.find(identifier).clear()

    def click(self, identifier: tuple, time:int = 10):
        self.wait_for_visible_element(identifier,time)
        self.find(identifier).click()

    def is_displayed(self, identifier: tuple):
        try:
            return self.find(identifier).is_displayed()
        except NoSuchElementException:
            return False