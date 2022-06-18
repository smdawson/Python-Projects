from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By

gecko_driver_path = "{DRIVER-PATH}"
service = FirefoxService(executable_path=gecko_driver_path)
driver = webdriver.Firefox(service=service)

driver.get("https://www.python.org")
# price = driver.find_element(By.CLASS_NAME, "a-price")
# print(price.text)
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))

# bug_link = driver.find_element(By.XPATH, "/html/body/div/footer/div[2]/div/ul/li[3]/a")
# print(bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_descriptions = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_descriptions[n].text,
    }
print(events)

# driver.close()
driver.quit()
