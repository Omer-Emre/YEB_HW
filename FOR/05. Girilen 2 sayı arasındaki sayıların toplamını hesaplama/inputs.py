def get_number_1():
    while True:
        try:
            number_1 = int(input("\n1.sayı: "))

            if number_1 == 0:
                raise ValueError

            else:
                return number_1

        except ValueError:
            print("Geçersiz sayı girdiniz")


def get_number_2():
    while True:
        try:
            number_2 = int(input("2.sayı: "))

            if number_2 == 0:
                raise ValueError

            else:
                return number_2

        except ValueError:
            print("Geçersiz sayı girdiniz")
