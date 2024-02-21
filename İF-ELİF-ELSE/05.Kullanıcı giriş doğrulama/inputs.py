def get_user_name():
    while True:
        try:
            return input("\nKullanıcı adı: ")
        except Exception:
            print("Geçersiz kullanıcı adı girdiniz")


def get_password():
    while True:
        try:
            return input("Şifre: ")
        except Exception:
            print("Geçersiz şifre girdiniz")
