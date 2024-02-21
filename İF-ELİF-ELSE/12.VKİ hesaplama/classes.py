class calculator_vki:
    def __init__(self, size, weight):
        self.size = size
        self.weight = weight

    def calculator(self):
        return self.weight / (self.size * self.size)
