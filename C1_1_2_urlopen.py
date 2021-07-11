# 한글 출력 인코딩 관련 오류 예외 처리
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# urllib 모듈을 사용해서 이미지 다운받기, 페이지의 html 다운받기
# urlopen, read, open, write 메소드의 활용
import urllib.request as req

imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA0MDJfMjIx%2FMDAxNjE3MzYxODAyMzQy.ZA8Hyn6a8APuVHRUjngveyY105z7iaxq-gc4Bu_E5-Yg.gOU92KdGzRjSjHfiPeZyNqx4LdG7qHo0ikLwxjscLuEg.JPEG.mgc4007%2F1789228b8f750db54.jpg&type=a340"
imgPath = "D:/test1.jpg"

f = req.urlopen(imgUrl).read()
saveFile1 = open(savePath1, 'wb') # w : write, r : read, a : add / wb는 write binary의 의미를 갖는다.
saveFile1.write(f) # f.read()로 사용할 수 있음
saveFile1.close()

# f = req.urlopen(imgUrl)
# saveFile1 = open(savePath1, 'wb')
# saveFile1.write(f.read())

htmlURL = "http://google.com"
htmlPath = "D:/index.html"

f2 = req.urlopen(htmlURL).read()
with open(savePath2, 'wb') as saveFile2: # with는 with를 벗어나는 순간 자동으로 close()가 실행이 된다. = 을 as로 대체하고 순서를 바꿔준다.
    saveFile2.write(f2)

print("다운로드 완료")

# urlretrieve
# 저장 > open > 변수 할당 > 파싱 > 저장
# 파싱이 필요로 하지 않는 단순 다운로드만 필요로 하는 데이터는 반복문을 사용해서 retrieve로 다운받는다.

# urlopen
# 변수 할당 > 파싱 > 저장
# 중간 작업에서 무언가 분석하고 필요로 한 데이터를 가공할 경우에는 urlopen으로 사용한다.
