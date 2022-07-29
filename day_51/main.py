from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from requests import request
import os
from dotenv import load_dotenv


SPEED_TEST = 'https://www.speedtest.net/'
TWITTER = 'https://twitter.com/'
QUOTES_JSON = 'https://zenquotes.io/api/random'
PROMISED_UP = 20
PROMISED_DOWN = 10
load_dotenv()
USERNAME = os.environ['TWITTER_USERNAME']
PASSWORD = os.environ['TWITTER_PASSWORD']

# getting internet speeds
speed_driver = webdriver.Firefox()
speed_driver.get(SPEED_TEST)
speed_driver.find_element(By.CLASS_NAME,"start-text").click()
time.sleep(60)

up_speed = float(speed_driver.find_element(By.CLASS_NAME,"upload-speed").text)
down_speed = float(speed_driver.find_element(By.CLASS_NAME,"download-speed").text)
# print(up_speed, down_speed)
speed_driver.quit()

# if speed less than promised
# going to twitter
if (up_speed < PROMISED_UP or  down_speed < PROMISED_DOWN):
    twitter_driver = webdriver.Firefox()
    twitter_driver.get(TWITTER)
    time.sleep(5)
    sign_in = twitter_driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div")
    sign_in.click()

    time.sleep(5)
    login_box = twitter_driver.find_element(By.NAME,"text")
    login_box.send_keys(USERNAME)
    login_box.send_keys(Keys.ENTER)

    time.sleep(5)
    password_box = twitter_driver.find_element(By.NAME,"password")
    password_box.send_keys(PASSWORD)
    password_box.send_keys(Keys.ENTER)

    # getting quote
    response = request(url=QUOTES_JSON, method="get").json()

    time.sleep(3)
    # ActionChains(twitter_driver).send_keys('n')
    # time.sleep(1)
    # ActionChains(twitter_driver).send_keys(f"{response[0]['q']}\n- [{response[0]['a']}]")\
    #     .key_down(Keys.CONTROL)\
    #     .key_down(Keys.ENTER)\
    #     .key_up(Keys.CONTROL)\
    #     .key_up(Keys.ENTER)\
    #     .perform()

    # tweet_body = twitter_driver.find_element(By.TAG_NAME,"body")
    # tweet_body.send_keys("n")
    # tweet_body.send_keys(f"{response[0]['q']}\n- [{response[0]['a']}]")

    time.sleep(2)
    tweet_button = twitter_driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span")
    tweet_button.click()
    time.sleep(1)
    ActionChains(twitter_driver)\
        .send_keys(response[0]['q'])\
        .send_keys(Keys.ENTER)\
        .send_keys(f"- {response[0]['a']}")\
        .key_down(Keys.CONTROL)\
        .key_down(Keys.ENTER)\
        .key_up(Keys.CONTROL)\
        .key_up(Keys.ENTER)\
        .perform()


# else if internet speed is fine
print("All good bruh.")