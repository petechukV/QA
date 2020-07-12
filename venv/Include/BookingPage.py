from BaseApp import BasePage
from selenium.webdriver.common.by import By

class BookingLocators:
    LOCATOR_BOOKING_LIST_BUTTON = (By.XPATH, "//label[@id='xp__guests__toggle']")
    LOCATOR_BOOKING_ADD_BUTTON = (By.XPATH, "//div[contains(@class,'sb-group__field sb-group-children')]//button[contains(@class,'bui-button bui-button--secondary bui-stepper__add-button')]")

    LOCATOR_BOOKING_SEARCH = (By.XPATH, "//input[@id='ss']")
    LOCATOR_BOOKING_FIND_BUTTON = (By.XPATH, "//form[1]//div[1]//div[4]//div[2]//button[1]//span[1]")
    LOCATOR_BOOKING_DATE = (By.CLASS_NAME, "bui-calendar__date--today")
    LOCATOR_BOOKING_BUTTON = (By.XPATH, "//button[contains(@class,'sb-searchbox__button')]")

class AddChuild(BasePage):

    def click_on_list(self):
        list_field = self.find_element(BookingLocators.LOCATOR_BOOKING_LIST_BUTTON).click()

    def click_add_chuild(self):
        chuild_field = self.find_element(BookingLocators.LOCATOR_BOOKING_ADD_BUTTON,time=2)
        for N in range(1, 5, 1):
            chuild_field.click()
            N = N - 1

class SelectDate(BasePage):

    def click_on_input(self,word):
        input_field = self.find_element(BookingLocators.LOCATOR_BOOKING_SEARCH)
        input_field.send_keys(word)
        return input_field

    def click_on_search(self):
        search_field = self.find_element(BookingLocators.LOCATOR_BOOKING_FIND_BUTTON).click()

    def click_on_date(self):
        date_field = self.find_element(BookingLocators.LOCATOR_BOOKING_DATE,time=3).click()
        end_field = self.find_element(BookingLocators.LOCATOR_BOOKING_BUTTON).click()