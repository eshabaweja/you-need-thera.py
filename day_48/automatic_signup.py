from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Esha")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Bewajah")

email_id = driver.find_element(By.NAME, "email")
email_id.send_keys("esha@bewajah.com")

submit_button = driver.find_element(By.CLASS_NAME,"btn-primary")
submit_button.click()

driver.quit()