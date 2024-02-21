def get_number():
    while True:
        try:
            number = int(input("\n1 ile 5 arasında bir sayı girin: "))

            if number == 3:
                print("\n3 sayısı girildi ve döngü sona erdi")
                break

            else:
                print("tekrar deneyin")

        except ValueError:
            print("Geçersiz sayı girdiniz")


get_number()
