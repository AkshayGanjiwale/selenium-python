from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# chrome driver
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CLASS_NAME, "blinkingText").click()

windowOpened = driver.window_handles

driver.switch_to.window(windowOpened[1])
userName = driver.find_element(By.LINK_TEXT, 'mentor@rahulshettyacademy.com').text
print(userName)

driver.switch_to.window(windowOpened[0])
driver.find_element(By.ID,"username").send_keys(userName)
driver.find_element(By.ID,"password").send_keys("12345678")
driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()
wait = WebDriverWait(driver, 5)
alertText = (By.CSS_SELECTOR, ".alert")
wait.until(expected_conditions.visibility_of_element_located(alertText))
print(driver.find_element(*alertText).text)
