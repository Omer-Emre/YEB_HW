def get_numbers(numbers):
    while True:
        try:
            get_number = int(input(str(numbers) + " not: "))

            if get_number < 0 or get_number > 100:
                raise ValueError
            else:
                return get_number

        except ValueError:
            print("Geçersiz not girdiniz")
