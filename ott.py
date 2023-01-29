import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://m.kinolights.com/title/111951', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

price_provider = soup.select('.provider-info')
for item in price_provider:
    print(item)

#dddddgit add .Wndtjrdh2@