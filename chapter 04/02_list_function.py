my_list = [1, 5, 2, 34, 45, 3, 6, 3]

my_list.append(4)

print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

my_list.insert(3, "zaid")  # insert zaid at index 3 on the list 
print(my_list)

my_list.remove("zaid")
print(my_list)

my_list.remove(3)  # remove 3 in the list which 3 first in the list
print(my_list)

my_list.pop(3)
print(my_list)

my_list = [1, "zsif", 2, 3]
count = my_list.count(2)
print(count)
# count is 2
