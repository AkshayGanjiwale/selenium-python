from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    purchaseButton = (By.CSS_SELECTOR, "[type='submit']")

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)