from inputs import get_size_and_weight as s_k
from classes import calculator_vki as c_v

while True:
    to_match_size = s_k()

    size = to_match_size[0]()
    weight = to_match_size[1]()

    to_match_calculator_vki = c_v(size, weight)
    calculator_vki = c_v.calculator(to_match_calculator_vki)

    if calculator_vki < 25:
        print("\nNormal:", calculator_vki)

    elif calculator_vki < 30:
        print("\nKilolu:", calculator_vki)

    elif calculator_vki >= 30:
        print("\nObez", calculator_vki)

    elif calculator_vki <= 35:
        print("\nCiddi obez:", calculator_vki)
