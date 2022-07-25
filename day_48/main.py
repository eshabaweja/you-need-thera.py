from selenium import webdriver

# webdriver is an interface to drive the browsers
firefox_driver_path = "/usr/local/bin/geckodriver"
driver = webdriver.Firefox(executable_path=firefox_driver_path)

driver.get("https://www.amazon.com/")


# close closes current tab only
driver.close()
# quit closes entire browser window
driver.quit()