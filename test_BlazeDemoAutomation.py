import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.select import Select

from BaseClass import BaseClass
from pageObjects.Checkout import Checkout
from pageObjects.Flight import Flight
from pageObjects.HomePage import HomePage
from pageObjects.PassengerDetails import PassengerDetails

@pytest.mark.usefixtures("test_launchWebPage")
class Test(BaseClass):

    #@pytest.mark.category("URL-CHECK")
    def test_urlCheckHomePage(self):
        print(self.driver.current_url)
        assert self.driver.current_url == "http://www.blazedemo.com/"

    def test_checkFlightPageText(self,dataload): #refers to the dataload fixture
        homePage=HomePage(self.driver)
        dropdownFrom=homePage.getFromPortDropdown()
        dropdownFrom.select_by_visible_text("San Diego")
        dropdownTo=homePage.getToPortDropdown()
        dropdownTo.select_by_index(4) #New York
        homePage.getSearchFlight().click()
        flight = Flight(self.driver)
        message = flight.getFlightText().text
        self.driver.implicitly_wait(10)
        assert message == "Flights from San Diego to New York:"
        logger = self.getLogger()
        logger.info(dataload[0])
        #self.driver.find_element_by_xpath("//input[@value='Find Flights']").click()

    #@pytest.mark.category("URL-CHECK")
    def test_urlViewFlights(self):
        assert self.driver.current_url == "http://www.blazedemo.com/reserve.php"

    def test_checkFlightText_wrongmsg(self, dataload): #refers to the dataload fixture
        flight = Flight(self.driver)
        message = flight.getFlightText().text
        allure.attach(self.driver.get_screenshot_as_png(),name="Screenshot1",attachment_type=AttachmentType.PNG)
        assert message == "Wrong"
        logger = self.getLogger()
        logger.info(dataload[0])

    def test_chooseFlight(self):
        flight=Flight(self.driver)
        #self.driver.find_element_by_xpath("//table//tbody//tr[1]//td[1]//input").click()
        flight.chooseFlight().click()
        passenger=PassengerDetails(self.driver)
        print(self.driver.current_url)
        assert self.driver.current_url == "http://www.blazedemo.com/purchase.php"

    def test_reservationText(self):
        passenger=PassengerDetails(self.driver)
        message=passenger.getReservationText().text
        assert message=="Your flight from San Diego to New York has been reserved."

    def test_inputPassengerDetails(self):
        passenger=PassengerDetails(self.driver)
        passenger.getName().send_keys("Riya")
        passenger.getAddress().send_keys("#123,Indiranagar")
        passenger.getCity().send_keys("Bangalore")
        passenger.getState().send_keys("Karnataka")
        passenger.getZip().send_keys("560000")
        passenger.getCreditNum().send_keys("1234 5443 4444 6666")
        passenger.getNameOnCard().send_keys("Riya")
        passenger.getRememberMe().click()
        assert passenger.getName().get_attribute('value') == "Riya"

    #@pytest.mark.category("URL-CHECK")
    def test_urlFlightConfirmation(self):
        passenger=PassengerDetails(self.driver)
        passenger.getPurchaseFlightButton().click()
        assert self.driver.current_url == "http://www.blazedemo.com/confirmation.php"

    def test_flightConfirmationMessage(self):
        checkout=Checkout(self.driver)
        message=checkout.getConfirmationText().text
        assert message == "Thank you for your purchase today!"

    def test_closeWindow(self):
        self.driver.close()
