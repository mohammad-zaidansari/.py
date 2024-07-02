a={
    "name":"harry",
    "from":"india",
    "marks":[92,98,96], 
    1: "muhammd"
    }

print(a.items())

print(a.keys())

a.update({"name": "zaid"}) #update key values
a.update({"city":"lmp"})   #update dict with key & value
print(a)

print(a.get("name"))  # return the value store in name Key


b = {
    "zaid": 100,
    "talha": 44,
    "asif": 21
}

# print(b.get("zaid"))  # print None
# print(b["zaid"])      # return an error

# dict.clear()
# b.clear()
# print(b)

# dict.copy()
new_b = b.copy()
print(new_b)

# Returns the value for key if key is in the dictionary, else default.

my_dict = {
    "apple": 1,
    "banana": 2
    }
value = my_dict.get("apple")  # Output: 1
value = my_dict.get("cherry", "empty")  # Output: "empty" is a default value
print(value)

# Removes the specified key and returns the corresponding value. If the key is not found, default is returned if provided, otherwise a KeyError is raised.

my_dict = {"apple": 1, "banana": 2}
value = my_dict.pop("apple")  # Output: 1
value2 = my_dict.popitem()
print(my_dict)   # Output: {'banana': 2}

# dict.values()
my_dict = {"apple": 1, "banana": 2}
values = my_dict.values()
print(values)  # Output: dict_values([1, 2])


# Creates a new dictionary with keys from seq and values set to value (default is None).

keys = ["apple", "banana"]
new_dict = dict.fromkeys(keys, "0s")
print(new_dict)  # Output: {'apple': 0, 'banana': 0}