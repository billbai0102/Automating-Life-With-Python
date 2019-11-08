#######################################################################
# This python scripts gets the top post of the day in r/TodayILearned #
# I created this script to prototype for one of my android apps that  #
# teaches people something new every day.                             #
#   By Bill Bai                                                       #
#######################################################################

from bs4 import BeautifulSoup as bs
import requests

url = "https://www.reddit.com/r/todayilearned/top/"

headers = {"User-Agent": 'Mozilla/5.0'}
page = requests.get(url=url, headers=headers)

soHeresTheScoop = bs(page.content, 'html.parser')

hi = soHeresTheScoop.find("h3", {"class": "_eYtD2XCVieq6emjKBH3m"}).get_text()

print(hi)