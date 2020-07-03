import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.keys import Keys


class ReservOnBooking(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver.exe")

    def test_calendar(self):
        try:
            driver = self.driver
            driver.set_window_size(1078, 738)
            driver.get("http://www.booking.com")
            self.assertIn("Booking.com", driver.title)

            driver.implicitly_wait(5)
            sp = driver.find_element_by_xpath("//input[@id='ss']").send_keys("Ужгород")
            driver.implicitly_wait(1)
            en = driver.find_element_by_xpath("//form[1]//div[1]//div[4]//div[2]//button[1]//span[1]").click()

            driver.implicitly_wait(5)
            dt = driver.find_element_by_class_name("bui-calendar__date--today").click()#суперечливо
            driver.implicitly_wait(2)
            bt = driver.find_element_by_xpath("//button[contains(@class,'sb-searchbox__button')]").click()

        except ElementNotVisibleException as e:
            print(e.__dict__["msg"])

        finally:
            driver.save_screenshot("screen2.png")
            def tearDown(self):
                self.driver.quit()

if __name__ == "__main__":
    unittest.main()