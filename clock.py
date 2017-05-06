class Counter(object):

    def __init__(self):
        self._tick = 0

    def reset(self):
        self._tick = 0

    def tick(self):
        self._tick += 1

    def get_value(self):
        return self._tick

    def set_value(self, value):
        self._tick = value

    Value = property(fget=get_value, fset=set_value)


class Clock(object):

    Counter = [None] * 3

    def __init__(self):
        self.Counter[0] = Counter()
        self.Counter[1] = Counter()
        self.Counter[2] = Counter()

    def print(self):
        return (str(self.Counter[2].Value).zfill(2) + ":" + str(self.Counter[1].Value).zfill(2) + ":" + str(self.Counter[0].Value).zfill(2))

    def tickprocess(self):

        import time

        self.Counter[0].tick()

        time.sleep(0.1)

        if self.Counter[0].Value >= 60:
            self.Counter[1].tick()
            self.Counter[0].reset()

        if self.Counter[1].Value >= 60:
            self.Counter[2].tick()
            self.Counter[1].reset()

        if self.Counter[2].Value >= 24:
            self.Counter[2].reset()


clock = Clock()

while True:
    import os
    clock.tickprocess()
    os.system('clear')
    print(clock.print())