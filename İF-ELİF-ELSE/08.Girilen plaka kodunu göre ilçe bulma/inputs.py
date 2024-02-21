def get_plate():
    while True:
        try:
            plate = input("\nPlaka numarası: ")

            if plate <= "0" or plate > "81":
                raise ValueError
            else:
                return plate

        except ValueError:
            print("Geçersiz plaka kodu")
