import random
from requests import request
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv


INSTAGRAM_URL = 'https://www.instagram.com/accounts/login/'
load_dotenv()
USERNAME = os.environ['INSTA_USERNAME']
PASSWORD = os.environ['INSTA_PASSWORD']
OTHER_ACCOUNT = os.environ['OTHER_ACCOUNT']

# creating a class for the bot
class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.num_of_followers = 1000

    def login(self):
        # self.url = url
        # self.username = username
        # self.password = password
        self.driver.get(INSTAGRAM_URL)
        time.sleep(5)
        user_box = self.driver.find_element(By.NAME,"username")
        user_box.send_keys(USERNAME)
        password_box = self.driver.find_element(By.NAME,"password")
        password_box.send_keys(PASSWORD)
        # clicking login button
        self.driver.find_element(By.CSS_SELECTOR,"button.sqdOP.L3NKy.y3zKF").click()

    def find_followers(self):
        # goin to their page and  open followers
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{OTHER_ACCOUNT}/followers")
        
        # make a list of their followers?
        time.sleep(5)
        scrollable_popup = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul")
        for i in range(5):
            self.follow_ids = scrollable_popup.find_elements(By.CLASS_NAME,"_acas")
            # [follow_id.click() for follow_id in self.follow_ids]
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            time.sleep(2)

    def follow(self):
        # follow everyone on the list
        [follow_id.click() for follow_id in self.follow_ids]
        # pass


# Outside of the class, initialise the object and call the three methods in order. 
insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
