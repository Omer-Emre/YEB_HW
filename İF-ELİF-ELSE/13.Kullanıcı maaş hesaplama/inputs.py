def get_name_and_wage_year():

    def get_name():
        while True:
            try:
                name = str(input("\nİsim: "))

                if len(name) < 2:
                    raise ValueError
                else:
                    return name

            except ValueError:
                print("Geçersiz isim girdiniz")

    def get_wage():
        while True:
            try:
                wage = int(input("Maaş: "))

                if wage <= 7500:
                    raise ValueError
                else:
                    return wage

            except ValueError:
                print("Geçersiz maaş girdiniz: ")

    def get_year():
        while True:
            try:
                year = int(input("İş yerinizde kaç yıl çalıştınız? : "))

                if year < 0 or year >= 100:
                    raise ValueError
                else:
                    return year

            except ValueError:
                print("Geçersiz yıl girdiniz")

    return get_name, get_wage, get_year
