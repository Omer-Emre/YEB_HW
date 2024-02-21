class calculation_time_wage:

    def __init__(self, wage, year):
        self.wage = wage
        self.year = year

    def calculation_time_10(self):
        multiplacition = self.wage * 0.10
        return multiplacition + self.wage

    def calculation_time_15(self):
        multiplacition = self.wage * 0.15
        return multiplacition + self.wage

    def calculation_time_25(self):
        multiplacition = self.wage * 0.25
        return multiplacition + self.wage
