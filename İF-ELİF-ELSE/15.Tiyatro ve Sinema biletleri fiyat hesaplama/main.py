from inputs import get_cinema_or_theatre_and_student_or_not as g_c_t_s_n
from classes import calculator_cinema_theatre_and_student_or_not as c_c_t_s_n

while True:
    cinema_or_theatre = g_c_t_s_n()[0]()
    stundet_or_not = g_c_t_s_n()[1]()

    if cinema_or_theatre == "s" and stundet_or_not == "e":
        to_match_calculator_cinema = c_c_t_s_n()[0]()
        print("\nİndirimli fiyat:", to_match_calculator_cinema, "TL'dir")

    elif cinema_or_theatre == "s" and stundet_or_not == "h":
        print("\nFiyat: 15 TL'dir")

    if cinema_or_theatre == "t" and stundet_or_not == "e":
        to_match_calculator_theatre = c_c_t_s_n()[1]()
        print("\nİndirimli fiyat:", to_match_calculator_theatre, "TL'dir")

    elif cinema_or_theatre == "t" and stundet_or_not == "h":
        print("\nFiyat: 10 TL'dir")
