# 실시간 검색어 크롤링
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

driver.get(f'https://datalab.naver.com/keyword/realtimeList.naver?where=main')

# 전체연령만 나오게 css셀렉터 수정하기
words = driver.find_elements_by_css_selector(
    '#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul > li > a > span')
texts = [word.text for word in words]

print("마블리의 급상승 검색어♥")
for n in range(0, len(texts)):
    print("%d"%(n+1) + "." + " " + texts[n])


driver.quit()
