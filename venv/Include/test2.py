import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from datetime import datetime, date, time

class ReservOnBooking(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver.exe")

    def test_add_chuld(self):
        driver = self.driver
        driver.get("http://www.booking.com")
        self.assertIn("Booking.com", driver.title)
        driver.implicitly_wait(5)
        sp = driver.find_element_by_xpath("//input[@id='ss']").send_keys("Ужгород")
        driver.implicitly_wait(1)
        en = driver.find_element_by_xpath("//form[1]//div[1]//div[4]//div[2]//button[1]//span[1]").click()

        d = datetime.now()
        driver.implicitly_wait(5)
        dt = driver.find_element_by_class_name("bui-calendar__date--today").click()
        driver.implicitly_wait(2)
        bt = driver.find_element_by_xpath("//button[contains(@class,'sb-searchbox__button')]").click()
        driver.save_screenshot("screen2.png")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()