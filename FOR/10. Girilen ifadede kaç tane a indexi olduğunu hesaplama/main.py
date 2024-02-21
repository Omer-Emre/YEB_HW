from inputs import get_txt as g_t

while True:
    txt = g_t()

    a = txt.count("a")

    print("\nMetin belgenizde a harfi", a, "kere geçmektedir")
