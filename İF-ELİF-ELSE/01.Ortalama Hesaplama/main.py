from inputs import get_numbers as g_n
from classes import notes_calculation as n_c

while True:
    number_1 = g_n("\n1")
    number_2 = g_n(2)
    performance = g_n("performans")

    to_match_numbers = n_c(number_1, number_2, performance)
    calculation = n_c.print_calculation(to_match_numbers)

    if calculation < 50:
        print("\nBaşarısız:", calculation)

    else:
        print("\nBaşarılı:", calculation)
