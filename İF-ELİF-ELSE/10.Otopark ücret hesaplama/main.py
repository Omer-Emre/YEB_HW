from inputs import get_parking as g_p
from classes import calculation_parking as c_p

while True:
    parking = g_p()

    if parking == 1:
        print("\nOtopark fiyatınız: 5TL'dir")

    elif parking <= 5:
        to_match_parking_one_between_five = c_p(parking)
        calculation_fee_one_between_five = c_p.calculation_one_between_five(to_match_parking_one_between_five)

        print("\nOtopark fiyatınız:", calculation_fee_one_between_five, "TL'dir")

    else:
        to_match_more_five = c_p(parking)
        calculation_fee_more_five = c_p.calculation_more_five(to_match_more_five)

        print("\nOtopark fiyatınız:", calculation_fee_more_five, "TL'dir")

