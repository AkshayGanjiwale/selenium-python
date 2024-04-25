import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# chrome driver
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

name = "Akshay"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()

name = "Akshay"
driver.find_element(By.ID, "confirmbtn").click()
time.sleep(2)
alert1 = driver.switch_to.alert
alertText1 = alert1.text
print(alertText1)
assert name in alertText1
# alert1.accept()
alert1.dismiss()