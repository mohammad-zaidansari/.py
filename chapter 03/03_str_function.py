name = "Muhammad"

print(len(name))
print(name.endswith('mad'))
print(name.startswith("mu")) #false bcs M is capital in the string
print(name.count("a")) #bcs tow a in the given string 

name = "Zaid"
capitalized_name = name.capitalize()  #only first latter convert into capital latter.
all_upper = name.upper()
all_lower = name.lower()
print(all_lower)
print(all_upper)
print(capitalized_name) 

name2 = "Hello world"
index = name2.find("world")
print(index)

replace = "Muhammad Zaid"
replace_str = replace.replace("Zaid", "Talha")
print(replace_str)

name3 = "Talha khan Zaid"
split_list = name3.split()
print(split_list)

name4 = "   muhammad zaid!" #removing all spaces and symbol from the string
strip_list = name4.strip("!")
strip_list = strip_list.strip()
print(strip_list)   # muhammad zaid


name = "zaid"
print(name.startswith("z")) # this method return value Ture and False
