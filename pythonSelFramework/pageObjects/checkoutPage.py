from selenium.webdriver.common.by import By


class Checkout :

    def __init__(self, driver):
        self.driver = driver
    getTitle = (By.CSS_SELECTOR, ".card-title a")
    addButton = (By.CSS_SELECTOR, ".card-footer button")
    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getCardTitle(self):
        return self.driver.find_elements(*Checkout.getTitle)

    def getAddButton(self):
        return self.driver.find_elements(*Checkout.addButton)

    def getCheckoutButton(self):
        return self.driver.find_element(*Checkout.checkoutButton)
