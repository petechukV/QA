from BookingPage import AddChuild

def test_booking_chuild(browser):
    booking_main_page = AddChuild(browser)
    booking_main_page.go_to_site()
    booking_main_page.click_on_list()
    booking_main_page.click_add_chuild()