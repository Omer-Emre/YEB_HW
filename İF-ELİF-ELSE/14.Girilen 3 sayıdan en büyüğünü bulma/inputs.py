def get_numbers(number):
    while True:
        try:
            numbers = float(input(str(number) + ".sayı: "))

            if numbers <= 0:
                raise ValueError
            else:
                return numbers

        except ValueError:
            print("Geçersiz sayı girdiniz")
