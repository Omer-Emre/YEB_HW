def get_angles(angle):
    while True:
        try:
            get_angle = float(input(str(angle) + ".açı: "))

            if get_angle == 0 or get_angle > 180 or get_angle == 180:
                raise ValueError
            else:
                return get_angle

        except ValueError:
            print("Geçersiz açı girdiniz")
