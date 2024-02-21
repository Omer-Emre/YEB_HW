from inputs import get_plate as g_p

while True:
    plate = g_p()

    if plate == "06":
        print("\nAnkara")

    elif plate == "07":
        print("\nAntalya")

    elif plate == "08":
        print("\nArtvin")

    else:
        print("\nTürkiye")
