def get_luggage():
    while True:
        try:
            luggage = float(input("\nKaç kg'ramlık yer istersiniz: "))

            if luggage <= 0:
                raise ValueError
            else:
                return luggage

        except ValueError:
            print("Geçersiz işlem girdiniz")
