# 한글 출력 인코딩 관련 오류 예외 처리
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request as req

imgUrl = "https://ssl.pstatic.net/tveta/libs/1345/1345335/014e226b027b9f5fbeda_20210629110713733.jpg"
imgPath = "D:/adPic.jpg"
req.urlretrieve(imgUrl, imgPath)

movieUrl = "https://tvetamovie.pstatic.net/libs/1339/1339095/4a540861ff41e0d83f7c_20210702184036435.mp4-pHIGH-v0-f136267-20210702184136066_1.mp4"
moviePath = "D:/adMovie.mp4"
req.urlretrieve(movieUrl, moviePath)

print("다운로드 완료")
