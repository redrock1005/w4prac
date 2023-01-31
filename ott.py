from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/jungseokoh/Downloads/chromedriver_mac64/chromedriver')
#암묵적으로 웹 지원 로드를 위해 3초까지 기다려준다.
driver.implicitly_wait(3)
#url에 접근한다.
driver.get("https://m.kinolights.com/title/111951")
html = driver.page_source ##페이지의 element 모두 가져오기
soup = BeautifulSoup(html, 'html.parser')

data_ott = []
otts_name = soup.select("#streamingVodList > div > div.price-item-provider > div.provider-info")
for ott_name in otts_name:
    OTTs = ott_name.select_one('p').text
    data_ott.append({'ott':OTTs})
    print(data_ott)


#OTT이미지는 어떻게 가져올지.

# data_ott_image = []
# otts_image = soup.select("#streamingVodList > div > div.price-item-provider > div.provider-info")
# for ott_image in otts_image:
#     OTTs_image = ott_image.select_one('p')
#     data_ott_image.append({'ott_image':OTTs})
#     print(data_ott_image)

