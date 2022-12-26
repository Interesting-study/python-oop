# decorator
"""
함수를 받아 명령을 추가한 뒤 이를 다시 함수의 형태로 반환하는 함수이다.
함수의 내부를 수정하지 않고 기능에 변화를 주고 싶을 때 사용한다 .
일반적으로 함수의 전처리나 후처리에 대한 필요가 있을때 사용을 한다.
또한 데코레이터를 이용해, 반복을 줄이고 메소드나 함수의 책임을 확장한다
"""


def copyright(func):
    def new_func():
        print("@ Otter")
        func()

    return new_func


@copyright
def smile():
    print("😆")


@copyright
def angry():
    print("😡")


@copyright
def love():
    print("😘")


smile()
angry()
love()
