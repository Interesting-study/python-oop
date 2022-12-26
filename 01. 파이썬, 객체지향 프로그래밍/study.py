class Cal:
    # 생성자
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


cal1 = Cal(1, 2)

print(cal1.a)
print(cal1.b)
print(cal1.add())
print(cal1.sub())
print(cal1.mul())
print(cal1.div())
