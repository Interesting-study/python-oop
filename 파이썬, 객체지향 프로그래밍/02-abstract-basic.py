"""
#* 추상화 : abstraction
#* 불필요한 정보는 숨기고 중요한(필요한) 정보만을 표현함으로써
#* 공통의 속성 값이나 행위(methods)를 하나로 묶어 이름을 붙이는 것이다.
"""


class Robot:
    # 클래스 변수, 인스턴스들이 공유하는 변수
    population = 0

    # 생성자, self는 각각의 인스턴스
    def __init__(self, name, code):
        self.name = name  # 인스턴스 변수
        self.code = code
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        print(f"Greeting, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    def dif(self):
        print(f"{self.name} is being destroyed!")

    # 클래스 메소드
    @classmethod
    def how_many(cls):
        print(f"We have {cls.population} robots")


# print(Robot.population)  # start = 0
siri = Robot("siri", 21039788127)
jarvis = Robot("jarvis", 2311214123)
bixvy = Robot("bixvy", 234723975)
test = Robot("test", 234723975)
# print(Robot.population)  # end = 3

print(siri.name)
print(siri.code)

siri.say_hi()


Robot.how_many()
