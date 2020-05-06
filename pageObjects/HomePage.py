from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.Flight import Flight

class HomePage:
    searchFlight=(By.XPATH,"//input[@value='Find Flights']")
    fromPort=(By.XPATH,"//select[@name='fromPort']")
    toPort=(By.XPATH,"//select[@name='toPort']")

    def __init__(self,driver): #constructor which accepts drive object
        self.driver=driver

    def getSearchFlight(self):
        return self.driver.find_element(*HomePage.searchFlight)# * to deserialize the tuple searchFlight
        #self.driver.find_element_by_xpath("//input[@value='Find Flights']").click()

    def getFromPortDropdown(self):
        dropdownFrom=Select(self.driver.find_element(*HomePage.fromPort)) #dropdown_from = Select(self.driver.find_element_by_xpath("//select[@name='fromPort']"))  # //tagname[@attribute='value']
        return dropdownFrom

    def getToPortDropdown(self):
        dropdownTo=Select(self.driver.find_element(*HomePage.toPort))
        return dropdownTo
        #dropdown_to = Select(self.driver.find_element_by_xpath("//select[@name='toPort']"))
