def get_password():
    while True:
        try:
            password = input("\nŞifre: ")

            if len(password) == 8:
                return password

            else:
                raise ValueError

        except ValueError:
            print("Geçersiz şifre giridniz")
