from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

ACCOUNT_EMAIL = "{EMAIL-ADDRESS}"
ACCOUNT_PASSWORD = "{EMAIL-PASSWORD}"

gecko_driver_path = "{DRIVER-PATH}"
service = FirefoxService(executable_path=gecko_driver_path)
driver = webdriver.Firefox(service=service)

driver.get("https://tinder.com/")

time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button").click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)

time.sleep(2)
username = driver.find_element(By.ID, "email")
username.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(By.ID, "pass")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)
driver.switch_to.window(base_window)
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/button").click()
time.sleep(2)

for n in range(100):

    time.sleep(1)

    try:
        print("called")
        driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button"
        ).click()
        time.sleep(2)
    except ElementClickInterceptedException:
        try:
            driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")

        except NoSuchElementException:
            time.sleep(2)

driver.quit()
