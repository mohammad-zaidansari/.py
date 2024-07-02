# Can we have a set with 18 int and "18" str as a value in it ? 

a = set()

num1 = int(input("enter a number (int): "))
a.add(num1)
num2 = input("enter a number (str): ")
a.add(num2)

print(a)

# yes we can store it 