from inputs import *

while True:
    user_name = get_user_name()
    password = get_password()

    if user_name == "Türkiye" and password == "1925":
        print("\nGiriş başarılı")
        break

    else:
        print("\nKullanıcı adı veya şifre hatalı")
