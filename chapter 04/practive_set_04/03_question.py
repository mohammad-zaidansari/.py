a = ("zaid", 5, 'a', 35, 34.05)
print(type(a))

new_tuple = (a + ("talha", 45))
print(new_tuple)
print("tuple can't change old tuple: ", a)

a[2] = "34"