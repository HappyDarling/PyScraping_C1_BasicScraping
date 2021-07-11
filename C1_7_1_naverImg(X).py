import io
import sys
import urllib.parse as rep
import urllib.request as req
import io
import os
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

headers = {
    'User-Agent': UserAgent().chrome,
    'referer': 'https://finance.daum.net/'
}

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("사자")
url = base + quote

res = req.urlopen(req.Request(url, headers=headers))
savePath = "D:\Django\workspace\WebCrawling\C1_BasicScraping\imageDown"

try:
    if not (os.path.isdir(savePath)):
        os.mkdir(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")

print(soup)

img_list = soup.select("div.photo_group._listGrid > div.photo_tile._grid > div > div > div.thumb > a > img")

for i, img_list in enumerate(img_list, 1):
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    req.urlretrieve(img_list['data-source'], fullFileName)
