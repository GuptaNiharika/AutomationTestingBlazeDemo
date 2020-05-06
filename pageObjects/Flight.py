from selenium.webdriver.common.by import By


class Flight:
    flightText=(By.XPATH,"//h3")
    flightChoose=(By.XPATH,"//table//tbody//tr[1]//td[1]//input")

    def __init__(self,driver): #constructor which accepts drive object
        self.driver=driver

    def getFlightText(self):
        return self.driver.find_element(*Flight.flightText)

    def chooseFlight(self):
        return self.driver.find_element(*Flight.flightChoose)
