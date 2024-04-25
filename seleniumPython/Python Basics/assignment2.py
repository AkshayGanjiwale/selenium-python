# implicit and explicit wait
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []
# chrome driver
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//input[@class='search-keyword']").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
print(count)
assert count > 0
for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt=Cart]").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()
driver.find_element(By.XPATH, "//div/input[@class = 'promoCode']").send_keys('rahulshettyacademy')
driver.find_element(By.XPATH,"//div/button[@class = 'promoBtn']").click()
print(driver.find_element(By.CLASS_NAME,"promoInfo"))

# prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
# sum = 0
# for price in prices:
#     sum = sum + int(price.text)
#
print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(totalAmount)
totalAfterDiscount = int(float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text))
print(totalAfterDiscount)
assert totalAfterDiscount < totalAmount

