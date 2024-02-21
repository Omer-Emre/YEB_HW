class calculator_big_number:
    def __init__(self, number_1, number_2, number_3):
        self.number_1 = number_1
        self.number_2 = number_2
        self.number_3 = number_3

    def calculator(self):
        return max(self.number_1, self.number_2, self.number_3)
