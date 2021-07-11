# 한글 출력 인코딩 관련 오류 예외 처리
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request as req

# urllib.parse 모듈에서 urlencode 메서드만 import 한다.
from urllib.parse import urlencode

API = "https://api.ipify.org"

values = {
    'format': 'json' # json, jsonp
}

print('before', values)
params = urlencode(values)
print('after', params)
# values dictionary에 두개 이상의 변수를 할당하면 format=json&format2=jsonp 형식으로 인코딩된다.

url = API + "?" + params # https://api.ipify.org?format=json
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print('출력', reqData)
