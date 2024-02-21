def get_weather():
    while True:
        try:
            weather = float(input("\nHava sıcaklığı: "))

            if weather < -50 or weather > 50:
                raise ValueError
            else:
                return weather

        except ValueError:
            print("Geçersiz hava sıcaklığı girdiniz")
