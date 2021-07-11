from bs4 import BeautifulSoup

fp = open("food-list.html", encoding="utf-8")
# 내장 메모리에서 HTML을 불러오고 한글로 되어있기 때문에 인코딩까지 해준다
soup = BeautifulSoup(fp, "html.parser")

print(soup)

print("1", soup.select("li:nth-of-type(4)")[1].string)
# nth-of-type : 직계 자식들 중에서 내가 원하는 순서를 지정해서 가져온다

print("2", soup.select_one("#ac-list > li:nth-of-type(4)").string)
# 자식 선택자는 본인의 자식만 선택 ( > )
# 자손 선택자는 자식의 자식도 조건이 맞다면 모두 선택한다 (띄어쓰기 )

print("3", soup.select("#ac-list > li[data-lo='cn']")[0].string)
# 조건에 맞는 Element를 List형태로 반환한다
# 배열, 인덱스로 접근을 해야 한다 (조건에 맞는 원소가 하나일 때도 배열로 접근해야 한다)

print("4", soup.select("#ac-list > li.alcohol.high")[0].string)
# html에서는 CSS이름을 띄어쓰기로 구분할 수 있지만 선택자로 할 때는 온점을 찍어야 하고 ID 값은 #을 넣어야 한다

param = {"data-lo": "cn", "class": "alcohol"}
print("5", soup.find("li", param).string)
# Dictionary의 형태도 들어갈 수 있다

print("6", soup.find(id="ac-list").find("li",param).string)
# 이 방법은 정석적인 접근이지만, 우리는 많은 정보를 알고 있기 때문에 5번의 형태가 바람직하다

for ac in soup.find_all("li"):
    if ac['data-lo'] == 'us':
        print('data-lo == us', ac.string)
