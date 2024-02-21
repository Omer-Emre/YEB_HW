from inputs import get_product as g_p
from classes import *

while True:
    product_1 = g_p(f"\n{1}")
    product_2 = g_p(2)

    to_match_product = calculation_products(product_1, product_2)

    to_match_not_discount = calculation_products.calculation(to_match_product)
    to_match_discount = calculation_products.calculation_discount(to_match_product)

    if to_match_not_discount > 200:
        print("\nÖdenecek miktar indirimden sonra", to_match_discount, "TL'dir")

    else:
        print("\nÖdenecek miktar ", to_match_not_discount, "TL'dir")
