import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

class SelfTest:
    def function1():
        print("function1 called!")
    def function2(self):
        print(id(f))
        print("function2 called!")

f = SelfTest()
print(dir(f))
print(id(f))

#f.function1() # Error, 반드시 self 매개 변수를 보내는데 클래스에 매개로 self가 없으므로 에러가 발생
f.function2()

print(SelfTest.function1()) # 인스턴스를 생성하지 않고 클래스에서 직접적으로 호출하면 가능
