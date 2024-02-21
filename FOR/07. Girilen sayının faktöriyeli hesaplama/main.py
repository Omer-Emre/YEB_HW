from inputs import get_number as g_n

while True:
    number = g_n()
    multiplacition = 1

    for calculation in range(1, number + 1):
        multiplacition *= calculation
    print("\nFaktöriyel:", multiplacition)
