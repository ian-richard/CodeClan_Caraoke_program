ages = [5, 15, 64, 27, 84, 26]

odd_ages  = [age for age in ages if age % 2 != 0]
print(odd_ages)

chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]

chars_10 = [name for name in chicken_names if len(name) > 10]
name_start = [name for name in chicken_names if name[0] == "H"]
print(name_start)
# print(chars_10)

words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

first_list = [name[0].lower() for name in words]
print(first_list)