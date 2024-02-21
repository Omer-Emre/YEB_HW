from inputs import get_numbers as g_n

add = 0
decision = 0

while True:
    numbers = g_n()

    if numbers == 1:
        break

    try:
        number = numbers
        add += number
        decision += 1
    except ValueError:
        print("Geçersiz sayı girdiniz")

if decision > 0:
    divide = add / decision
    print("\nOrtalama:", divide)

else:
    print("\nHiç sayı girmediniz")




