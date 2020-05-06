from selenium.webdriver.common.by import By

class PassengerDetails:

    reservationText=(By.XPATH,"//h2")
    name=(By.XPATH,"//input[@name='inputName']")
    address=(By.XPATH,"//input[@name='address']")
    city=(By.XPATH,"//input[@name='city']")
    state=(By.XPATH,"//input[@name='state']")
    zip=(By.XPATH,"//input[@name='zipCode']")
    creditNum=(By.XPATH,"//input[@name='creditCardNumber']")
    nameOnCard=(By.XPATH,"//input[@name='nameOnCard']")
    rememberMe=(By.XPATH,"//input[@id='rememberMe']")
    purchaseFlight=(By.XPATH,"//input[@value='Purchase Flight']")

    def __init__(self,driver): #constructor which accepts drive object
        self.driver=driver

    def getReservationText(self):
        return self.driver.find_element(*PassengerDetails.reservationText)

    def getName(self):
        return self.driver.find_element(*PassengerDetails.name)

    def getAddress(self):
        return self.driver.find_element(*PassengerDetails.address)

    def getCity(self):
        return self.driver.find_element(*PassengerDetails.city)

    def getState(self):
        return self.driver.find_element(*PassengerDetails.state)

    def getZip(self):
        return self.driver.find_element(*PassengerDetails.zip)

    def getCreditNum(self):
        return self.driver.find_element(*PassengerDetails.creditNum)

    def getNameOnCard(self):
        return self.driver.find_element(*PassengerDetails.nameOnCard)

    def getRememberMe(self):
        return self.driver.find_element(*PassengerDetails.rememberMe)

    def getPurchaseFlightButton(self):
        return self.driver.find_element(*PassengerDetails.purchaseFlight)