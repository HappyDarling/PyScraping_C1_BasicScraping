from bs4 import BeautifulSoup
import re # regex, 정규 표현식

html = """
<html><body>
  <ul>
    <li><a id="naver" href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

test = soup.find('a', string='naver')
print(test.string)

print(soup.find(id="naver").string)

li = soup.find_all(href=re.compile(r"^https://"))
print('li', li) # list 형태
for e in li:
    print(e.attrs['href'])

li = soup.find_all(href=re.compile(r"da"))
print('li', li) # list 형태
for e in li:
    print(e.attrs['href'])
