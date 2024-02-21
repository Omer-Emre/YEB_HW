def get_parking():
    while True:
        try:
            parking = float(input("\nKaç saat istersiniz?: "))

            if parking <= 0:
                raise ValueError
            else:
                return parking

        except ValueError:
            print("Geçersiz saat girdiniz")
