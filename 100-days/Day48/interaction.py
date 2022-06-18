from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

gecko_driver_path = "{DRIVER-PATH}"
service = FirefoxService(executable_path=gecko_driver_path)
driver = webdriver.Firefox(service=service)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# driver.get("https://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# first_name = driver.find_element(By.NAME, "fName")
# first_name.send_keys("{FIRST-NAME}")
# last_name = driver.find_element(By.NAME, "lName")
# last_name.send_keys("{LAST-NAME}")
# input_email = driver.find_element(By.NAME, "email")
# input_email.send_keys("nonya@business.com")
# submit = driver.find_element(By.CSS_SELECTOR, "form button")
# submit.send_keys(Keys.ENTER)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

time_end = time.time() + 60
while time.time() < time_end:
    driver.find_element(By.ID, "cookie").click()

# driver.quit()