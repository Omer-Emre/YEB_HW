def get_cinema_or_theatre_and_student_or_not():

    def cinema_theatre():
        while True:
            try:
                get_cinema_theatre = str(input("\nSinemayamı gitmek istersiniz? yoksa tiyatroyamı? (S/T): ")).lower()

                if get_cinema_theatre == "s" or get_cinema_theatre == "t":
                    return get_cinema_theatre
                else:
                    raise ValueError

            except ValueError:
                print("Geçersiz seçim yaptınız")


    def student_or_not():
        while True:
            try:
                get_student_or_not = str(input("Öğrencimisiniz? yoksa değilmi? (E/H): ")).lower()

                if get_student_or_not == "e" or get_student_or_not == "h":
                    return get_student_or_not
                else:
                    raise ValueError

            except ValueError:
                print("Geçersiz seçim yaptınız")

    return cinema_theatre, student_or_not
