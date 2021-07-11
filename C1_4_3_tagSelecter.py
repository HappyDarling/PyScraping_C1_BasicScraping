# 태그 선택자를 활용

from bs4 import BeautifulSoup

html = """
<html>
    <body>
      <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="https://www.google.com">google</a></li>
        <li><a href="https://www.tistory.com">tistory</a></li>
      </ul>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a") # 해당 태그를 가지고 있는 것들을 변수에 모두 담음
#print('links', type(links)) # element의 resultset

for a in links:
    # print('a', type(a), a)
    href = a.attrs['href'] # Dictionary 형식이기 때문에 Key인 href 를 입력하면 원하는 URL 값이 할당이 된다
    txt = a.string
    #print('txt >> ', txt, 'href >> ', href)

a = soup.find_all("a", string="daum") # a 태그의 String이 daum인 모든 것들을 가져온다.
print('a', a)

# find는 가장 상위의 하나만 출력한다.

a = soup.find_all("a", limit=3)
# 가져오는 갯수에 제한을 걸어서 가져온다
# 리미트가 0일 경우에는 무제한
print('a', a)

a = soup.find_all(string=["naver", "google"])
# 내용을 가져오는 것이 아니라 해당 String을 가져온다
print('a', a)
