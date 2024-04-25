from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# chrome driver
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

# driver.get("https://the-internet.herokuapp.com/iframe")
# driver.implicitly_wait(5)
# driver.switch_to.frame("mce_0_ifr")
# driver.find_element(By.ID, "tinymce").clear()
# driver.find_element(By.ID, 'tinymce').send_keys("I am automating the iframes")
# driver.switch_to.default_content()
# print(driver.find_element(By.CSS_SELECTOR, 'h3').text)




# new website iframe handling
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.switch_to.frame("courses-iframe")
action = ActionChains(driver)
action.scroll_to_element(driver.find_element(By.CLASS_NAME, "register-btn")).perform()
driver.implicitly_wait(5)
action.context_click(driver.find_element(By.CLASS_NAME, "register-btn")).click().perform()
