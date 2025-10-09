my_list = [10, 20, 30, 40, 10, 15, 25, 35]
# 
# print(my_list)
# print("Item 2 from list is", my_list[2])
# my_list[3] = 100
# print("Item 3 from list is", my_list[3])
# my_list.append(50)
# print(my_list)
# my_list.remove(30)
# print(my_list)
# del my_list[2]
# print(my_list)

my_tuple = (10, 20, 30, 40, 10, 15, 25, 35)

# print("My tuple is", my_tuple)
# print("Item 2 from tuple is", my_tuple[2])
# my_tuple[3] = 100
# print("Item 3 from list is", my_tuple[3])

my_set = {10, 20, 30, 40, 10, 15, 25, 35}
my_this = {45}
my_that = {10, 400, 1000}

# print(my_set)
# my_set.add(500)
# print(my_set)
# my_set.remove(40)
# print(my_set)
# print(f"Union of {my_set} and {my_this} is", my_set.union(my_this))
# print(f"Intersection of {my_set} and {my_that} is", my_set.intersection(my_that))

my_family = { "husband" : "Jeff",
              "wife" : "Sue",
              "dog" : "Ginny",
              "extra" : "Extra"
            }

print(my_family)
print(my_family['dog'])
my_family['dog'] = "Virginia Wolf"
print(my_family)
my_family["cat"] = "Gabby"
print(my_family)
del my_family['extra']
print(my_family)



