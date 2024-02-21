from inputs import get_luggage as g_l
from classes import calculation_luggage as c_l

while True:
    luggage = g_l()
    to_match_luggage = c_l(luggage)

    calculation = c_l.calculation(to_match_luggage)

    if luggage > 20:
        print("\nFazla bagaj için:", calculation, "tl ödemelisiniz")

    else:
        print("\nHerhangi bir ücret ödemeniz gerekmiyor")
