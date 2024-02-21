from inputs import *

while True:
    number_1 = get_number_1()
    number_2 = get_number_2()

    verification = number_1
    add = 0

    for number_add in range(verification, number_2):
        add += verification
        verification += 1
    print("\nToplam:", add)
