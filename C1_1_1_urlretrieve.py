# 한글 출력 인코딩 관련 오류 예외 처리
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# urllib 모듈을 사용해서 이미지 다운받기, 페이지의 html 다운받기
# urlretrieve 메소드의 활용
import urllib.request as req

imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA0MDJfMjIx%2FMDAxNjE3MzYxODAyMzQy.ZA8Hyn6a8APuVHRUjngveyY105z7iaxq-gc4Bu_E5-Yg.gOU92KdGzRjSjHfiPeZyNqx4LdG7qHo0ikLwxjscLuEg.JPEG.mgc4007%2F1789228b8f750db54.jpg&type=a340"
# 크롬 개발자 도구에서 이미지의 주소를 받아와서 imgUrl 변수에 저장한다.
imgPath = "D:/test1.jpg"
# 컴퓨터에 저장하고자 하는 경로를 변수에 저장한다
req.urlretrieve(imgUrl, imgPath)
# urlretrieve 메소드를 사용해서 저장한다

htmlURL = "http://google.com"
# 저장하고 싶은 페이지의 주소를 htmlURL 변수에 저장한다.
htmlPath = "D:/index.html"
# 컴퓨터에 저장하고자 하는 경로를 변수에 저장한다
req.urlretrieve(htmlURL, htmlPath)
# urlretrieve 메소드를 사용해서 저장한다

print("다운로드 완료")
