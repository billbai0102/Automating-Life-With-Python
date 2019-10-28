from bs4 import BeautifulSoup
import requests
import smtplib
import time

def send_alert(username, password, url, itemTitle, trackingPrice):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(username, password)
    subject = "ALERT! " + itemTitle + " has dropped below $" + str(trackingPrice)
    body = "Hurry up and get it!\n\nIn case you forgot, here's the link\n" + url
    server.sendmail(
        username,
        username,
        f"Subject: {subject}\n\n{body}"
    )

    server.quit()



url = input("Enter the URL for the product you'd like to track: ")
# url = 'https://www.ebay.com/itm/Air-Jordan-10-Retro-Size-11-5-310805-100/123951235782?_trkparms=ispr%3D1&hash=item1cdc11c2c6:g:G5oAAOSws65dsham&enc=AQAEAAACMBPxNw%2BVj6nta7CKEs3N0qUYhwoM2mWtrgI73vbJHk0aBVuFuzH91RoUrw8lCZ1sCbCyuFuBkwnF3hp5Hx%2BmVzRQLOwtD4vUk2xwst7xzyseVEpMNgsY0cc%2FJv7idx%2B%2BWUy0hiknue7jhhxkviQfKi6y1pfMYolPXMwUZI98rumF8ELyJp1i3zMEkT8eX74mnkvxzC16OrE%2FosOlusOTO0Qzr1XIfFu%2Fd6AC%2FaW6vbjYBi0VQbTIq%2BkTbUzdZfP0FKiFl8IoBA4aOp1WCXcDDj2xD8fYSH99vE0te863NfN4mZkfWNYvecPtNN6SvOUxwsW0vG11z8Afrb0xQp6irJdqjxxFcc4tolknI9PYWeV3%2BrLN2yYgLddtTbdCFcmcs0caT4xeV7OThMcJy%2FF0OQqONe4uY8lZqPJbRoIUiDbdO04j8ymyhC%2BsPYIyc09lrvZUMy%2By18lVjV18WvyiNX8A%2FHz2pfFFn66Y%2Bunez%2FcODQ6duaRQ9JY2zHkG0mJl0DUztbLnrMWo0%2F%2F7VF8Ycbbf4wAuPy5YTA1pMKC%2BxsY1EWzfAHv42yQ6kQ1y%2Bv45lFz8vbFywD6xSc5rAYOhynRVhQy15IZQ05fub09CQBZbeFWB2S2%2F2Fg3MqS%2FycjHLuWh0du1OZCxbtPTI8jhbu%2BkgHQVacBP%2BlTxSEzBBLrTjUnnyfxz%2BJxtVLh%2F%2BX9b%2BhZHajm9PHuHYozbWIZC3OXWhNYviqMgDt6EEvha8xCz&checksum=12395123578284edf16a06f84e9eb0aa2d1a8d3f47b0&enc=AQAEAAACMBPxNw%2BVj6nta7CKEs3N0qUYhwoM2mWtrgI73vbJHk0aBVuFuzH91RoUrw8lCZ1sCbCyuFuBkwnF3hp5Hx%2BmVzRQLOwtD4vUk2xwst7xzyseVEpMNgsY0cc%2FJv7idx%2B%2BWUy0hiknue7jhhxkviQfKi6y1pfMYolPXMwUZI98rumF8ELyJp1i3zMEkT8eX74mnkvxzC16OrE%2FosOlusOTO0Qzr1XIfFu%2Fd6AC%2FaW6vbjYBi0VQbTIq%2BkTbUzdZfP0FKiFl8IoBA4aOp1WCXcDDj2xD8fYSH99vE0te863NfN4mZkfWNYvecPtNN6SvOUxwsW0vG11z8Afrb0xQp6irJdqjxxFcc4tolknI9PYWeV3%2BrLN2yYgLddtTbdCFcmcs0caT4xeV7OThMcJy%2FF0OQqONe4uY8lZqPJbRoIUiDbdO04j8ymyhC%2BsPYIyc09lrvZUMy%2By18lVjV18WvyiNX8A%2FHz2pfFFn66Y%2Bunez%2FcODQ6duaRQ9JY2zHkG0mJl0DUztbLnrMWo0%2F%2F7VF8Ycbbf4wAuPy5YTA1pMKC%2BxsY1EWzfAHv42yQ6kQ1y%2Bv45lFz8vbFywD6xSc5rAYOhynRVhQy15IZQ05fub09CQBZbeFWB2S2%2F2Fg3MqS%2FycjHLuWh0du1OZCxbtPTI8jhbu%2BkgHQVacBP%2BlTxSEzBBLrTjUnnyfxz%2BJxtVLh%2F%2BX9b%2BhZHajm9PHuHYozbWIZC3OXWhNYviqMgDt6EEvha8xCz&checksum=12395123578284edf16a06f84e9eb0aa2d1a8d3f47b0'
trackingPrice = float(input("Input the desired price of the product: "))
# trackingPrice = 120
email = input("What is your email: ")
# email = 'billbai0102@gmail.com'
appPassword = input("What is your app password: ")
# appPassword = '[REDACTED]'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

page = requests.get(url=url, headers=headers)

bs = BeautifulSoup(page.content, 'html.parser')

price = float(bs.find(id='prcIsum').get_text()[4:])
itemTitle = bs.find(id='itemTitle').get_text()[16:]

print("The script is currently running. You will be notified when the price has dropped.")

while(1):
    if(price < trackingPrice):
        send_alert(email, appPassword, url, itemTitle, trackingPrice)
        break
    time.sleep(60)

print("Message has been sent.")