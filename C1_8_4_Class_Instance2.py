import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

class NameTest:
    total = 0 # 클래스에 전역변수 하나를 선언해준다.

print(dir()) # dir() 내장 함수는 어떤 객체를 인자로 넣어주면 해당 객체가 어떤 변수와 메소드(method)를 가지고 있는지 나열해줍니다.

print("before : ", NameTest.__dict__) # 클래스의 total은 0으로 선언되어 있다.
NameTest.total = 1
print("after : ", NameTest.__dict__) # 클래스의 total은 1으로 선언되어 있다.

n1 = NameTest() # NameTest의 객체를 선언한다
n2 = NameTest() # NameTest의 객체를 선언한다

print(id(n1), "vs", id(n2))
print(dir())

print(n1.__dict__) # 객체에 할당된 변수의 값이 없으므로 아무것도 출력되지 않는다.
print(n2.__dict__) # 객체에 할당된 변수의 값이 없으므로 아무것도 출력되지 않는다.

n1.total = 77 # n1의 total 값을 77으로 설정해준다.
print(n1.__dict__) # 설정된 total의 값을 출력해준다.

print(n1.total) # 본인에게 설정된 인스턴스 변수인 total 값이 있으므로 우선적으로 77이 출력된다.
print(n2.total) # 본인에게 설정된 인스턴스 변수 값이 없으므로 클래스 변수 값인 1이 출력된다.
print(n2.next) # 본인에게 설정된 인스턴스 변수 값도 없고 클래스에도 값이 없기 때문에 에러가 출력된다.
