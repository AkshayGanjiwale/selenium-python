import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browserSortedVeggiesList = []
# chrome driver
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
time.sleep(5)

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
veggiesWebElements = driver.find_elements(By.XPATH, '//tr/td[1]')

for ele in veggiesWebElements:
    browserSortedVeggiesList.append(ele.text)

originalVeggiesList = browserSortedVeggiesList.copy()
time.sleep(5)
assert browserSortedVeggiesList == originalVeggiesList