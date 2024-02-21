def get_product(product):
    while True:
        try:
            products = float(input(str(product) + ".ürün: "))

            if products <= 0:
                raise ValueError
            else:
                return products

        except ValueError:
            print("Geçersiz fiyat girdiniz")
