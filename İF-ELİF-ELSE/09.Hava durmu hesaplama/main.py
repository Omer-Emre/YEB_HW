from inputs import get_weather as g_w

while True:
    weather = g_w()

    if weather <= 5:
        print("\nSoğuk")

    elif weather <= 14:
        print("\nIlık")

    else:
        print("\nSıcak")
