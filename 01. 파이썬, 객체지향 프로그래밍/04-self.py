"""
 [self의 이해]
 ** self는 인스턴스 객체이다!!
 ** 클래스 안에 있는 self의 주소와 만들어진 인스턴스의 주소는 같다! 즉, self는 인스턴스 그 자체이다!
"""


class SelfTest:
    # 클래스 변수, 공용
    name = "otter"

    def __init__(self, x):
        self.x = x

    # 클래스 메소드
    @classmethod
    def func1(cls):
        print(f"cls: {cls}")  # cls는 클래스 자체를 가리킨다
        print("func1")

    # 인스턴스 메소드
    def func2(self):
        print(f"self: {self}")
        print("class안의 Self 주소", id(self))
        print("func2")


test_obj = SelfTest(17)

test_obj.func2()
SelfTest.func1()
print("인스턴스의 주소 : ", id(test_obj))

test_obj.func1()
