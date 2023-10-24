#In info page am definit toate datele, caile si actiunile ce sunt necesare
# pentru a putea defini pasii de testare pentru actualizarea informatiilor
# personale din cadrul sectiunii contul meu, informatii cont.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features.pages.base_page import BasePage

class InfoPage(BasePage):
    #DATA
    INFO_PAGE_URL = 'https://www.quickmobile.ro/info'
    INFO_PAGE_MESSAGE = 'Modifica datele contului tau'
    FIRSTNAME = 'Cristian'
    LASTNAME = 'TANASESCU'
    PHONE = '0773973155'
    COUNTY = 'Bucuresti'
    CITY = 'Sector 6'
    ADDRESS = 'Str. Sergent Ion Marcu 14'

    #XPATH
    INFO_PAGE_CLICK = (By.XPATH, '//h3[@class=contains(text(), "Informatii cont")]')
    INFO_PAGE_LABEL = (By.XPATH, '//a[@href="/info"]')
    INFO_PAGE_MESSAGE_LABEL = (By.XPATH, '//div[@class="page-subtitle"]')
    FIRSTNAME_LABEL = (By.XPATH, '//input[@id="firstname"]')
    LASTNAME_LABEL = (By.XPATH, '//input[@id="lastname"]')
    PHONE_LABEL = (By.XPATH, '//input[@id="phone"]')
    COUNTY_LABEL = (By.XPATH, '//select[@id="county"]')
    CITY_LABEL = (By.XPATH, '//select[@id="city"]')
    ADDRESS_LABEL = (By.XPATH, '//textarea[@id="streetaddress"]')
    SAVE_BUTTON_LABEL= (By.XPATH, '//button[@id="modifica"]')
    SELECTED_CITY_VALUE = (By.XPATH, '//select[@id="city"]//option[@selected=""]')
    SELECTED_COUNTY_NAME = (By.XPATH, '//select[@id="county"]//option[@selected]')

    def click_info(self):
        self.click(self.INFO_PAGE_CLICK)

    def open_page(self):
        return self.open_url(self.INFO_PAGE_URL)

    def get_infopage_message(self):
        return self.get_text(self.INFO_PAGE_MESSAGE_LABEL)

    def enter_firstname(self):
        self.delete_text(self.FIRSTNAME_LABEL)
        self.type(self.FIRSTNAME_LABEL, self.FIRSTNAME)

    def enter_lastname(self):
        self.delete_text(self.LASTNAME_LABEL)
        self.type(self.LASTNAME_LABEL, self.LASTNAME)

    def enter_phone(self):
        self.delete_text(self.PHONE_LABEL)
        self.type(self.PHONE_LABEL, self.PHONE)

    def select_county(self):
        Select(self.find(self.COUNTY_LABEL)).select_by_visible_text(self.COUNTY)

    def select_city(self):
        Select(self.find(self.CITY_LABEL)).select_by_visible_text(self.CITY)


    def enter_address(self):
        self.delete_text(self.ADDRESS_LABEL)
        self.type(self.ADDRESS_LABEL, self.ADDRESS)

    def click_save(self):
        self.click(self.SAVE_BUTTON_LABEL)

    def verify_saved_data(self):
        assert self.get_text(self.FIRSTNAME_LABEL) in self.FIRSTNAME
        assert self.get_text(self.LASTNAME_LABEL) in self.LASTNAME
        assert self.get_text(self.PHONE_LABEL) in self.PHONE
        selected_city_value = self.find(self.SELECTED_CITY_VALUE).text
        selected_county_value = self.find(self.SELECTED_COUNTY_NAME).text
        assert selected_city_value == self.CITY, f"Error, Expected {self.CITY}, actual: {selected_city_value}"
        assert selected_county_value == self.COUNTY, f"Error, Expected {self.COUNTY}, actual: {selected_county_value}"
        assert self.get_text(self.ADDRESS_LABEL) in self.ADDRESS
