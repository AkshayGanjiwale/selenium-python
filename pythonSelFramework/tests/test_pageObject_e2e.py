from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.checkoutPage import Checkout
from pageObjects.confirmPage import ConfirmPage
from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_pageObject_e2e(self):
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        checkout = Checkout(self.driver)
        cards = checkout.getCardTitle()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkout.getAddButton()[i].click()

        checkout.getCheckoutButton().click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        # time.sleep(5)
        self.verifyTextPresence("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirm = ConfirmPage(self.driver)
        confirm.getPurchaseButton().click()
        textMatch = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        assert ("Success! Thank you!" in textMatch)
