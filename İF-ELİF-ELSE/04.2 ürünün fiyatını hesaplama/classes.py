class calculation_products:
    def __init__(self, product_1, product_2):
        self.product_1 = product_1
        self.product_2 = product_2

    def calculation(self):
        return self.product_1 + self.product_2

    def calculation_discount(self):
        add = (self.product_1 + self.product_2) * 0.25
        return (self.product_1 + self.product_2) - add

