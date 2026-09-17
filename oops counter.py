class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1

c1 = Counter()
c1.increment()
c1.increment()
c1.increment()
print(c1.count)