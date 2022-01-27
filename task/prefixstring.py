
list1 = ["anirudh", "entersoft", "python", "language", "hyderabad","developer"]

print(" The list is : " + str(list1))

list2 = ["a","p"]


result = [ele for ele in list1 if any(ele.startswith(el) for el in list2)]

print("The extracted prefix strings list : " , (result))



#USING COMMAND LINE ARGUMENT
"""import sys
list1 = ["anirudh", "entersoft", "python", "language", "hyderabad","developer"]

print(" The list is : " + str(list1))

list2 = sys.argv[1:]

result = [i for i in list1 if any(i.startswith(x) for x in list2)]

print(" prefix strings list : " , (result))"""



