# 한글 출력 인코딩 관련 오류 예외 처리
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# urllib 모듈의 request를 사용해서 페이지를 읽어와서 정보를 추출한다.
import urllib.request as req

url = "http://www.encar.com/" # 원하는 임의의 사이트 하나를 입력한다.
mem = req.urlopen(url) # url 주소에 저장된 사이트에서 반환되는 정보가 mem에 할당이 된다.

print(mem) # <http.client.HTTPResponse object at 0x0000015C8E5614E0>
print(type(mem)) # <class 'http.client.HTTPResponse'>

# 파이썬의 자료형 3가지
print(type({})) # 사전 / Key - Value
print(type([])) # 배열 (list) / 값의 생성, 삭제, 수정이 가능하다
print(type(())) # 튜플 (tuple) / 값을 바꿀 수 없다

print("getUrl", mem.geturl()) # 변수에 할당한 주소를 그대로 반환한다
# String에 콤마를 찍으면 이어서 출력할 수 있다.

print("status", mem.status) # 200, 404, 403, 500
# 200은 정상, 404는 페이지가 없음, 403은 거절, 500은 서버의 에러
# status에 따라서 if 문을 구성하기 때문에 중요하다.
# Ex. 500이라면 5분 뒤에 다시 접속해보기

print("code", mem.getcode()) # status와 동일하다

print("headers", mem.getheaders())
# 페이지의 헤더를 리스트 형태로 반환한다.

print("info", mem.info())
# 헤더를 보기 편하게 줄바꿈을 해서 출력해준다.

print("read", mem.read()) # mem.read(50), 50자 까지만 읽는다.
# read안의 매개 숫자만큼 페이지의 html을 읽어온다. (매개 숫자가 없다면 전체를 읽어온다.)
# 파싱할 내용이 위쪽에 있다면 전체를 읽지 않고 적당한 부분만큼만 가져와서 처리하기 위해서 사용한다.

print("read", mem.read(50).decode("utf-8")) # euc-kr ....
# 디코딩을 해서 가져온 것이 더 좋다. 자주 붙여서 쓴다.
# 하지만 디코드를 해서 가져온다면 너무 큰 값을 한번에 읽지는 못한다.

# urllib.parse 모듈에서 urlparse 메서드만 import 한다.
from urllib.parse import urlparse

print(urlparse("http://www.encar.com/path?test=test"))
# 스키마(http), 주소(www.encar.com), path(/path), params, query(test=test, ?로 시작하는 구문), fragment를 반환한다.
