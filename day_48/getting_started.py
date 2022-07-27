from selenium import webdriver
from selenium.webdriver.common.by import By

# webdriver is an interface to drive the browsers
firefox_driver_path = "/usr/local/bin/geckodriver"
driver = webdriver.Firefox(executable_path=firefox_driver_path)

driver.get("https://www.python.org/")

search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))

# if nothing else works in find_element, we can use XPATH to find our element
# inspect element, right click, copy XPATh

# close closes current tab only
# driver.close()
# quit closes entire browser window
driver.quit()