def get_angles(angle):
    while True:
        try:
            angles = float(input(str(angle) + ".açı: "))

            if angles <= 0 or angles >= 180:
                raise ValueError
            else:
                return angles

        except ValueError:
            print("Geçersiz açı girdiniz")
