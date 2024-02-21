def get_numbers():
    while True:
        try:
            number = int(input("Sayı: "))

            if number == 0:
                raise ValueError
            else:
                return number

        except ValueError:
            print("Geçersiz sayı girdiniz")
