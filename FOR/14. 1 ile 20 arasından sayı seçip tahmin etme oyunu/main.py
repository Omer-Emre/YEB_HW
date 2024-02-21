from inputs import get_number as g_n

for random_number in range(1):
    import random
    numbers = random.randint(1, 21)

    while True:
        number = g_n()

        if number > numbers:
            print("Sayınızı küçültün")

        elif number < numbers:
            print("Sayınızı büyültün")

        else:
            print("\nTEBRİKLER", numbers, "sayısını bulup oyunu kazandınız")
            break
