from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.homepage_data import HomePageData
from pageObjects.homePage import HomePage
# from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])
        print(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        print(getData["lastname"])
        homepage.getCheckbox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        print(getData["gender"])

        homepage.getSubmitButton().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
