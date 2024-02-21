get_list = ["B", "İ", "L", "İ", "Ş", "İ", "M"]

get_list.sort()
print(get_list)

get_list = ["B", "İ", "L", "İ", "Ş", "İ", "M"]

get_list.reverse()
print(get_list)

get_list = ["B", "İ", "L", "İ", "Ş", "İ", "M"]

i = get_list.count("İ")
print("listenin içersinde İ harfi", i, "kere geçmektedir")

get_list = ["B", "İ", "L", "İ", "Ş", "İ", "M"]

elements_to_remove = ["Ş", "İ"]

for element in elements_to_remove:
    get_list.remove(element)

print(get_list)
