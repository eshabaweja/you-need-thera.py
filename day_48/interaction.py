from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articlecount = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
print(articlecount.text)
# articlecount.click()

all_portals = driver.find_element(By.LINK_TEXT,"Random article")
# all_portals.click()

search_bar = driver.find_element(By.NAME,"search")
search_bar.send_keys("pandemic")
search_bar.send_keys(Keys.ENTER)

# driver.quit()