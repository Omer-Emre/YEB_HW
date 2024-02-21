def get_txt():
    while True:
        try:
            txt = input("\nMetin belgeniz: ")

            if len(txt) == 0:
                raise ValueError

            else:
                return txt

        except ValueError:
            print("Geçersiz metin belgesi girdiniz")
