from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "{EMAIL-ADDRESS}"
ACCOUNT_PASSWORD = "{EMAIL-PASSWORD}"

gecko_driver_path = "{DRIVER-PATH}"
service = FirefoxService(executable_path=gecko_driver_path)
driver = webdriver.Firefox(service=service)

driver.get("{URL}")

time.sleep(2)
driver.find_element(By.LINK_TEXT, "Sign in").click()

time.sleep(3)
username = driver.find_element(By.ID, "username")
username.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")


