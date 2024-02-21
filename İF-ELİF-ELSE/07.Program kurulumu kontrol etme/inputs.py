def get_processor():
    while True:
        try:
            processor = input("\nBilgisayar işlemcisi nedir? : ").lower()

            if processor <= "0" or processor > "i9":
                raise ValueError
            else:
                return processor

        except ValueError:
            print("Geçersiz işlemci girdiniz")


def get_ram():
    while True:
        try:
            return input("Bilgisayar ram ne kadar? : ")
        except ValueError:
            print("Geçersiz ram girdiniz")
