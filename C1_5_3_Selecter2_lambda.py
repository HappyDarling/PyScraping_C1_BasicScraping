from bs4 import BeautifulSoup

fp = open("cars.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

def car_func(selector):
    print("car_func", soup.select_one(selector).string)

car_func("#gr")
car_func("li#gr")
car_func("ul > li#gr")
car_func("#cars #gr")
# id가 cars인 자손들 중에서 id가 gr인 것
car_func("li[id='gr']")
# 배열은 속성값을 지정

print("car_func", soup.select("li")[3].string)
print("car_func", soup.find_all("li")[3].string)

##### 람다식 #####

car_lambda = lambda q : print("car_lambda", soup.select_one(q).string) # q가 Selector 선택자

car_lambda("#gr")
car_lambda("li#gr")
car_lambda("ul > li#gr")
car_lambda("#cars #gr")
car_lambda("li[id='gr']")
