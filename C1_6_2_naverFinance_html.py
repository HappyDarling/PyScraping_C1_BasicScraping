import io
import sys
import urllib.request as req
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "https://finance.naver.com/sise/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

# 선택자 방법 1
top5 = soup.select("#siselist_tab_0 > tr")

i = 1
for e in top5:
    if e.find("a") is not None:
    # top에 리스트 형식으로 저장되어 있는 모든 tr 태그들을 대상으로 IF문을 시행한다.
    # 만약 a 태그가 없다면 None 형식을 리스트에 반환되고 None이 아닌 것을 대상으로 한다.
        print(i, e.select_one(".tltle").string)
        i += 1

# 선택자 방법 2
top5_1 = soup.select("#siselist_tab_0 > tr > td > a")
for e2 in top5_1:
    print(e2.string)
