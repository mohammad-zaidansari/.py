file_path = "/Users/mzaid/Desktop/PYTHON/chapter 09/file.txt"
f = open("file.txt", "rb")
data = f.read()
print(data)
print(type(data))
print(len(data))
f.close()


f = open("file.txt", "r")  # by deafult "r" means read mode 
data = f.read()
print(data)