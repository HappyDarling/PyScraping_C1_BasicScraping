# CSS 선택자를 활용

from bs4 import BeautifulSoup

html = """
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs">
    <li>Java 초고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.select("div#main > h1")
print('h1', h1) # 선택자로 가져온 Type은 List이다.
# print(h1.string) # 따라서 이렇게 접근할 수 없고

for z in h1: # 리스트의 원소가 하나일 때도 반드시 반복문으로 접근해야 한
    print(z.string)

h1 = soup.select_one("div#main > h1")
print('h1', h1.string) # 혹은 select_one을 사용한다

# li 의 모든 값을 가져오기

list_li = soup.select("div#main > ul.lecs > li")
# #main > .lecs > li 이렇게 해도 상관 없지만 더 정확하게 하기 위해서 모두 명시해주는 것이 좋다
# id 는 #, class는 .

for li in list_li:
    print("li >> ", li.string)
