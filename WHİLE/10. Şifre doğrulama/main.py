from inputs import get_password as g_p

while True:
    password = g_p()

    if password == "Python":
        print("\nGiriş başarılı")
        break

    else:
        print("Tekrar deneyiniz")
