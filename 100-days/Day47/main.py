from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

URL = "https://www.amazon.com/Beats-Studio-Cancelling-Earbuds-Built-Bluetooth-Headphones/dp/B096SV8SJG/ref=sr_1_3?crid=3O3JQLLVAEWDL"
MY_EMAIL = "{EMAIL ADDRESS}"
MY_PASSWORD = "{PASSWORD}"
TARGET_PRICE = 125
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0"
accept_language = "en-US,en;q=0.5"
header = {"User-Agent": user_agent, "Accept-Language": accept_language}
response = requests.get(URL, headers=header)
# print(response.content)

amazon_webpage = response.text
soup = BeautifulSoup(amazon_webpage, "lxml")
# print(soup.prettify())
price = soup.find(name="span", class_="a-offscreen").get_text()
price_list = price.split('$')[1]
float_price = float(price_list)
# print(float_price)

if float_price < TARGET_PRICE:

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="{TO_EMAIL_ADDRESS}",
            msg=f"Subject:Amazon Price Alert\n\nEarbuds are below your target price of $125.00 go to {URL}\nSeth"
        )
