import BookingPage

def test_booking_date(browser):
    booking_main_page = SelectDate(browser)
    booking_main_page.go_to_site()
    booking_main_page.click_on_input("Ужгород")
    booking_main_page.click_on_search()
    booking_main_page.click_on_date()