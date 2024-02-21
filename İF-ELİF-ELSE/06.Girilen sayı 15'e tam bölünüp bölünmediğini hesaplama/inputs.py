def get_number():
    while True:
        try:
            number = int(input("\nSayı: "))

            if number <= 0:
                raise ValueError
            else:
                return number

        except ValueError:
            print("Geçersiz sayı girdiniz")

