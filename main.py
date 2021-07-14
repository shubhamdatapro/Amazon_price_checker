import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

# getting the current price
amazon_item_url = "https://www.amazon.com/Ergonomic-Adjustable-computer-Portable-MacBook/dp/B08G3YGDJ1/ref=gbps_tit_m" \
                  "-9_475e_b5394718?currency=USD&language=en_US&pf_rd_i=15529609011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p" \
                  "=5d86def2-ec10-4364-9008-8fbccf30475e&pf_rd_r=X1042CC3CCA0XSCS83Z6&pf_rd_s=merchandised-search-9" \
                  "&pf_rd_t=101&smid=A2VZCCDDWQOFWP&spLa" \
                  "=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSTBES0VEVEhXS01HJmVuY3J5cHRlZElkPUEwNjM3MTk0V0ZBOTZXNlUzNUdTJmVuY3J5cHRlZEFkSWQ9QTAwNjk1ODIzTzRJRlY1Q0w5TDdJJndpZGdldE5hbWU9c3BfZ2JfbWFpbl9zdXBwbGUmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl "
header = {
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/88.0.4324.190 Safari/537.36 "
}
response = requests.get(url=amazon_item_url, headers=header)
page_html = response.text
soup = BeautifulSoup(page_html, "lxml")
current_price = soup.find(name="span", id="priceblock_dealprice").get_text()
str_value = current_price[1:]  # help to remove $
current_value = float(str_value)


# initilize smtp server
def sendmail():
    username = "smart.dummy96@gmail.com"
    password = "Shubham@123"
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=username, password=password)

        connection.sendmail(from_addr="smart.dummy96@gmail.com", to_addrs="smartyshub5@gmail.com",
                            msg=f"subject:Hello\n\ngo grab your item its less than your cutoff price current_price is {current_value}, {amazon_item_url}")


if current_value < 60.0:
    sendmail()

# automate this code to run daily on cloud platform but main data should be hidden.
