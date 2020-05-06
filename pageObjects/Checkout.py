from selenium.webdriver.common.by import By


class Checkout:

    confirmationText=(By.XPATH,"//h1")

    def __init__(self,driver): #constructor which accepts drive object
        self.driver=driver

    def getConfirmationText(self):
        return self.driver.find_element(*Checkout.confirmationText)
