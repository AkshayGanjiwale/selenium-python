from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# chrome driver
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(2)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

# taking screenshot
driver.get_screenshot_as_file("screen.png")
