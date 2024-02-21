from inputs import get_name_and_wage_year as n_w_y
from classes import calculation_time_wage as t_w

while True:
    name = n_w_y()[0]()
    wage = n_w_y()[1]()
    year = n_w_y()[2]()

    to_match_time_wage = t_w(wage, year)

    if year < 5:
        time_wage = t_w.calculation_time_15(to_match_time_wage)
        print("\nSayın", name, "zaamlı maaşınız", time_wage, "TL'dir")

    elif year <= 10:
        time_wage = t_w.calculation_time_15(to_match_time_wage)
        print("\nSayın", name, "zaamlı maaşınız", time_wage, "TL'dir")

    else:
        time_wage = t_w.calculation_time_25(to_match_time_wage)
        print("\nSayın", name, "zaamlı maaşınız", time_wage, "TL'dir")

