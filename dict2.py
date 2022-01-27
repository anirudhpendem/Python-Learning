my_dict = {"a" :10 , "b" : 20, "c" :30 , "d" :40}

new_key = "A"

old_key = "a"

my_dict[new_key] = my_dict.pop(old_key)

print(my_dict)

my_dict["d"] = 50

print(my_dict)