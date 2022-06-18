from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
import random

ACCOUNT_EMAIL = "{ACCOUNT-EMAIL}"
ACCOUNT_PASSWORD = "{ACCOUNT-PASSWORD}"
SIMILAR_ACCOUNT = "{SIMILAR-ACCOUNT}"
GECKO_DRIVER_PATH = "{DRIVER-PATH}"


class InstaFollower:
    def __init__(self, gecko_driver_path):
        self.service = FirefoxService(executable_path=gecko_driver_path)
        self.driver = webdriver.Firefox(service=self.service)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        username.send_keys(ACCOUNT_EMAIL)
        sleep(2)
        password.send_keys(ACCOUNT_PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)
        sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".mt3GC .HoLwm").click()
        sleep(2)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        sleep(2)
        modal = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[3]")
        for i in range(20):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".PZuss button")
        for button in all_buttons:
            try:
                button.click()
                sleep(random.randint(1, 8))
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div[3]/button[2]")
                cancel_button.click()


insta_bot = InstaFollower(GECKO_DRIVER_PATH)
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
