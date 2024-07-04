# Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter a number you want to print table of this number: "))

for i in range(1, 11):
    print(f"{num} X {i} =", num * i)
