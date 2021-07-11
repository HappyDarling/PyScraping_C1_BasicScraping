import io
import sys
import urllib.parse as rep # 주소에 한글이 포함되어 있을 경우 인코딩
import urllib.request as req
from bs4 import BeautifulSoup

from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Fake Header 정보
ua = UserAgent()

# 헤더 선언
headers = {
    'User-Agent': ua.chrome,
    'referer': 'https://finance.daum.net/'
}

base = "https://arca.live/b/epic7?target=all&keyword="
quote = rep.quote_plus("에픽")

url = base + quote

res = req.urlopen(req.Request(url, headers=headers)).read()
soup = BeautifulSoup(res, "html.parser")

str = soup.select("div.list-table > a.vrow > div.vrow-top > span.vcol.col-title > span.title")

for i, e in enumerate(str, 1):
    print(i, e.string)
