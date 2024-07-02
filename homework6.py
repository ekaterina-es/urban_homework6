# работа со словарями
my_dict = {"Elena": 1998, "Alla": 1989, "Polina": 2001}
print("Dict:", my_dict)
print("Existing value:", my_dict["Alla"])
print("Not existing value:", my_dict.get("Sonya", "None"))
my_dict.update({"Vanya": 1999,
                "Lera": 1988})
del_value = my_dict.pop("Alla")
print("Deleted value:", del_value)
print("Modified dictionary:", my_dict)
# работа с множествами
my_set = {5, 5, 5, 3, 3, "October", "June", "June", "May", (1, 2, 3)}
print("Set:", my_set)
my_set.add(True)
my_set.add(88)
my_set.remove("May")
print("Modified set:", my_set)
