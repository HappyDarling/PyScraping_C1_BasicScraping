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
url = "https://www.inflearn.com/"

res = req.urlopen(req.Request(url, headers=headers))
savePath = "D:\Django\workspace\WebCrawling\C1_BasicScraping\imageDown\\"

try:
    if not (os.path.isdir(savePath)):
        os.mkdir(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")

img_list = soup.select("div.swiper-wrapper > div > div.card.course.course_card_item > a.course_card_front")

for i, e in enumerate(img_list, 1):
    with open(savePath+"text_"+str(i)+".txt","wt") as f:
    # 저장할 경로에 "text_순번.txt"의 이름으로 텍스트를 저장한다. 텍스트 쓰기 모드 (wt)
        f.write(e.select_one("div.card-content > div.course_title").string)

    fullFileName = os.path.join(savePath, savePath+str(i)+'.png')

    imgUrl = e.select_one("div.card-image > figure > img")['src']
    base = rep.urljoin(imgUrl, "../../../../../")

    parseUrl = rep.urlparse(imgUrl).path
    path = rep.quote(parseUrl)

    fullURL = rep.urljoin(base, path)

    #request_url = req.Request(fullURL, None, headers)
    #response_url = req.urlopen(request_url)
    #f = open(fullFileName, 'wb')
    #f.write(response_url.read())
    #f.close()

    print(imgUrl)
    print(fullURL)

    #req.urlretrieve(imgUrl, fullFileName)
