from bs4 import BeautifulSoup

# """ 쌍따옴표 3개를 사용하면 줄바꿈이 포함된 문자열을 생성할 수 있다.
html = """
<html>
    <body>
        <h1>파이썬 BeautifulSoup 공부</h1>
        <p>태그 선택자</p>
        <p>CSS 선택자</p>
    </body>
</html>
"""

# BeautifulSoup객체를 초기화, 첫 번째 매개에는 html을, 두번째에는 parser를 지정한다.
soup = BeautifulSoup(html, 'html.parser')

# print('soup', type(soup))
# print('prettify', soup.prettify()) # 들여쓰기를 사용해서 출력을 해준다.

h1 = soup.html.body.h1
print('h1', h1) # 아직 Class 객체로 가져와진다.
print(h1.string) # 스트링 형태로 가져오는 방법

p1 = soup.html.body.p
print('p1', p1) # 직접 접근을 활용하면 가장 앞에 나온 p가 출력됨을 알 수 있음

p2 = p1.next_sibling
print('p2', p2) # 공백이 출력되는 이유는 줄바꿈이 있기 때문에 줄바꿈 문자에 접근한다.
# 원래는 줄바꿈 문자나 공백을 제거해야 원하는 데이터에 접근할 수 있음

p2 = p2.next_sibling # 다음 p에 접근하기 위해서 한번 더 next 메소드를 사용
print('p2', p2)

p3 = p1.previous_sibling.previous_sibling
print('p3', p3)

print("h1 >> ", h1.string)
print("p1 >> ", p1.string)
print("p2 >> ", p2.string)

# 하지만 이러한 방법은 중간에 페이지가 수정되면 무용지물이 되기 때문에 사용하지 않는다
