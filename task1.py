list1 = ["anirudh", "entersoft", "python", "language", "hyderabad","developer"]

print(" The list is : " + str(list1))

list2 = ["ani", "la","de"]

for i in list1:
    for x in i:
        if x: 
            res = any(i.startswith(list2))

# checking for all possible allowed prefixes using any()
#res = [ele for ele in list1 if any(ele.startswith(el) for el in list2)]

# printing result
print("The extracted prefix strings list : " , (res))
