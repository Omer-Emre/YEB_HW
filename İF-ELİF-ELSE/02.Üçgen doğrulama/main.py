from inputs import get_angles as g_a
from classes import angles_calculation as a_c

angle_1 = g_a(1)
angle_2 = g_a(2)
angle_3 = g_a(3)

to_match_angles = a_c(angle_1, angle_2, angle_3)
result = to_match_angles.calculation()

if result < 180:
    print(f"\n{result}: Bu bir üçgen değildir")

elif result == 180:
    print(f"\n{result}: Bu bir üçgendir")

else:
    print(f"\n{result}: Bu bir üçgen değildir")
