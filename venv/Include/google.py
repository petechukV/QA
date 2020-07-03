import unittest
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException

class ChildOnBooking(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver.exe")

    def test_add_chaild(self):
         try:
            driver = self.driver
            driver.set_window_size(1078, 738)
            driver.get("http://www.booking.com")
            self.assertIn("Booking.com", driver.title)

            sp = driver.find_element_by_xpath("//label[@id='xp__guests__toggle']")
            sp.click()
            driver.implicitly_wait(5)

            pl = driver.find_element_by_xpath("//div[contains(@class,'sb-group__field sb-group-children')]//button[contains(@class,'bui-button bui-button--secondary bui-stepper__add-button')]")
            for N in range(1,5,1):
                driver.implicitly_wait(2)
                pl.click()
                N = N - 1

         except ElementNotVisibleException as e:
            print(e.__dict__["msg"])

         finally:
              driver.save_screenshot("screen.png")
              # self.assertIn("value", driver.find_element_by_xpath("//input[@id='group_children']"))
              def tearDown(self):
                 self.driver.quit()

if __name__ == "__main__":
    unittest.main()