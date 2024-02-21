from inputs import *

while True:
    processor = get_processor()
    ram = get_ram()

    if processor >= "i7" and ram >= "8gb":
        print("\nKurulum uygun")

    else:
        print("\nKurulum uygun değil")

