class Accumulator:

    def __init__(self):
        self._count = 0

    @property
    def count(self):
        return self.count

    def add(self, more = 1):
        self._count += 1