from inputs import *

number_1 = get_number_1()
number_2 = get_number_2()

connec = number_1
add = 0

while connec < number_2:
    add += connec
    connec += 1
print("Toplam:", add)
