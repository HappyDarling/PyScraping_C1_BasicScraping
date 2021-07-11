import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 클래스 변수, 인스턴스 변수

class Warehouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1
    def __del__(self):
        warehouse.stock_num -= 1

user1 = Warehouse('kim')
user2 = Warehouse('park')

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__) # 인스턴스의 네임스페이스를 확인한 후 클래스의 네임스페이스를 찾는다. # 클래스 변수는 공유된다.
print(user1.stock_num)
print(user2.stock_num)
