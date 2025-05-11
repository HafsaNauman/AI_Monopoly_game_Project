from random import randint

class Throw:
    """Stores each die roll and total."""
    def __init__(self, n=2):
        self.values = []
        self.double = True
        for _ in range(n):
            v = randint(1, 6)
            if self.values and v != self.values[-1]:
                self.double = False
            self.values.append(v)
        self.amount = sum(self.values)

    def get_amount(self):
        return self.amount

    def is_double(self):
        return self.double

    @classmethod
    def simple_amount(cls, n=2):
        """Quick total without tracking faces."""
        return sum(randint(1,6) for _ in range(n))
