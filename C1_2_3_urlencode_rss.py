# 한글 출력 인코딩 관련 오류 예외 처리
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request as req

# urllib.parse 모듈에서 urlencode 메서드만 import 한다.
from urllib.parse import urlencode

API = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"
# 행정안전부의 게시판의 RSS 주소, XML으로 제공하고 있다

values = {
    'ctxCd': '1001'
}
# 1001번 게시판을 받아오는 Query문을 작성하기 위한 Dictionary.
# 만약 1001이 아닌 다른 값을 입력하면 다른 게시판을 받아올 수 있다.

print('before', values)
params = urlencode(values)
print('after', params)

url = API + "?" + params
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print('출력', reqData)
