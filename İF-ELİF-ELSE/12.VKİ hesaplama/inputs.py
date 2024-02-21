def get_size_and_weight():

    def get_size():
        while True:
            try:
                size = float(input("\nBoy: "))

                if size <= 0.50 or size > 2.51:
                    raise ValueError
                else:
                    return size

            except ValueError:
                print("Geçersiz boy girdiniz")

    def get_weight():
        while True:
            try:
                weight = int(input("Kilo: "))

                if weight < 3 or weight > 727:
                    raise ValueError
                else:
                    return weight

            except ValueError:
                print("Geçersiz kilo girdiniz")

    return get_size, get_weight
