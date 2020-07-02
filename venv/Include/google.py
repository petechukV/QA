import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ChildOnBooking(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver.exe")

    def test_add_chuld(self):
        driver = self.driver
        driver.get("http://www.booking.com")
        self.assertIn("Booking.com", driver.title)

        sp = driver.find_element_by_xpath("//label[@id='xp__guests__toggle']")
        sp.click()

        pl = driver.find_element_by_xpath("//div[contains(@class,'sb-group__field sb-group-children')]//button[contains(@class,'bui-button bui-button--secondary bui-stepper__add-button')]")
        for N in range(1,5,1):
            pl.click()
            N = N - 1

       # self.assertIn("value", driver.find_element_by_xpath("//input[@id='group_children']"))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()