from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# chrome driver
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

#firefox driver
# service_obj = Service("C:\\Users\\ITH\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj)

#edge driver
# service_obj = Service("C:\\Users\\ITH\\Downloads\\edgedriver_win64\\msedgedriver.exe")
# driver = webdriver.Edge(service=service_obj)


driver.maximize_window()
driver.get("https://dev.ballers.fun")
print(driver.title)
print(driver.current_url)
driver.get("https://dev.coinbuck.com/")
driver.back()
driver.refresh()
driver.forward()
driver.close()
