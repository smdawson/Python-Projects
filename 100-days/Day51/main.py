from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWN = 400
PROMISED_UP = 40
GECKO_DRIVER_PATH = "{DRIVER-PATH}"
ACCOUNT_EMAIL = "{LOGIN-USERNAME}"
ACCOUNT_PASSWORD = "{PASSWORD}"


class InternetSpeedTwitterBot:
    def __init__(self, gecko_driver_path):
        self.service = FirefoxService(executable_path=gecko_driver_path)
        self.driver = webdriver.Firefox(service=self.service)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".start-button a").click()
        sleep(60)
        self.down = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]"
                                                       "/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]").text
        self.up = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div"
                                                     "/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]").text

    def tweet_at_provider(self):
        if PROMISED_DOWN > float(self.down) or PROMISED_UP > float(self.up):
            self.driver.get("https://twitter.com")
            sleep(2)
            # self.driver.find_element(By.XPATH,
            #                          "/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div").click()
            # self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]"
            #                                    "/div[4]/span/span").click()
            self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/div/div/div/div[1]/div/"
                                               "div[3]/div[5]/a").click()
            # sleep(2)
            # self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]"
            #                                    "/a/div/span/span").click()
            sleep(5)
            username = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/"
                                                          "div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/"
                                                          "label/div/div[2]/div/input")
            username.send_keys(ACCOUNT_EMAIL)
            username.send_keys(Keys.ENTER)
            sleep(2)

            password = self.driver.find_element(By.NAME, "password")
            password.send_keys(ACCOUNT_PASSWORD)
            password.send_keys(Keys.ENTER)
            sleep(2)
            tweet = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/"
                                                       "div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/"
                                                       "div/div/div/div/div/div/div/label/div[1]/div/div/div/div/"
                                                       "div[2]/div")
            tweet.send_keys(f"Hey @suddenlink @SuddenlinkHelp why is my internet speed {self.down} down / {self.up} "
                            f"up when I pay for {PROMISED_DOWN} down / {PROMISED_UP} up?")
            sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/"
                                               "div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span"
                                               "/span").click()
            sleep(2)
            self.driver.quit()
        else:
            self.driver.quit()


bot = InternetSpeedTwitterBot(GECKO_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
