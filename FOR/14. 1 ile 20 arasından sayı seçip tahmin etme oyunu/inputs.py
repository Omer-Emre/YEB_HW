def get_number():
    while True:
        try:
            number = int(input("\n(1-20) arası bir sayı girin: "))

            if number <= 0 or number > 20:
                raise ValueError

            else:
                return number

        except ValueError:
            print("Geçersiz sayı girdiniz")
