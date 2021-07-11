# URL 주소를 사용자에게 입력받아 MP3로 변환하는 코드
# 동영상 주소 여러개를 한번에 입력받아 mp3로 변환하는 코드
# 무조건 mp3로 변환하는 것이 아니라 동영상을 다운로드 후에 mp3로 변환할지 여부를 입력받아서
# 변환하고 싶다고 하면 mp3 이름을 입력받아 변환하고 아니라면 종료

import pytube
import os
import subprocess

down_dir = "D:\Django\workspace\WebCrawling\Youtube"
ytlinks = []
videos = [] # 비디오 개수 / 화

while True:
    cNum = input("다운 받을 링크는? (0 입력시 종료)")
    if cNum == '0':
        break
    ytlinks.append(cNum)

# 비디오 배열에 영상 주소들을 저장
for i in range(len(ytlinks)):
    yt = pytube.YouTube(ytlinks[i])
    videos.append(yt.streams)

while True:
    select = input("선택 [1: 동영상 / 2: MP3] : ")
    if select == '1':
        break
    if select == '2':
        break
    else:
        print("다시 입력해주세요")

if select == '1':
    for i in range(len(videos[0])):
        print(i, ' , ', videos[0][i])
    cNum = int(input("다운 받을 화질은? (0 ~ 21 입력) "))
    for j in range(len(videos)):
        videos[j][cNum].download(down_dir)
    print("동영상 다운로드 완료!")


if select == '2':
    for i in range(len(videos)):
        videos[i][0].download(down_dir)
        oriFileName = videos[i][0].default_filename
        print("기존 파일명 : ", oriFileName)
        newFileName = input("변환 할 mp3 파일명은? (.mp3 입력) ")
        subprocess.call(['ffmpeg', '-i',
            os.path.join(down_dir, oriFileName),
            os.path.join(down_dir, newFileName)
        ])
    print("동영상 다운로드 및 mp3 변환 완료!")
