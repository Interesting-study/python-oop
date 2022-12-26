"""
#* namespace : 개체를 구분할 수 있는 범위
#* __dict__ : 네임스페이스를 확인할 수 있다.
#* dir() : 네임스페이스의 key 값을 확인할 수 있다.
#* __doc__ : class의 주석을 확인한다.
#* __class__ : 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다.
"""


class Robot:
    # 클래스 변수, 인스턴스들이 공유하는 변수
    population = 0

    # 생성자, self는 각각의 인스턴스
    def __init__(self, name):
        self.name = name  # 인스턴스 변수
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

    @staticmethod
    def this_is_robot_class():
        print("Yes!")


siri = Robot("siri")
jarvis = Robot("jarvis")
bixvy = Robot("bixvy")

print(Robot.__dict__)
print(siri.__dict__)
print(jarvis.__dict__)

print(siri.name)
print(bixvy.name)


siri.cal_add(2, 3)
print(siri.population)

siri.how_many()

# 동일한 코드
Robot.say_hi(self=siri)
siri.say_hi()

print(dir(siri))
siri.this_is_robot_class()
