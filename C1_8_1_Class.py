import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

class UserInfo:
    def __init__(self, name, phone): # 생성자
        self.name = name
        self.phone = phone

    def set_info(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("------------")
        print("Name: " + self.name)
        print("Phone: " + self.phone)
        print("------------")

    def __del__(self): # 소멸자
        print("소멸자")

user1 = UserInfo("kim", "010-3433-7777")
user2 = UserInfo("park", "010-4466-7777")

print(id(user1))
print(id(user2))

#user1.set_info("kim", "010-3433-7777")
#user2.set_info("park", "010-4466-7777")

user1.print_info()
user2.print_info()

print(user1.__dict__) # {'name': 'kim', 'phone': '010-3433-7777'}
print(user2.__dict__) # {'name': 'park', 'phone': '010-4466-7777'}

print(user1.name, user1.phone)
