from inputs import get_number as g_n

while True:
    number = g_n()

    if number % 3 == 0 and number % 5 == 0:
        print("\n15'e tam bölünür")

    else:
        print("\n15'e tam bölünmez")

