from inputs import *

number_1 = get_number_1()
number_2 = get_number_2()

to_match_number_1 = number_1
add = 0
divide = 1

for calculation_average in range(to_match_number_1, number_2):
    add += to_match_number_1
    divide = add / to_match_number_1
    to_match_number_1 += 1
print("\nOrtalama:", divide)
