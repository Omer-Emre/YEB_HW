from inputs import get_numbers as g_n
from classes import calculator_big_number as b_n

while True:
    number_1 = g_n(1)
    number_2 = g_n(2)
    number_3 = g_n(3)

    if number_1 == number_2 == number_3:
        print("\n3 tane aynı sayı girdiniz")

    else:
        to_match_calculator_number = b_n(number_1, number_2, number_3)
        calculator_numbers = b_n.calculator(to_match_calculator_number)

        print("\nEn büyük sayı:", calculator_numbers)
