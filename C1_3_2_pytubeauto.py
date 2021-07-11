import pytube
import os
import subprocess # Command 환경을 사용하기 위해서 사용한다.

yt = pytube.YouTube("https://www.youtube.com/watch?v=vrmH0pRjUA4&ab_channel=%ED%8C%80%ED%8C%8C%EB%9E%91%EC%83%88")
videos = yt.streams

for i in range(len(videos)):
    print(i, ' , ', videos[i])

cNum = int(input("다운 받을 화질은? (0 ~ 21 입력)"))
# 사용자에게 입력받아서 형변환을 해서 cNum에 할당해준다.

down_dir = "D:\Django\workspace\WebCrawling\Youtube"
videos[cNum].download(down_dir)

newFileName = input("변환 할 mp3 파일명은?")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg', '-i',
    os.path.join(down_dir, oriFileName),
    os.path.join(down_dir, newFileName)
])

print("동영상 다운로드 및 mp3 변환 완료!")

# 환경변수에 ffmpeg을 등록하지 않았다면 ffmpeg이 있는 위치로 py파일을 이동시키고 cmd에서 이동한 다음 실행한다.
