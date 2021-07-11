# 2019-01-28 수정
# 기존 daum 주식 사이트 : ajax 방식으로 변경으로 인해 이를 반영한 코드를 수정.
# pip install fake-useragent 설치 후 실행 가능

import io
import json
import sys
import urllib.request as req

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

# 다음 주식 요청 URL
url = "https://finance.daum.net/api/domestic/trend/price_performance/?pagination=true&perPage=5&changeType=RISE"
# API를 가져오는 방법
# F12로 개발자 도구를 진입한 후 Network를 켠 뒤 새로고침을 해서 정보를 받아온다.
# Filter를 클릭해서 필터탭을 열은 뒤 XHR을 눌러서 XHR만 나타나게 변경한다.
# Filter로 걸러진 것들을 하니씩 클릭해서 Preview를 확인하고 원하는 값이 있는 것을 찾아서 API를 찾아낸다.

# print(request.get_method())   #Post or Get 확인
# print(request.get_full_url()) #요청 Full Url 확인

# 요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')

# 응답 데이터 확인(Json Data)
# print('res', res)

# 응답 데이터 str -> json 변환
rank_json = json.loads(res)['KOSPI'] # Preview를 확인해서 원하는 저장 값을 저장

# 중간 확인
print('중간 확인 : ', rank_json, '\n')

for elm in rank_json:
    # print(type(elm)) #Type 확인
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(elm['rank'], elm['tradePrice'], elm['name']), )
