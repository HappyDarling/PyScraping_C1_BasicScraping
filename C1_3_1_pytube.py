# pytube 설치 / pip install git+git://github.com/nficano/pytube
# 설치되어 있는 pip 확인 / conda list
# 파이썬 3.6 이상

import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=ksAd0GjaDXk&t=29s&ab_channel=%E9%AC%B1P%2FUtsu-P")
# 다운 받을 동영상 URL 지정

videos = yt.streams
#print('videos', videos)
# 다운로드 받을 수 있는 선택을 제공한다. 확장자, 화질 등의 선택지를 제공해준다.

for i in range(len(videos)): # videos의 길이만큼 반복문을 시행한다. (0부터 시작)
    print(i, ' , ', videos[i])

down_dir = "D:\Django\workspace\WebCrawling\Youtube" # 동영상을 다운로드할 경로를 지정한다.
videos[0].download(down_dir) # Youtube에 업로드되어있는 파일 이름으로 저장이 된다.

# 수동으로 변환하고 싶다면 ffmpeg을 cmd에서 경로를 잡아준 다음
# ffmpeg -i "동영상 이름" "새로운 파일명" 으로 변환해준다.
