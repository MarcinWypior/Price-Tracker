from bs4 import BeautifulSoup
import requests
import smtplib

my_email = "marcin1java@gmail.com"
password = "bczgqfrnpqxexekd"

response = requests.get(url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",
                        headers={
                            "Content-Type": "text",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
                            "Accept-Language": "en-US,en;q=0.5",

                        })

soup = BeautifulSoup(response.text, "html.parser")

print(soup)
print("\n\n\n")
# print(soup.find_all(name="div",class_="a-section a-spacing-none aok-align-center aok-relative"))
div = soup.find_all(name="div", id="corePriceDisplay_desktop_feature_div")
# price_whole = soup.find_all(name="span", class_="a-price-whole")
# price_fraction = soup.find_all(name="span", class_="a-price-whole")
#
# print(price_fraction,",",price_whole)
try:
    price_whole = div[0].find_all(name="span", class_="a-price-whole")[0].text.replace(".","")
    price_fraction = div[0].find_all(name="span", class_="a-price-fraction")[0].text.replace(".","")
    price = float(price_whole) + float(price_fraction) / 100
    print(price)
except IndexError:
    print("0 elements in list")
    price = 0





print("\n\n\n")
if price < 50:
    print("attempt to send email")
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.ehlo()
        connection.login(user=my_email, password=password)
        result = connection.sendmail(from_addr=my_email,
                            to_addrs="marcin1java@op.pl",
                            msg=f"Subject:Item below regular price \n\n https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
        connection.close()

    print(result, "was email send ?")