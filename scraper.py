import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/FEICE-Stainless-Leathers-Waterproof-Business/dp/B074MWWTVL'
desiredPrice = 110
headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content ,features='lxml')

currentPrice = soup.select("#priceblock_saleprice")[0].get_text().strip()
convertedPrice = float(currentPrice[1:len(currentPrice)])


if convertedPrice <= desiredPrice:
    print("Sale is on!!!")
else:
    print("no sale")
