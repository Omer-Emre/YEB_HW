from inputs import get_angles as g_a

while True:
    angle_1 = g_a(f"\n{1}")
    angle_2 = g_a(2)
    angle_3 = g_a(3)

    if angle_1 == angle_2 == angle_3:
        print("\nEşkenar üçgen")

    elif angle_1 != angle_2 != angle_3:
        print("\nÇeşitkenar üçgen")

    else:
        print("\nİkizkenar üçgen")
