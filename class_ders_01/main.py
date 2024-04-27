class Time:

    def __init__(self, hour=None, minute=None, second=None):
        self.hour = hour
        self.minute = minute
        self.second = second

    def show(self):
        print(f"Saat {self.hour}:{self.minute}:{self.second}")

    def is_later_than(self, t):
        s1 = self.hour * 60 * 60 + self.minute * 60 + self.second
        s2 = t.hour * 60 * 60 + t.minute * 60 + t.second
        return s1 > s2


t1 = Time(10, 20, 33)

t1.show()

t2 = Time(11, 10, 55)

t2.show()

print(t1.is_later_than(t2))
print(t2.is_later_than(t1))
